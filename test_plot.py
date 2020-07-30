# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# reference
# https://matplotlib.org/gallery/index.html

from pylab import *
figure()
plot(range(1,5),'r*') # color option: r,g,b, 
                     #line sytle: -(solid),--(dash),s(square),^(triangle),*(star)
title('title')
xlabel('x')
ylabel('some numbers')
#axis([0,10,0,10])
#grid(b=True, which='both', axis='both')
grid(b=True, which='major', axis='both')

figure()
plot([1,2,3,4],range(1,5))

import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(1,5),'go')
plt.title('title')
plt.xlabel('x')
plt.ylabel('number')
#plt.axis([0,4])
grid(b=True, which='both', axis='x')
#grid(b=True, which='minor', axis='x')

figure()
plot([1,2,3,4],'r^',[5,6,7,8],'bs')
#legend('data1','data2')

# scatter
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
figure()
plt.scatter(x,y)


# Bar horizontal
figure()
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

# fig, ax =plt.subplot()
# ax.bar(y_pos, performance, yerr=error, align='center')
# ax.set_xticks(y_pos)
# ax.set_yticklabels(people)
# ax.invert_xaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# plt.show()