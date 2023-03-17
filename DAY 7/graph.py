'''
import matplotlib.pyplot as plt
plt.plot([0,1,2],[0,1,2])
plt.show()
'''

import matplotlib.pyplot as plt
plt.figure()
x1=[0,1]
y1=[0,1]
x2=[0,1]
y2=[0,2]
x3=[0,1]
y3=[0,0.5,]
x4=[0,1]
y4=[1,-1]

plt.plot(x1,y1,'y',
         x2,y2,'r',
         x3,y3,'g',
         x4,y4,'b')
plt.show()

