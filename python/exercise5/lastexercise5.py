import numpy as np
import matplotlib.pyplot as plt

#Data simulation:

rng = np.random.default_rng()
def data_generator():
    torque = rng.uniform(5,50,size=100)
    speed = rng.uniform(-5,5,size=100)
    data_table = np.column_stack((torque,speed))
    return data_table

data_raw = data_generator()

#Partitioning for machine learning:
data_machine = data_raw.copy()
rng.shuffle(data_machine)

train_data = data_machine[:80]
test_data = data_machine[80:]

print(test_data)

#exporting to csv:

np.savetxt('test_data.csv', test_data, delimiter=',', header='torque,speed', comments='')
np.savetxt('train_data.csv', train_data, delimiter=',', header='torque,speed', comments='')


#plotting of data

plt.scatter(train_data[:,0], train_data[:,1])
plt.xlabel('torque')
plt.ylabel('speed')
plt.show()