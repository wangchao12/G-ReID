import scipy.io as scio
import matplotlib.pyplot as plt
import numpy as np
import math


x=np.array([1,5,10,15,20])
ry0=np.array([70.4,82.7,87.7,91.4,92.6])
ry1=np.array([67.9,80.2,86.4,88.9,91.4])
ry2=np.array([65.4,82.7,84.0,88.9,91.4])
ry3=np.array([61.7,77.8,84.0,87.7,88.9])
ry4=np.array([59.3,79.0,82.7,87.7,87.7])
dy0=np.array([65.9,86.4,92.0,95.5,98.9])
dy1=np.array([59.1,83.0,88.6,93.2,97.7])
dy2=np.array([61.4,78.4,83.0,86.4,92.6])
dy3=np.array([53.4,79.5,86.4,92.0,93.2])
dy4=np.array([35.2,70.5,78.4,85.2,89.8])
#plt.figure(num=5)
plt.ylim(0.0,100.0)
plt.figure(num=5,figsize=(12,5))
plt.subplot(122)
plt.xlabel('Rank')
plt.ylabel('Accuracy(Road)')
plt.grid(True)
plt.plot(x,ry0,'gs-',linewidth=2,label='conv1')
plt.plot(x,ry1,'bs-',linewidth=2,label='conv2_x')
plt.plot(x,ry2,'rs-',linewidth=2,label='conv3_x')
plt.plot(x,ry3,'ys-',linewidth=2,label='conv4_x')
plt.plot(x,ry4,'ks-',linewidth=2,label='conv5_x')
plt.legend(bbox_to_anchor=(0.97,0.55))
plt.subplot(121)
plt.xlabel('Rank')
plt.ylabel('Accuracy(DukeMTMC)')
plt.grid(True)
plt.plot(x,dy0,'gs-',linewidth=2,label='conv1')
plt.plot(x,dy1,'bs-',linewidth=2,label='conv2_x')
plt.plot(x,dy2,'rs-',linewidth=2,label='conv3_x')
plt.plot(x,dy3,'ys-',linewidth=2,label='conv4_x')
plt.plot(x,dy4,'ks-',linewidth=2,label='conv5_x')
plt.legend(bbox_to_anchor=(0.97,0.55))
plt.savefig('/home/nvlab/result/compare.pdf')