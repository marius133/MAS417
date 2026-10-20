import torch
from torch import nn

# 200 kunstige motorprøver
n = 200
voltage = 12 + 12 * torch.rand(n, 1)
load_torque = 0.0 + 0.8 * torch.rand(n, 1)
noise = 120 * torch.randn(n, 1)
rpm = 420 * voltage - 850 * load_torque + noise

x = torch.cat((voltage, load_torque), dim=1) # Combines voltage and load_torque into one [200, 2] input tensor:
# 200 samples with 2 features per sample.
y = rpm

class MotorModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)

    def forward(self, x):
        return self.linear(x)

model = MotorModel()
criterion = nn.MSELoss()

# The optimizer updates the model parameters using their gradients.
# SGD = Stochastic Gradient Descent.
# model.parameters() gives the optimizer the weights and biases it should update.
# Adam also uses gradients, but additionally keeps statistics about past gradients to adapt the parameter updates.

optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

for epoch in range(100000):
    optimizer.zero_grad() #removes old gradients
    prediction = model(x) #make a prediction by using the current weights and biases
    loss = criterion(prediction, y) #Calculates loss: L = (y_hat-y)² -> good prediction = small loss, bad prediction = greater loss
    loss.backward() #calculates the gradients by going backwards through the computational graph (starts at the loss)
    optimizer.step() #updates the parameters: w_new = w_old - lr*gradient


print("Learned weights:", model.linear.weight)
print("Learned bias:", model.linear.bias)