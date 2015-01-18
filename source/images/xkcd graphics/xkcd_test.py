__author__ = 'Huis'
import numpy as np
import random
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from xkcdify import XKCDify

#TODO cleanup this script

#Vee model
np.random.seed(0)

ax = pl.axes()

x = np.linspace(1, 1.2, 50)
ax.plot(x, 6 - x, 'black', lw=1)
x = np.linspace(1.6, 3.7, 50)
ax.plot(x, 6 - x, 'black', lw=1)
x = np.linspace(4.2, 5, 50)
ax.plot(x, 6 - x, 'black', lw=1)

x = np.linspace(5, 5.8, 50)
ax.plot(x, x - 4, 'black', lw=1)
x = np.linspace(6.3, 8.3, 50)
ax.plot(x, x - 4, 'black', lw=1)
x = np.linspace(8.7, 9, 50)
ax.plot(x, x - 4, 'black', lw=1)

x = np.linspace(8.7, 9, 50)
ax.plot(x, x - 4, 'black', lw=1)

plt.arrow(6.8, 4.5, -3.6, 0, head_width=0.1, head_length=0.1, color = 'grey')

plt.arrow(2.5, 2.3, -0.8, 0.8, head_width=0, head_length=0, color = 'grey')
plt.arrow(1.4, 3.4, -0.7, 0.7, head_width=0.1, head_length=0.1, color = 'grey')
plt.arrow(0.9, 4.2, 0.8, -0.8, head_width=0.0, head_length=0.0, color = 'grey')
plt.arrow(2.0, 3.1, 0.7, -0.7, head_width=0.1, head_length=0.1, color = 'grey')

# plt.arrow(9.2, 4.2, -1.8, -1.8, head_width=0.1, head_length=0.1, color = 'grey')
plt.arrow(9.2, 4.2, -0.8, -0.8, head_width=0.0, head_length=0.0, color = 'grey')
plt.arrow(8.1, 3.1, -0.7, -0.7, head_width=0.1, head_length=0.1, color = 'grey')
plt.arrow(6, 2.3, -2, 0, head_width=0.1, head_length=0.1, color = 'grey')

ax.set_title('v-model')
ax.set_xlabel('time')
ax.set_ylabel('high level')
plt.annotate('low level', xy=(-2, 2)).set_rotation(80)
plt.annotate('requirements', xy=(-0, 4.5))
plt.annotate('design', xy=(3, 2))
plt.annotate('development', xy=(5.5, 2))
plt.annotate('integration', xy=(7, 4.5))

ax.legend(loc='lower right')

ax.set_xlim(-1, 10)
ax.set_ylim(0.0, 5.0)

#XKCDify the axes -- this operates in-place
XKCDify(ax, xaxis_loc=0.0, yaxis_loc=-1.0,
        xaxis_arrow='+', yaxis_arrow='',
        expand_axes=True)
prop = fm.FontProperties(fname='Humor-Sans.ttf', size=14)
plt.text(4, 4.7, 'validation', color = 'grey').set_fontproperties(prop)
plt.text(7.5, 3.2, 'verification', color = 'grey').set_fontproperties(prop)
plt.text(3.9, 2.5, 'verification', color = 'grey').set_fontproperties(prop)
plt.text(0.2, 3.2, 'traceability', color = 'grey').set_fontproperties(prop)
pl.show()

#XKCD demo
# np.random.seed(0)
#
# ax = pl.axes()
#
# x = np.linspace(0, 10, 100)
# ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=1, label='damped sine')
# ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=1, label='damped cosine')
#
# ax.set_title('check it out!')
# ax.set_xlabel('x label')
# ax.set_ylabel('y label')
#
# ax.legend(loc='lower right')
#
# ax.set_xlim(0, 10)
# ax.set_ylim(-1.0, 1.0)
#
# #XKCDify the axes -- this operates in-place
# XKCDify(ax, xaxis_loc=0.0, yaxis_loc=1.0,
#         xaxis_arrow='+-', yaxis_arrow='+-',
#         expand_axes=True)
# pl.show()

#vesion 1 xkcd plots
# plt.xkcd()
#
# #uniform probability distribution
# x = np.arange(5)
# y = np.ones(5)
# fig1 = plt.figure()
# plt.xticks([])
# plt.yticks([])
# ax1 = fig1.add_subplot(111)
# ax1.set_ylim([-30, 10])
# ax1.spines['right'].set_color('none')
# ax1.spines['top'].set_color('none')
# plt.rcParams.update({'font.size': 22})
# plt.xlabel('time')
# plt.ylabel('probability of encountering the bug')
# ax1.plot(x, y)
# plt.annotate(
#  'uniform distribution bugs\ni.e. random bugs',
#  xy=(2, 1), arrowprops=dict(arrowstyle='->'), xytext=(0.2, -12))
# plt.show()
#
# #increasing probability distribution
# x = np.arange(5)
# y = np.exp(x)
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# plt.xticks([])
# plt.yticks([])
# ax2.spines['right'].set_color('none')
# ax2.spines['top'].set_color('none')
# plt.rcParams.update({'font.size': 22})
# plt.xlabel('time')
# plt.ylabel('probability of encountering the bug')
# ax2.plot(x, y)
# plt.annotate(
#  'increasing distribution bugs\ni.e. memory leaks',
#  xy=(2.5, 14.3), arrowprops=dict(arrowstyle='->'), xytext=(0.2, 32))
# plt.show()
#
#
# #decreasing probability distribution
# x = np.arange(5)
# y = 1 / np.exp(x)
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# plt.xticks([])
# plt.yticks([])
# ax2.spines['right'].set_color('none')
# ax2.spines['top'].set_color('none')
# plt.rcParams.update({'font.size': 22})
# plt.xlabel('time')
# plt.ylabel('probability of encountering the bug')
# ax2.plot(x, y)
# plt.annotate(
#  'decreasing distribution bugs\ni.e. startup bugs',
#  xy=(1, 0.4), arrowprops=dict(arrowstyle='->'), xytext=(1.5, 0.65))
# plt.show()
#
# #exponential with fill probability distribution
# x = np.arange(5)
# y = 1 / np.exp(x)
# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# plt.xticks([])
# plt.yticks([])
# ax3.spines['right'].set_color('none')
# ax3.spines['top'].set_color('none')
# plt.rcParams.update({'font.size': 22})
# plt.xlabel('x')
# plt.ylabel('f(x)')
# ax3.plot(x, y)
# fillx = [2,3,4]
# filly = 1 / np.exp(fillx)
# plt.fill_between(fillx, filly, color = 'black')
# plt.show()

