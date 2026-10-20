import torch

x = torch.tensor(2.0)
y = torch.tensor(10.0)
w = torch.tensor(3.0, requires_grad=True)

prediction = w * x
loss = (prediction - y) ** 2

print("prediction:", prediction.item())
print("loss:", loss.item())

loss.backward()
print("gradient:", w.grad.item())

#2A

#y_hat = w*x = 3*2
#loss = (y_hat-y)**2 -> (w*x-y)**2
#dL/dw -> with chain rule: 2*(w*x-y)*x

z = 2*(w*x-y)*x
print(z)

#2B

learning_rate = 0.01
print("w before:", w.item())
print("gradient:", w.grad.item()) #the tensor
with torch.no_grad():
    w -= learning_rate * w.grad #gradient descent
print("w after:", w.item()) #The actual value

for step in range(1000):
    prediction_1 = w *x
    loss_1 = (prediction_1 - y) **2
    loss_1.backward()
    with torch.no_grad():
        w -= learning_rate *w.grad # w is a weight that is learned during training.
    # Training may converge when the gradient becomes small and the loss stops decreasing significantly.
    w.grad.zero_()

    print(w)