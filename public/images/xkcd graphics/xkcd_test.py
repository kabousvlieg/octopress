#!usr/bin/env python
__author__ = 'Huis'
import numpy as np
import random
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
import matplotlib
from xkcdify import XKCDify
from xkcdify import xkcd_line
import math
from matplotlib.patches import Ellipse
from matplotlib.patches import Arc

def main():
    #VeeModel()
    #testProbPlots()
    #docPlots()
    #agilePyramid()
    #scrum()
    #kanban()
    #agileWaterfallSpectrum()
    #agileSetup()
    #testPyramid()
    agileWaterfallTeamActivities()
    #alternativeEskom()
    pass


def alternativeEskom():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)

    #Battery
    ax.plot((1, 2), (1, 1), color = 'black')
    ax.plot((1, 2), (1.5, 1.5), color = 'black')
    ax.plot((1, 1), (1, 1.5), color = 'black')
    ax.plot((2, 2), (1, 1.5), color = 'black')

    ax.plot((1.9, 1.9), (1.5, 1.6), color = 'black')
    ax.plot((1.7, 1.7), (1.5, 1.6), color = 'black')
    ax.plot((1.7, 1.9), (1.6, 1.6), color = 'black')

    ax.plot((1.1, 1.1), (1.5, 1.6), color = 'black')
    ax.plot((1.3, 1.3), (1.5, 1.6), color = 'black')
    ax.plot((1.1, 1.3), (1.6, 1.6), color = 'black')

    #Display
    ax.plot((1, 3), (3, 3), color = 'black')
    ax.plot((1, 3), (4, 4), color = 'black')
    ax.plot((1, 1), (3, 4), color = 'black')
    ax.plot((3, 3), (3, 4), color = 'black')
    ax.plot((1.1, 2.9), (3.3, 3.3), color = 'black')
    ax.plot((1.1, 2.9), (3.9, 3.9), color = 'black')
    ax.plot((1.1, 1.1), (3.3, 3.9), color = 'black')
    ax.plot((2.9, 2.9), (3.3, 3.9), color = 'black')

    #DB Board
    ax.plot((5, 7), (3, 3), color = 'black')
    ax.plot((5, 7), (4, 4), color = 'black')
    ax.plot((5, 5), (3, 3.8), color = 'black')
    ax.plot((7, 7), (3, 4), color = 'black')
    ax.plot((5, 4.7), (4, 3.8), color = 'black')
    ax.plot((4.7, 6.7), (3.8, 3.8), color = 'black')
    ax.plot((7, 6.7), (4, 3.8), color = 'black')
    #Switches
    ax.plot((5.2, 6.8), (3.3, 3.3), color = 'black')
    ax.plot((5.2, 6.8), (3.7, 3.7), color = 'black')
    ax.plot((5.2, 5.2), (3.3, 3.7), color = 'black')
    ax.plot((6.8, 6.8), (3.3, 3.7), color = 'black')

    #Inverter
    ax.plot((3, 4.5), (1, 1), color = 'black')
    ax.plot((3, 4.5), (1.1, 1.1), color = 'black')
    ax.plot((3, 4.5), (1.2, 1.2), color = 'black')
    ax.plot((3, 4.5), (1.3, 1.3), color = 'black')
    ax.plot((3, 4.5), (1.4, 1.4), color = 'black')
    ax.plot((3, 4.5), (1.5, 1.5), color = 'black')
    # ax.plot((3, 4.5), (1.5, 1.5), color = 'black')
    ax.plot((3, 3), (1, 1.5), color = 'black')
    ax.plot((4.5, 4.5), (1, 1.5), color = 'black')
    el = Arc(xy=(3.75, 1.5), width=1.5, height=0.3, angle=0, fc='None', lw=2, theta1 = 0, theta2 = 180)
    ax.add_patch(el)

    # pl.text(1, 4.15, 'Waterfall',
    #         horizontalalignment='center', verticalalignment='center')

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([-0.2,4.25])
    pl.xlim([-0.2,8.2])
    pl.show()

def agileWaterfallTeamActivities():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)

    ax.plot((4, 4), (0, 4), color = 'black')

    pl.text(1, 4.15, 'Waterfall',
            horizontalalignment='center', verticalalignment='center')
    ax.plot((0.4, 1.60), (4.05, 4.05), color = 'black')
    pl.text(7, 4.15, 'Agile',
            horizontalalignment='center', verticalalignment='center')
    ax.plot((6.7, 7.3), (4.05, 4.05), color = 'black')

    ax.plot((-0.1, -0.1), (3.9, 0), color = 'black')

    pl.text(0.1, 3.9, 'Requirements gathering',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0.1, 3.7, 'Write specification (SRD)',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0.1, 3.5, '(Client approves SRD?)',
            horizontalalignment='left', verticalalignment='center', color = "blue")
    ax.plot((-0.1, 0), (3.9, 3.9), color = 'black')
    ax.plot((-0.1, 0), (3.7, 3.7), color = 'black')
    ax.plot((-0.1, 0), (3.5, 3.5), color = 'black')
    ax.arrow(-0.1, 3.5, 0.08, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(0, 3.20, 'Write PSAC and SDP',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 3.0, '(CA approves PSAC and SDP?)',
            horizontalalignment='left', verticalalignment='center', color = "blue")
    pl.text(0, 2.7, 'Write Low level requirements',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 2.5, 'Write Design documentation',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 2.3, '(Client approves design?)',
            horizontalalignment='left', verticalalignment='center', color = "blue")
    pl.text(0, 2.1, 'Write Code',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 2.2, 'Write SVCP',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 2.0, '(Development done?)',
            horizontalalignment='left', verticalalignment='center', color = "blue")
    pl.text(0, 1.85, 'Testing / Write SVR',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 1.7, 'Code reviews',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 1.5, '(Product fulfills mission?)',
            horizontalalignment='left', verticalalignment='center', color = "blue")
    pl.text(0, 1.35, 'Write SAS, SCMR and SQA',
            horizontalalignment='left', verticalalignment='center')
    pl.text(0, 1.15, '(DO-178 Certification)',
            horizontalalignment='left', verticalalignment='center', color = "blue")

    pl.text(4.1, 3.9, 'Requirements gathering',
            horizontalalignment='left', verticalalignment='center')

    # pl.text(0.5, 0.5,'matplotlib',
    #  horizontalalignment='center',
    #  verticalalignment='center',
    #  transform = ax.transAxes)

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([-0.2,4.25])
    pl.xlim([-0.2,8.2])
    pl.show()

def testPyramid():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)

    ax.plot((0.0, 2), (0, 1), color = 'black')
    ax.plot((2, 4), (1, 0), color = 'black')
    ax.plot((0, 4), (0, 0), color = 'black')

    ax.plot((1.2, 2.8), (0.6, 0.6), color = 'black')
    ax.plot((0.6, 3.4), (0.3, 0.3), color = 'black')
    pl.text(2, 0.7, 'Manual tests',
            horizontalalignment='center', verticalalignment='center')
    pl.text(2, 0.45, 'Automated functional tests',
            horizontalalignment='center', verticalalignment='center')
    pl.text(2, 0.15, 'Unit tests',
            horizontalalignment='center', verticalalignment='center')

    # pl.text(0.5, 0.5,'matplotlib',
    #  horizontalalignment='center',
    #  verticalalignment='center',
    #  transform = ax.transAxes)

    XKCDify(ax, xaxis_loc=-1, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([-0.2,1.2])
    pl.xlim([-0.2,4.2])
    pl.show()

def agileSetup():
    np.random.seed(0)
    ax = pl.axes()
    ax.set_autoscale_on(False)
    drawLaptop(ax, 1, 2, 1.5)
    drawCircuit(ax, -1.5, 2, 1.5)
    drawLaptop(ax, 1, 6, 1.5)
    drawCircuit(ax, -1.5, 6, 1.5)
    drawLaptop(ax, 1, 10, 1.5)
    drawCircuit(ax, -1.5, 10, 1.5)
    drawLaptop(ax, 1, 14, 1.5)
    drawCircuit(ax, -1.5, 14, 1.5)
    drawDatabase(ax, 9, 16, 1.5)
    drawOscilloscope(ax, 13, 12, 1.5)
    drawCircuit(ax, 13, 9, 1.5)
    drawPC(ax, 8.25, 11, 1.5)
    drawDiamond(7.8, 7, 1.2)
    drawMultiDoc(ax, 8, 1, 3)
    plt.plot((0.2, 1.8), (3, 3), color = 'grey')
    plt.plot((0.2, 1.8), (7, 7), color = 'grey')
    plt.plot((0.2, 1.8), (11, 11), color = 'grey')
    plt.plot((0.2, 1.8), (15, 15), color = 'grey')
    plt.plot((6, 6), (3, 15), color = 'black')
    plt.plot((4, 8), (15, 15), color = 'black')
    plt.plot((4, 6), (11, 11), color = 'black')
    plt.plot((4, 6), (7, 7), color = 'black')
    plt.plot((4, 6), (3, 3), color = 'black')
    plt.plot((9, 9), (13.8, 12.8), color = 'black')
    plt.plot((9, 9), (9.5, 8.5), color = 'black')
    plt.plot((10, 11.5), (11, 11), color = 'black')
    plt.plot((11.5, 12.8), (12.7, 12.7), color = 'black')
    plt.plot((11.5, 12.8), (9.7, 9.7), color = 'black')
    plt.plot((11.5, 11.5), (9.7, 12.7), color = 'black')
    plt.plot((9, 9), (5.6, 4.8), color = 'black')
    plt.plot((13.7, 13.7), (11.7, 10.7), color = 'grey')
    pl.text(1, 18, 'Developers',
            horizontalalignment='center', verticalalignment='center')
    pl.text(9, 18, 'Version\ncontrol',
            horizontalalignment='center', verticalalignment='center')
    pl.text(13.5, 15, 'Automated\ntest bench\n(CD)',
            horizontalalignment='center', verticalalignment='center')
    pl.text(13.7, 7.5, 'Device\nunder\ntest',
            horizontalalignment='center', verticalalignment='center')
    pl.text(7.5, 11, 'Unit\ntests\n(CI)',
            horizontalalignment='center', verticalalignment='center')
    pl.text(9, 6.9, 'Tests\npass?',
            horizontalalignment='center', verticalalignment='center')
    pl.text(10.3, 3, 'Auto generate:\n'
                    '- Source code\n'
                    '- Object code\n'
                    '- SCMR\n'
                    '- SVP\n'
                    '- SVR',
            horizontalalignment='left', verticalalignment='center')
    XKCDify(ax, xaxis_loc=-5, yaxis_loc=-5,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([0., 20.])
    pl.xlim([-2., 15.])
    pl.show()


def drawMultiDoc(ax, x, y, sz):
    rng = np.linspace(0, sz/1.9, 100)
    fixed = np.zeros(100)
    ax.plot(rng+x, fixed + y, c='gray')
    ax.plot(rng+x, fixed + y + sz, c='gray')
    ax.plot(rng+x + 0.1*sz, fixed + y + sz*1.1, c='gray')
    ax.plot(rng+x + 0.2*sz, fixed + y + sz*1.2, c='gray')
    rng = np.linspace(0, sz, 100)
    ax.plot(fixed + x, rng + y, c='gray')
    ax.plot(fixed + x + sz/1.9, rng + y, c='gray')
    ax.plot(fixed + x + sz/1.9 + sz*0.1, rng + y + sz*0.1, c='gray')
    ax.plot(fixed + x + sz/1.9 + sz*0.2, rng + y + sz*0.2, c='gray')
    rng = np.linspace(0, sz*0.1, 100)
    ax.plot(rng+x + sz/1.9, fixed + y + sz*0.1, c='gray')
    ax.plot(rng+x + sz/1.9 + sz*0.1, fixed + y + sz*0.2, c='gray')
    ax.plot(fixed + x + sz*0.1, rng + y + sz, c='gray')
    ax.plot(fixed + x + sz*0.2, rng + y + sz*1.1, c='gray')


def drawCircuit(ax, x, y, sz):
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    #Housing
    ax.plot(rng+x, fixed + y, c='gray')
    ax.plot(rng+x, fixed + y + sz, c='gray')
    ax.plot(fixed + x, rng + y, c='gray')
    ax.plot(fixed + x + sz, rng + y, c='gray')
    #Circuit
    plt.plot((x + sz/6, x + sz *4/6), (y + sz*2/6, y + sz*2/6), color = 'gray')
    plt.plot((x + sz*4/6, x + sz*4/6), (y + sz*4/6, y + sz*1.2/6), color = 'gray')
    #CAP
    plt.plot((x + sz*1/6, x + sz*1/6), (y + sz*2.8/6, y + sz*2/6), color = 'gray')
    plt.plot((x + sz*1/6, x + sz*1/6), (y + sz*4/6, y + sz*3.2/6), color = 'gray')
    plt.plot((x + sz*0.6/6, x + sz*1.4/6), (y + sz*3.2/6, y + sz*3.2/6), color = 'gray')
    plt.plot((x + sz*0.6/6, x + sz*1.4/6), (y + sz*2.8/6, y + sz*2.8/6), color = 'gray')
    #RESISTOR
    plt.plot((x + sz*1/6, x + sz *1.5/6), (y + sz*4/6, y + sz*4/6), color = 'gray')
    plt.plot((x + sz*3.45/6, x + sz *4/6), (y + sz*4/6, y + sz*4/6), color = 'gray')

    plt.plot((x + sz*9/36, x + sz *10/36), (y + sz*4./6, y + sz*4.6/6), color = 'gray')
    plt.plot((x + sz*10/36, x + sz *12/36), (y + sz*4.6/6, y + sz*3.4/6), color = 'gray')
    plt.plot((x + sz*12/36, x + sz *14/36), (y + sz*3.4/6, y + sz*4.6/6), color = 'gray')
    plt.plot((x + sz*14/36, x + sz *16/36), (y + sz*4.6/6, y + sz*3.4/6), color = 'gray')
    plt.plot((x + sz*16/36, x + sz *18/36), (y + sz*3.4/6, y + sz*4.6/6), color = 'gray')
    plt.plot((x + sz*18/36, x + sz *19/36), (y + sz*4.6/6, y + sz*4./6), color = 'gray')
    #GND
    plt.plot((x + sz*3.5/6, x + sz *4.5/6), (y + sz*1.2/6, y + sz*1.2/6), color = 'gray')
    plt.plot((x + sz*3.8/6, x + sz *4.2/6), (y + sz*0.8/6, y + sz*0.8/6), color = 'gray')
    plt.plot((x + sz*3.95/6, x + sz *4.05/6), (y + sz*0.5/6, y + sz*0.5/6), color = 'gray')



def drawOscilloscope(ax, x, y, sz):
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    #Housing
    ax.plot(rng+x, fixed + y, c='gray')
    ax.plot(rng+x, fixed + y + sz, c='gray')
    ax.plot(fixed + x, rng + y, c='gray')
    ax.plot(fixed + x + sz, rng + y, c='gray')
    #Screen
    rng = np.linspace(0, sz/2, 100)
    fixed = np.zeros(100)
    ax.plot(rng + x + 0.15, fixed + y + 0.2, c='gray')
    ax.plot(rng + x + 0.15, fixed + y + sz - 0.2, c='gray')
    rng = np.linspace(0, sz - 0.4, 100)
    ax.plot(fixed + x + 0.15, rng + y + 0.2, c='gray')
    ax.plot(fixed + x + 0.15 + sz/2, rng + y + 0.2, c='gray')
    #Signal
    rng = np.linspace(0, sz/2, 100)
    ysig = np.sin(rng*16)/2
    ax.plot(rng + x + 0.15, ysig + y + 0.75, c='gray')
    #Knobs
    el = Ellipse(xy=(x + sz*5/6,y + sz*5/6), width=sz/6, height=sz/6, angle=0, edgecolor='gray', fc='None', lw=2)
    ax.add_patch(el)
    el = Ellipse(xy=(x + sz*5/6,y + sz*3/6), width=sz/6, height=sz/6, angle=0, edgecolor='gray', fc='None', lw=2)
    ax.add_patch(el)
    el = Ellipse(xy=(x + sz*5/6,y + sz*1/6), width=sz/6, height=sz/6, angle=0, edgecolor='gray', fc='None', lw=2)
    ax.add_patch(el)

def drawDatabase(ax, x, y, sz):
    el = Ellipse(xy=(x,y), width=sz, height=sz/2, angle=0, edgecolor='gray', fc='None', lw=2)
    ax.add_patch(el)
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    ax.plot(fixed + x + sz / 2, rng + y - sz, c='gray')
    ax.plot(fixed + x - sz / 2, rng + y - sz, c='gray')
    el = Arc(xy=(x,y-sz), width=sz, height=sz/2, angle=0, edgecolor='gray', fc='None', lw=2, theta1 = 180, theta2 = 0)
    ax.add_patch(el)
    el = Arc(xy=(x,y-(sz/3)), width=sz, height=sz/2, angle=0, edgecolor='gray', fc='None', lw=2, theta1 = 180, theta2 = 0)
    ax.add_patch(el)
    el = Arc(xy=(x,y-(2*sz/3)), width=sz, height=sz/2, angle=0, edgecolor='gray', fc='None', lw=2, theta1 = 180, theta2 = 0)
    ax.add_patch(el)


def drawLaptop(ax, x, y, sz):
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    #screen
    ax.plot(rng+x+sz, fixed + 1.5*sz + y, c='gray')
    ax.plot(rng+x+sz*2/3, fixed + sz/2 + y, c='gray')
    ax.plot(rng+x, fixed + y, c='gray')
    ax.plot(rng+x + sz*1.3/6, fixed + y + sz*1/6, c='gray')
    ax.plot(rng+x + sz*2.6/6, fixed + y + sz*2/6, c='gray')
    xl = np.linspace(0, sz/3, 100)
    yl = rng
    ax.plot(xl + x + sz*2/3, yl + y + sz/2, c='gray')
    ax.plot(xl + x + 1.66*sz, yl + y + sz/2, c='gray')
    xl = np.linspace(0, sz/1.5, 100)
    yl = rng/2
    ax.plot(xl + x, yl + y, c='gray')
    ax.plot(xl + x + sz, yl + y, c='gray')
    ax.plot(xl + x + sz*1/6, yl + y, c='gray')
    ax.plot(xl + x + sz*2/6, yl + y, c='gray')
    ax.plot(xl + x + sz*3/6, yl + y, c='gray')
    ax.plot(xl + x + sz*4/6, yl + y, c='gray')
    ax.plot(xl + x + sz*5/6, yl + y, c='gray')

def drawPC(ax, x, y, sz):
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    #screen
    ax.plot(rng+x, fixed + y, c='gray')
    ax.plot(rng+x, fixed + sz + y, c='gray')
    ax.plot(fixed + x, rng + y, c='gray')
    ax.plot(fixed + x + sz, rng + y, c='gray')

    rng = np.linspace(0, sz - 0.2, 100)
    fixed = np.zeros(100)
    ax.plot(rng + x + 0.1, fixed + y + 0.1, c='gray')
    ax.plot(rng + x + 0.1, fixed + sz + y - 0.1, c='gray')
    ax.plot(fixed + x + 0.1, rng + y + 0.1, c='gray')
    ax.plot(fixed + x + sz - 0.1, rng + y + 0.1, c='gray')

    #keyboard
    rng = np.linspace(0, sz, 100)
    fixed = np.zeros(100)
    ax.plot(rng+x, fixed - (sz * 0.8) + (sz / 2) + y, c='gray')
    ax.plot(rng+x, fixed - (sz * 0.8) + y, c='gray')

    ax.plot(rng+x, fixed - (sz * 0.8) + (2*sz / 6) + y, c='gray')
    ax.plot(rng+x, fixed - (sz * 0.8) + (1*sz / 6) + y, c='gray')

    rng_h = np.linspace(0, sz / 2, 100)
    ax.plot(fixed + x, rng_h - (sz * 0.8) + y, c='gray')
    ax.plot(fixed + x + sz, rng_h - (sz * 0.8) + y, c='gray')

    ax.plot(fixed + x + (sz / 6), rng_h - (sz * 0.8) + y, c='gray')
    ax.plot(fixed + x + (2*sz / 6), rng_h - (sz * 0.8) + y, c='gray')
    ax.plot(fixed + x + (3*sz / 6), rng_h - (sz * 0.8) + y, c='gray')
    ax.plot(fixed + x + (4*sz / 6), rng_h - (sz * 0.8) + y, c='gray')
    ax.plot(fixed + x + (5*sz / 6), rng_h - (sz * 0.8) + y, c='gray')

# Some helper functions
def norm(x, x0, sigma):
    return np.exp(-0.5 * (x - x0) ** 2 / sigma ** 2)

def sigmoid(x, x0, alpha):
    return 1. / (1. + np.exp(- (x - x0) / alpha))

def agileWaterfallSpectrum():
    # define the curves
    x = np.linspace(0, 1, 100)
    y = np.sqrt(100 - pow(x - 0.5, 2)) - 9.3

    # draw the curves
    ax = pl.axes()
    ax.plot(x, y, c='gray')

    ax.text(-0.07, 0.72, "waterfall")
    #ax.plot([0.15, 0.2], [1.0, 0.2], '-k', lw=0.5)

    ax.text(0.95, 0.72, "agile")

    ax.text(0.50, 0.25, "a happy middle ground?")
    ax.plot([0.50, 0.75], [0.68, 0.35], '-k', lw=0.5)

    ax.text(0.50, 0.8, "Development spectrum", horizontalalignment='center')

    # modify all the axes elements in-place
    XKCDify(ax, expand_axes=True,
            xaxis_loc=-10, yaxis_loc=-10)
    pl.ylim([-0.2,1.2])
    pl.xlim([-0.2,1.2])
    pl.show()


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

    drawbacklog(ax, -1, -2)
    drawArch(ax, -1, 0)

    ax.arrow(0.6, 3.5, 1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
    pl.text(1.2, 3.7, 'Review\n'
                      'architecture',
            horizontalalignment='center', verticalalignment='center')

    ax.arrow(1.7, 2, -1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
    pl.text(1.2, 2.2, 'Update\n'
                      'architecture',
            horizontalalignment='center', verticalalignment='center')

    pl.text(1.2, 1.8, 'Update\n'
                      'requirements',
            horizontalalignment='center', verticalalignment='center')

    # plt.arrow(1.05, 3.05, 0, 0.9, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(1.05, 3.95, 2.9, 0, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(3.95, 3.95, 0, -0.9, head_width=0, head_length=0, color = 'grey')
    # plt.arrow(3.95, 3.05, -2.9, 0, head_width=0, head_length=0, color = 'grey')


    pl.text(2.5, 4, 'Create backlog',
            horizontalalignment='center', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 3.9, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 3.5, 'Sprint planning',
            horizontalalignment='center', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 3.4, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 3, 'Daily scrum',
            horizontalalignment='center', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 2.9, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')

    drawDecision(ax, 2.5, 2.5)
    pl.text(2.4, 2.5, 'Sprint done?\n2-4 weeks',
            horizontalalignment='right', verticalalignment='center',
            color="grey")
    pl.text(2.6, 2.6, 'No',
            horizontalalignment='left', verticalalignment='center',
            color="grey")
    pl.text(2.55, 2.3, 'Yes',
            horizontalalignment='left', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 2.35, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(2.6, 2.5, 1, 0, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(3.6, 2.5, 0, 0.5, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(3.6, 3, -0.45, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 2, 'Sprint review',
            horizontalalignment='center', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 1.9, 0, -0.2, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(2.5, 1.5, 'Shippable code',
            horizontalalignment='center', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 1.4, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')

    drawDecision(ax, 2.5, 1)
    pl.text(2.4, 1, 'Project done?',
            horizontalalignment='right', verticalalignment='center',
            color="grey")
    pl.text(2.6, 1.1, 'No',
            horizontalalignment='left', verticalalignment='center',
            color="grey")
    ax.arrow(2.5, 0.85, 0, -0.15, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(2.6, 1, 1.4, 0, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(4, 1, 0, 2.25, head_width=0.05, head_length=0.1, fc='k', ec='k')


    pl.text(2.5, 0.4, 'Yes, throw a party\n(time for certification...)',
            horizontalalignment='center', verticalalignment='center',
            color="grey")

    drawDecision(ax, 4, 3.5)
    ax.arrow(3.9, 3.5, -0.55, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(4, 3.65, 0, 0.35, head_width=0.00, head_length=0.0, fc='k', ec='k')
    ax.arrow(4, 4, -0.65, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

    pl.text(4.1, 3.5, 'Did the \nproject\npriorities\nchange?',
            horizontalalignment='left', verticalalignment='center',
            color="grey")
    pl.text(3.9, 3.4, 'No',
            horizontalalignment='right', verticalalignment='center',
            color="grey")
    pl.text(3.9, 3.9, 'Yes',
            horizontalalignment='right', verticalalignment='center',
            color="grey")

    XKCDify(ax, xaxis_loc=-2, yaxis_loc=-1,
        xaxis_arrow='', yaxis_arrow='',
        expand_axes=True)
    pl.ylim([0,4.2])
    pl.xlim([-1,5.0])
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
    drawScribble(ax, x + 0.05, y + 0.1, 0.07)

def drawbacklog(ax, x = 0, y = 0):
    plt.plot((x + 0.2, x + 0.2), (y + 2.2, y + 4), color = 'black')
    plt.plot((x + 0.2, x + 1.45), (y + 2.2, y + 2.2), color = 'black')
    plt.plot((x + 0.2, x + 1.45), (y + 4, y + 4), color = 'black')
    plt.plot((x + 1.45, x + 1.45), (y + 2.2, y + 4), color = 'black')
    plt.annotate('Requirements', xy=(x + 0.25, y + 3.85))
    plt.plot((x + 0.25, x + 1.4), (y + 3.75, y + 3.75), color = 'black')
    # drawScribble(ax, x + 0.25, y + 3.9, 0.6)
    # drawScribble(ax, x + 0.25, y + 3.8, 0.7)
    # drawScribble(ax, x + 0.25, y + 3.7, 0.4)
    drawScribble(ax, x + 0.35, y + 3.6, 0.3)
    drawScribble(ax, x + 0.35, y + 3.5, 0.6)
    drawScribble(ax, x + 0.35, y + 3.4, 0.2)
    drawScribble(ax, x + 0.35, y + 3.3, 0.4)
    drawScribble(ax, x + 0.35, y + 3.2, 0.6)
    drawScribble(ax, x + 0.35, y + 3.1, 0.6)
    drawScribble(ax, x + 0.35, y + 3.0, 0.4)
    drawScribble(ax, x + 0.35, y + 2.9, 0.3)
    drawScribble(ax, x + 0.35, y + 2.8, 0.6)
    drawScribble(ax, x + 0.35, y + 2.7, 0.2)
    drawScribble(ax, x + 0.35, y + 2.6, 0.6)

    # drawScribble(ax, x + 0.25, y + 3.9, 0.02)
    # drawScribble(ax, x + 0.25, y + 3.8, 0.02)
    # drawScribble(ax, x + 0.25, y + 3.7, 0.02)
    drawScribble(ax, x + 0.25, y + 3.6, 0.02)
    drawScribble(ax, x + 0.25, y + 3.5, 0.02)
    drawScribble(ax, x + 0.25, y + 3.4, 0.02)
    drawScribble(ax, x + 0.25, y + 3.3, 0.02)
    drawScribble(ax, x + 0.25, y + 3.2, 0.02)
    drawScribble(ax, x + 0.25, y + 3.1, 0.02)
    drawScribble(ax, x + 0.25, y + 3.0, 0.02)
    drawScribble(ax, x + 0.25, y + 2.9, 0.02)
    drawScribble(ax, x + 0.25, y + 2.8, 0.02)
    drawScribble(ax, x + 0.25, y + 2.7, 0.02)
    drawScribble(ax, x + 0.25, y + 2.6, 0.02)


def drawArch(ax, x = 0, y = 0):
    plt.plot((x + 0.2, x + 0.2), (y + 2.2, y + 4), color = 'black')
    plt.plot((x + 0.2, x + 1.45), (y + 2.2, y + 2.2), color = 'black')
    plt.plot((x + 0.2, x + 1.45), (y + 4, y + 4), color = 'black')
    plt.plot((x + 1.45, x + 1.45), (y + 2.2, y + 4), color = 'black')
    plt.annotate('Architecture', xy=(x + 0.25, y + 3.85))
    plt.plot((x + 0.25, x + 1.4), (y + 3.75, y + 3.75), color = 'black')
    drawDiamond(x + 0.3, y + 2.7, 0.2)
    drawDiamond(x + 0.9, y + 3.2, 0.2)
    drawBox(x + 0.9, y + 2.3, 0.2)
    plt.arrow(x + 0.5, y + 3.5, 0, -0.55, head_width=0.05, head_length=0.05, color = 'grey')
    plt.arrow(x + 0.7, y + 2.705, 0.4, -0, head_width=0.00, head_length=0.00, color = 'grey')
    plt.arrow(x + 0.5, y + 3.2, 0.35, -0, head_width=0.05, head_length=0.05, color = 'grey')
    plt.arrow(x + 1.1, y + 3.0, 0, -0.45, head_width=0.05, head_length=0.05, color = 'grey')


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


def drawScribble(ax, xpos, ypos, len, rnd=0.01):
    np.random.seed(0)
    y = []
    x = np.linspace(0 + xpos, len + xpos, 50)
    for n in x:
        y.append(ypos + random.uniform(0, rnd))
    ax.plot(x, y, 'grey', lw=1)


def drawDoc(xoffset, yoffset, sz = 0.3):
    a4width = sz
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

def drawDiamond(xoffset, yoffset, sz = 0.5):
    plt.arrow(xoffset, yoffset, sz, sz, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + sz, yoffset + sz, sz, -sz, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 2*sz, yoffset, -sz, -sz, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + sz, yoffset - sz, -sz, sz, head_width=0, head_length=0, color = 'grey')

def drawBox(xoffset, yoffset, sz = 0.05):
    plt.arrow(xoffset, yoffset, 0, sz, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset, yoffset + sz, 2*sz, 0, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 2*sz, yoffset + sz, 0, -sz, head_width=0, head_length=0, color = 'grey')
    plt.arrow(xoffset + 2*sz, yoffset, -2*sz, 0, head_width=0, head_length=0, color = 'grey')

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