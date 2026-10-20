import torch


#angle, angular velocity, acceleration
imu = torch.tensor([
    [ 0.02,  0.10, 9.79],
    [ 0.03,  0.08, 9.81],
    [-0.01, -0.04, 9.84],
], dtype=torch.float32)

print(imu)
print(imu.shape)
print(imu.dtype)

#1A
angle = imu[:,0]
print("Angle is: ",angle)

#1B
mean = imu.mean(dim=0) #calculates the mean of each column
std = imu.std(dim=0)
imu_normalized = (imu-mean) / std
print(imu_normalized)
print("Normalized mean: ",imu_normalized.mean(dim=0)) #normalized tensor
print("Normalized std:",imu_normalized.std(dim=0))

#Normalizing data makes it easier for a NN to learn of the dataset.
#Makes the values into the same scale, so that large og small values don't dominate the dataset.

#1C

random_batch = torch.rand(32,6)
print(random_batch)
reshaped = random_batch.T
print(reshaped)