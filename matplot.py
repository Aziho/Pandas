import matplotlib.pyplot as plt
import numpy as np
num_means= 4
num_groups=3
bc_means = [20, 35, 30, 35, 27]
alberta_means = [25, 32, 34, 20, 25]
sk_means= [ 18, 28, 32, 24, 31]
ind=np.arange(num_means)
width=0.2
plt.bar(ind,bc_means[:4],width,label='BC')
plt.bar(ind+width,alberta_means[:4],width,label='AL')
plt.bar(ind+width+width,sk_means[:4],width,label='SK')
qlist=['Q1','Q2','Q3','Q4']
plt.xticks(ind+width,qlist)
plt.ylabel('Revenue')
plt.legend(loc='best')
plt.title("Quarterly Revenue By Province")
plt.show()
