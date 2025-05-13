'''
externals modules are made by other programmers

they can give you a lot of functionalities


we use pip install pyautogui

'''

import pyautogui
from time import sleep

sleep(1)

#pyautogui.write('This is written by a computer', interval=0.5)

'''

Exercise

we are going to use the matplotlib to draw a graph

'''

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,5.,0.2)


# plt.plot([1,2,3,4],[1, 4, 9, 16],'ro')
# plt.axis((0,6,0,20))
# plt.ylabel('some numbers')
# plt.show()



# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')

# plt.show()

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()