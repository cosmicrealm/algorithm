import torch.nn as nn
import torch.nn.functional as F
import torch
class MHA(nn.Module):
    def __init__(self,hidden_dim,head_num,attn_type='mha',num_group=2):
        super(MHA,self).__init__()
        self.head_num = head_num
        self.hidden_dim = hidden_dim
        assert hidden_dim % self.head_num == 0
        self.head_dim = hidden_dim // self.head_num
        self.attn_type = attn_type
        self.num_group = num_group
        self.wq = nn.Linear(hidden_dim,hidden_dim)
        if self.attn_type=='mha':
            self.wk = nn.Linear(hidden_dim,hidden_dim)
            self.wv = nn.Linear(hidden_dim,hidden_dim)
        elif self.attn_type=='mqa':
            self.wk = nn.Linear(hidden_dim,self.head_dim)
            self.wv = nn.Linear(hidden_dim,self.head_dim)
        elif self.attn_type == 'gqa':
            self.wk = nn.Linear(hidden_dim,self.num_group*self.head_dim)
            self.wq = nn.Linear(hidden_dim,self.num_group*self.head_dim)
        
        self.out = nn.Linear(hidden_dim,hidden_dim)
    
    def reshape(self,x, head_num=None):
        b,l,d = x.shape
        if head_num == None:
            x = x.view(b,l,self.head_num,self.head_dim).transpose(1,2)
        else:
            x = x.view(b, l, head_num, self.head_dim).transpose(1, 2)
        return x
    
    def split_head(self,x):
        b,l,d = x.shape
        g = self.num_group
        x = x.view(b,l,g,self.head_dim).transpose(1,2)
        x = x[:,:,None,:,:].expand(b,g,self.head_num//g,l,self.head_dim)
        x = x.reshape(b,self.head_num, l,self.head_dim)
        return x

    def forward(self,x, mask=None,):
        # x is b*l*d
        b,l,d = x.shape
        q = self.wq(x)
        k = self.wk(x)
        v = self.wv(x)
        if self.attn_type == 'mha':
            q = self.reshape(q)
            k = self.reshape(k)
            v = self.reshape(v)
        elif self.attn_type == 'mqa':
            q = self.reshape(q)
            k = self.reshape(k,1)
            v = self.reshape(v,1)
        elif self.attn_type == 'gqa':
            q = self.reshape(q)
            k = self.split_head(k)
            v = self.split_head(v)
            
        score = torch.matmul(q,k.transpose(-1,-2)) / (self.head_dim**0.5)
        if mask is not None:
            score = score + mask * -1e-9
        score = F.softmax(score,dim=-1)
        out = torch.matmul(score,v)
        out = out.transpose(1, 2).contiguous().view(b, l, -1)
        out = self.out(out)
        return out