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
    #docPlots()
    agilePyramid()
    #scrum()
    #kanban()

    pass

def kanban():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)
    drawkanbanboard(ax)
    pl.text(2.5, 3.8, 'To do',
            horizontalalignment='center', verticalalignment='center')
    pl.text(3.5, 3.8, 'Doing',
            horizontalalignment='center', verticalalignment='center')
    pl.text(4.5, 3.8, 'Done',
            horizontalalignment='center', verticalalignment='center')
    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([1.8,4.2])
    pl.xlim([1.8,5.2])
    pl.show()

def scrum():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)

    drawbacklog(ax)

    # plt.arrow(1.05, 3.05, 0, 0.9, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(1.05, 3.95, 2.9, 0, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(3.95, 3.95, 0, -0.9, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(3.95, 3.05, -2.9, 0, head_width=0, head_length=0, color = 'grey')


    pl.text(2.5, 4, 'Create backlog',
            horizontalalignment='center', verticalalignment='center')
    ax.arrow(2.5, 3.9, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 3.5, 'Sprint planning',
            horizontalalignment='center', verticalalignment='center')
    ax.arrow(2.5, 3.4, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 3, 'Daily scrum',
            horizontalalignment='center', verticalalignment='center')
    ax.arrow(2.5, 2.9, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')

    drawDecision(ax, 2.5, 2.5)
    pl.text(2.4, 2.5, 'Scrum done?\n2-4 weeks',
            horizontalalignment='right', verticalalignment='center')
    pl.text(2.6, 2.6, 'No',
            horizontalalignment='left', verticalalignment='center')
    pl.text(2.55, 2.3, 'Yes',
            horizontalalignment='left', verticalalignment='center')
    ax.arrow(2.5, 2.35, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(2.6, 2.5, 1, 0, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(3.6, 2.5, 0, 0.5, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(3.6, 3, -0.5, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 2, 'Sprint review',
            horizontalalignment='center', verticalalignment='center')
    ax.arrow(2.5, 1.9, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 1.5, 'Shippable code',
            horizontalalignment='center', verticalalignment='center')
    ax.arrow(2.5, 1.4, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')

    drawDecision(ax, 2.5, 1)
    pl.text(2.4, 1, 'Project done?',
            horizontalalignment='right', verticalalignment='center')
    pl.text(2.6, 1.1, 'No',
            horizontalalignment='left', verticalalignment='center')
    ax.arrow(2.5, 0.85, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(2.6, 1, 1.4, 0, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(4, 1, 0, 2.25, head_width=0.05, head_length=0.1, fc='k', ec='k')


    pl.text(2.5, 0.4, 'Yes, throw a party\n(or everybody is fired...)',
            horizontalalignment='center', verticalalignment='center')

    drawDecision(ax, 4, 3.5)
    ax.arrow(3.9, 3.5, -0.6, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(4, 3.65, 0, 0.35, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(4, 4, -0.7, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(4.1, 3.5, 'Did the \nproject\npriorities\nchange?',
            horizontalalignment='left', verticalalignment='center')
    pl.text(3.9, 3.4, 'No',
            horizontalalignment='right', verticalalignment='center')
    pl.text(3.9, 3.9, 'Yes',
            horizontalalignment='right', verticalalignment='center')

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([0,4.2])
    pl.xlim([0,5.2])
    pl.show()

def drawDecision(ax, x, y):
    sz = 0.1
    ax.arrow(x, y-sz, sz/2, sz, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(x+sz/2, y, -sz/2, sz, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(x, y+sz, -sz/2, -sz, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(x-sz/2, y, sz/2, -sz, head_width=0.00, head_length=0.0, fc='k', ec='k')

def drawsprintcard(ax, x,y):
    sz = 0.2
    plt.plot((x, x+sz), (y, y), color = 'grey')
    plt.plot((x, x), (y, y+sz), color = 'grey')
    plt.plot((x, x+sz), (y+sz, y+sz), color = 'grey')
    plt.plot((x+sz, x+sz), (y, y+sz), color = 'grey')
    drawScribble(ax, x + 0.05, y + 0.05, 0.1)
    drawScribble(ax, x + 0.05, y + 0.1 ,0.07)

def drawbacklog(ax):
    plt.plot((0.2, 0.2), (2.2, 4), color = 'black')
    plt.plot((0.2, 1), (2.2, 2.2), color = 'black')
    plt.plot((0.2, 1), (4, 4), color = 'black')
    plt.plot((1, 1), (2.2, 4), color = 'black')
    drawScribble(ax, 0.25, 3.9, 0.6)
    drawScribble(ax, 0.25, 3.8, 0.7)
    drawScribble(ax, 0.25, 3.7, 0.4)
    drawScribble(ax, 0.25, 3.6, 0.3)
    drawScribble(ax, 0.25, 3.5, 0.7)
    drawScribble(ax, 0.25, 3.4, 0.2)
    drawScribble(ax, 0.25, 3.3, 0.7)
    drawScribble(ax, 0.25, 3.2, 0.6)
    drawScribble(ax, 0.25, 3.1, 0.7)
    drawScribble(ax, 0.25, 3.0, 0.4)
    drawScribble(ax, 0.25, 2.9, 0.3)
    drawScribble(ax, 0.25, 2.8, 0.7)
    drawScribble(ax, 0.25, 2.7, 0.2)
    drawScribble(ax, 0.25, 2.6, 0.7)

    drawScribble(ax, 0.25, 3.9, 0.02)
    drawScribble(ax, 0.25, 3.8, 0.02)
    drawScribble(ax, 0.25, 3.7, 0.02)
    drawScribble(ax, 0.25, 3.6, 0.02)
    drawScribble(ax, 0.25, 3.5, 0.02)
    drawScribble(ax, 0.25, 3.4, 0.02)
    drawScribble(ax, 0.25, 3.3, 0.02)
    drawScribble(ax, 0.25, 3.2, 0.02)
    drawScribble(ax, 0.25, 3.1, 0.02)
    drawScribble(ax, 0.25, 3.0, 0.02)
    drawScribble(ax, 0.25, 2.9, 0.02)
    drawScribble(ax, 0.25, 2.8, 0.02)
    drawScribble(ax, 0.25, 2.7, 0.02)
    drawScribble(ax, 0.25, 2.6, 0.02)

def drawkanbanboard(ax):
    plt.plot((2, 2), (3, 4), color = 'black')
    plt.plot((2, 5), (4, 4), color = 'black')
    plt.plot((5, 5), (4, 3), color = 'black')
    plt.plot((5, 2), (3, 3), color = 'black')

    plt.plot((3, 3), (4, 3), color = 'black')
    plt.plot((4, 4), (4, 3), color = 'black')

    drawsprintcard(ax, 2.1, 3.1)
    drawsprintcard(ax, 2.4, 3.1)
    drawsprintcard(ax, 2.1, 3.4)

    drawsprintcard(ax, 3.1, 3.1)
    drawsprintcard(ax, 3.4, 3.4)
    drawsprintcard(ax, 3.7, 3.1)

    drawsprintcard(ax, 4.7, 3.4)

def agilePyramid():
    np.random.seed(0)
    ax = pl.axes([0., 0., 3., 3.], frameon=False, xticks=[],yticks=[])
    ax.set_autoscale_on(False)

    x = np.linspace(0, 0.025, 50)
    ax.plot(x, x, 'black', lw=1)
    x = np.linspace(0.14, 0.45, 50)
    ax.plot(x, x, 'black', lw=1)
    x = np.linspace(0.55, 1, 50)
    ax.plot(x, x, 'black', lw=1)

    x = np.linspace(1, 1.45, 50)
    ax.plot(x, 2 - x, 'black', lw=1)
    x = np.linspace(1.55, 1.89, 50)
    ax.plot(x, 2 - x, 'black', lw=1)

    x = np.linspace(0, 0.65, 50)
    ax.plot(x, np.zeros(50), 'black', lw=1)
    x = np.linspace(1.34, 1.81, 50)
    ax.plot(x, np.zeros(50), 'black', lw=1)

    pl.text(0.5, 0.9, 'Agile\nmanifesto',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    pl.text(0.3, 0.5, 'Scrum',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.7, 0.5, 'Kanban',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    pl.text(0.1, 0.20, 'Continuous\nIntegration',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.1, 0.10, 'Continuous\nDeployment',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    pl.text(0.9, 0.20, 'F/T/B',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.9, 0.15, 'Driven',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.9, 0.10, 'Development',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    pl.text(0.5, 0.2, 'Pair programming',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.5, 0.15, 'Code refactoring',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    pl.text(0.5, 0.1, 'Velocity tracking',
            horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    # pl.text(0.5, 0.5,'matplotlib',
    #  horizontalalignment='center',
    #  verticalalignment='center',
    #  transform = ax.transAxes)

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([-0.2,1.2])
    pl.xlim([-0.2,2.2])
    pl.show()
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