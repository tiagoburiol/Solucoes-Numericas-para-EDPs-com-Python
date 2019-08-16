% matplotlib inline
from matplotlib.pyplot import *
import matplotlib
import numpy as np


T = np.zeros([30,30])
T[-1, :] = 50
T[:, -1] = 100
T[0,  :] = 75 

lamb = 1.5

#print(T)
for n in range(50):
    #print ("iteração:", n+1)
    for i in range(1,len(T)-1):
        for j in range(1,len(T)-1):
            Tnovo = (T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])/4
            T[i,j]=lamb*Tnovo+(1-lamb)*T[i,j]
            #print ("T[",i,",",j,"]=", T[i,j])
        
# tabela de cores para o plot
dic = {'red': ((0., 1, 1), (0.00000000001, 0, 0), (0.66, 1, 1), (0.89,1, 1), (1, 0.5, 0.5)), 
       'green': ((0., 1, 1), (0.00000000001, 0, 0), (0.375,1, 1), (0.64,1, 1), (0.91,0,0), (1, 0, 0)), 
       'blue': ((0., 1, 1), (0.00000000001, 1, 1), (0.34, 1, 1), (0.65,0, 0), (1, 0, 0))}
my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',dic,256)

# plot
pcolor(T,cmap=my_cmap)
colorbar()
show()