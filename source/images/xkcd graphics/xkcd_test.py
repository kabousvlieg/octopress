#!usr/bin/env python
__author__ = 'Huis'
import numpy as np
import random
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from xkcdify import XKCDify
import math

def main():
    #VeeModel()
    #testProbPlots()
    docPlots()
    pass

def docPlots():
    ax = pl.axes([0., 0., 2., 2.], frameon=False, xticks=[],yticks=[])
    ax.set_autoscale_on(False)

    drawDoc(0.1,1.3)
    drawDoc(0.6,1.3)
    drawDoc(1.1,1.3)
    drawDoc(0.1,0.7)
    drawDoc(0.6,0.7)
    drawDoc(1.1,0.7)
    drawDoc(0.1,0.1)
    drawDoc(0.6,0.1)
    drawDoc(1.1,0.1)

    plt.annotate('Title\npage', xy=(0.182, 1.55))

    plt.annotate('Index', xy=(0.62, 1.66))
    drawScribble(ax, 0.62, 1.55, 0.04)
    drawScribble(ax, 0.87, 1.55, 0.01)
    drawScribble(ax, 0.62, 1.525, 0.07)
    drawScribble(ax, 0.87, 1.525, 0.01)
    drawScribble(ax, 0.62, 1.5, 0.03)
    drawScribble(ax, 0.87, 1.5, 0.01)
    drawScribble(ax, 0.62, 1.475, 0.04)
    drawScribble(ax, 0.87, 1.475, 0.01)
    drawScribble(ax, 0.62, 1.45, 0.07)
    drawScribble(ax, 0.87, 1.45, 0.01)
    drawScribble(ax, 0.62, 1.425, 0.08)
    drawScribble(ax, 0.87, 1.425, 0.01)

    plt.annotate('Change\ncontrol', xy=(1.12, 1.622))
    drawTable(1.1 + 0.025, 1.3 + 0.025)

    plt.annotate('1. Scope', xy=(0.12, 1.06))
    drawScribble(ax, 0.12, 1.0, 0.25)
    drawScribble(ax, 0.12, 0.975, 0.25)
    drawScribble(ax, 0.12, 0.95, 0.25)
    drawScribble(ax, 0.12, 0.925, 0.25)
    drawScribble(ax, 0.12, 0.9, 0.15)

    drawScribble(ax, 0.12, 0.85, 0.25)
    drawScribble(ax, 0.12, 0.825, 0.25)
    drawScribble(ax, 0.12, 0.8, 0.25)
    drawScribble(ax, 0.12, 0.775, 0.25)
    drawScribble(ax, 0.12, 0.75, 0.15)

    plt.annotate('2. Applicable\n  documents', xy=(0.62, 1.022))
    drawScribble(ax, 0.62, 0.975, 0.005)
    drawScribble(ax, 0.62, 0.95, 0.005)
    drawScribble(ax, 0.62, 0.925, 0.005)
    drawScribble(ax, 0.62, 0.9, 0.005)
    drawScribble(ax, 0.62, 0.875, 0.005)
    drawScribble(ax, 0.62, 0.85, 0.005)
    drawScribble(ax, 0.62, 0.825, 0.005)
    drawScribble(ax, 0.62, 0.8, 0.005)

    drawScribble(ax, 0.64, 0.975, 0.11)
    drawScribble(ax, 0.64, 0.95, 0.13)
    drawScribble(ax, 0.64, 0.925, 0.1)
    drawScribble(ax, 0.64, 0.9, 0.17)
    drawScribble(ax, 0.64, 0.875, 0.18)
    drawScribble(ax, 0.64, 0.85, 0.12)
    drawScribble(ax, 0.64, 0.825, 0.1)
    drawScribble(ax, 0.64, 0.8, 0.11)

    plt.annotate('3. Requirements', xy=(1.12, 1.06))
    drawScribble(ax, 1.12, 1.0, 0.25)
    drawScribble(ax, 1.12, 0.975, 0.25)
    drawScribble(ax, 1.12, 0.95, 0.25)
    drawScribble(ax, 1.12, 0.925, 0.25)
    drawScribble(ax, 1.12, 0.9, 0.15)

    drawScribble(ax, 1.12, 0.85, 0.25)
    drawScribble(ax, 1.12, 0.825, 0.25)
    drawScribble(ax, 1.12, 0.8, 0.25)
    drawScribble(ax, 1.12, 0.775, 0.25)
    drawScribble(ax, 1.12, 0.75, 0.15)

    plt.annotate('4. Detail\n   design', xy=(0.12, 0.422))
    drawDiamond(0.12, 0.22)
    drawDiamond(0.27, 0.35)
    drawBox(0.27, 0.13)
    plt.arrow(0.17, 0.385, 0, -0.1, head_width=0.01, head_length=0.01, color = 'grey')
    plt.arrow(0.22, 0.22, 0.1, -0, head_width=0.00, head_length=0.00, color = 'grey')
    plt.arrow(0.17, 0.35, 0.09, -0, head_width=0.01, head_length=0.01, color = 'grey')
    plt.arrow(0.32, 0.3, 0, -0.105, head_width=0.01, head_length=0.01, color = 'grey')

    plt.annotate('5. Notes', xy=(0.62, 0.46))
    drawScribble(ax, 0.62, 0.4, 0.25)
    drawScribble(ax, 0.62, 0.375, 0.25)
    drawScribble(ax, 0.62, 0.35, 0.25)
    drawScribble(ax, 0.62, 0.325, 0.25)
    drawScribble(ax, 0.62, 0.3, 0.15)

    drawScribble(ax, 0.62, 0.25, 0.25)
    drawScribble(ax, 0.62, 0.225, 0.25)
    drawScribble(ax, 0.62, 0.2, 0.25)
    drawScribble(ax, 0.62, 0.175, 0.25)
    drawScribble(ax, 0.62, 0.15, 0.15)

    plt.annotate('6. Traceability', xy=(1.12, 0.46))
    drawTable(1.1 + 0.025, 0.1 + 0.025)

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
    xaxis_arrow='', yaxis_arrow='',
    expand_axes=True)
    pl.ylim([-0.0,1.85])
    pl.xlim([-0.0,1.5])
    pl.show()


def drawScribble(ax, xpos, ypos, len):
    np.random.seed(0)
    y = []
    x = np.linspace(0 + xpos, len + xpos, 50)
    for n in x:
        y.append(ypos + random.uniform(0,0.01))
    ax.plot(x, y, 'grey', lw=1)

def drawDoc(xoffset, yoffset):
    a4width = 0.3
    plt.arrow(xoffset, yoffset, 0, a4width*1.4142, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + a4width*1.4142, a4width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset, a4width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + a4width, yoffset + a4width*1.4142, 0, -a4width*1.4142, head_width=0, head_length=0, color = 'grey')

def drawTable(xoffset, yoffset):
    width = 0.25
    plt.arrow(xoffset, yoffset, 0, width, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + width, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + width/5, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + 2*width/5, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + 3*width/5, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + 4*width/5, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset, width, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + width, yoffset + width, 0, -width, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + width/3, yoffset + width, 0, -width, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 2*width/3, yoffset + width, 0, -width, head_width=0, head_length=0, color = 'grey')

def drawDiamond(xoffset, yoffset):
    plt.arrow(xoffset, yoffset, 0.05, 0.05, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 0.05, yoffset + 0.05, 0.05, -0.05, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 0.1, yoffset, -0.05, -0.05, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 0.05, yoffset - 0.05, -0.05, 0.05, head_width=0, head_length=0, color = 'grey')

def drawBox(xoffset, yoffset):
    plt.arrow(xoffset, yoffset, 0, 0.05, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + 0.05, 0.1, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 0.1, yoffset + 0.05, 0, -0.05, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 0.1, yoffset, -0.1, 0, head_width=0, head_length=0, color = 'grey')

def VeeModel():
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

def testProbPlots():
    np.random.seed(0)
    #uniform probability distribution
    x = np.arange(5)
    y = np.ones(5)
    fig1 = plt.figure()
    plt.xticks([])
    plt.yticks([])
    ax1 = fig1.add_subplot(111)
    ax1.set_ylim([-30, 10])
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    plt.rcParams.update({'font.size': 22})
    plt.xlabel('time')
    plt.ylabel('probability of encountering the bug')
    ax1.plot(x, y)
    plt.annotate(
    'uniform distribution bugs\ni.e. random bugs',
    xy=(2, 1), arrowprops=dict(arrowstyle='->'), xytext=(0.2, -12))
    plt.show()

    #increasing probability distribution
    x = np.arange(5)
    y = np.exp(x)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    plt.xticks([])
    plt.yticks([])
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    plt.rcParams.update({'font.size': 22})
    plt.xlabel('time')
    plt.ylabel('probability of encountering the bug')
    ax2.plot(x, y)
    plt.annotate(
    'increasing distribution bugs\ni.e. memory leaks',
    xy=(2.5, 14.3), arrowprops=dict(arrowstyle='->'), xytext=(0.2, 32))
    plt.show()


    #decreasing probability distribution
    x = np.arange(5)
    y = 1 / np.exp(x)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    plt.xticks([])
    plt.yticks([])
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    plt.rcParams.update({'font.size': 22})
    plt.xlabel('time')
    plt.ylabel('probability of encountering the bug')
    ax2.plot(x, y)
    plt.annotate(
    'decreasing distribution bugs\ni.e. startup bugs',
    xy=(1, 0.4), arrowprops=dict(arrowstyle='->'), xytext=(1.5, 0.65))
    plt.show()

    #exponential with fill probability distribution
    x = np.arange(5)
    y = 1 / np.exp(x)
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    plt.xticks([])
    plt.yticks([])
    ax3.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')
    plt.rcParams.update({'font.size': 22})
    plt.xlabel('x')
    plt.ylabel('f(x)')
    ax3.plot(x, y)
    fillx = [2,3,4]
    filly = 1 / np.exp(fillx)
    plt.fill_between(fillx, filly, color = 'black')
    plt.show()

if __name__ == "__main__":
    main()