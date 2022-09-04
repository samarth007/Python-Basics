import numpy as np

# l=tuple(map(int,input().split()))
# print(l)
# print(np.zeros(l,dtype=int))
# print(np.ones(l,dtype=int))

n_row,m_col,n_dim=map(int,input().strip().split())
print(np.zeros((n_row,m_col,n_dim),dtype=int))
print(np.ones((n_row,m_col,n_dim),dtype=int))