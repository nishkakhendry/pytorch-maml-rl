import numpy as np

f = np.load('C:/Users/nishk/OneDrive/Desktop/LT/AML/pytorch-maml-rl/maml-2dnavig/results.npz',allow_pickle=True)
# print(len(f['tasks']))
print(len(f['valid_returns'][0]))