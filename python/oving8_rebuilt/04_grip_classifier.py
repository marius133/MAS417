import math
import torch
from torch import nn
n = 2000
m = 3.0
g = 9.81

slope_deg = 35 * torch.rand(n, 1)
mu = 0.15 + 0.40 * torch.rand(n, 1)
downforce_n = 15 * torch.rand(n, 1)

theta = torch.deg2rad(slope_deg)
normal_force = m * g * torch.cos(theta) + downforce_n
available = mu * normal_force
required = m * g * torch.sin(theta)

y = (available > required).float()
x = torch.cat((slope_deg, mu, downforce_n), dim=1)

# TODO: shuffle og train/test-splitt

#4A

# for i in range(len(x)):
#     for j in range(i + 1, len(x)):
#         slope_close = abs(x[i, 0] - x[j, 0]) < 1.0
#         friction_close = abs(x[i, 1] - x[j, 1]) < 0.02
#
#         if slope_close and friction_close:
#             if y[i] != y[j]:
#                 print("sample i:", x[i], y[i])
#                 print("sample j:", x[j], y[j])
#                 break
#


#4C split data before training
indices = torch.randperm(n)
split = int(0.8*n)

train_indices = indices[:split] # indices up to 1600
test_indices = indices[split:] # indices from 1600 to 2000

x_train = x[train_indices]
y_train = y[train_indices]

x_test = x[test_indices]
y_test = y[test_indices]









#4B

#MLP: Multilayer perceptron
model = nn.Sequential(nn.Linear(3, 8),nn.ReLU(), nn.Linear(8, 1))

criterion = nn.BCEWithLogitsLoss() #loss function for binary classification
optimizer = torch.optim.SGD(model.parameters(),lr= 0.001)

for epoch in range(1000):
    optimizer.zero_grad()
    logits = model(x_train)
    loss = criterion(logits, y_train)
    loss.backward()
    optimizer.step()



