#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:35:35 2017

@author: linus
"""

import math as m
import numpy as np
from matplotlib import pyplot as plt 
from sys import argv

N1 = int(argv[1])
x1_0 = float(argv[2])
v1_0 = float(argv[3])
h1 = float(argv[4])

def expliciteuler(N, x_0, v_0, h):
    # Calculates the motion of a simple harmonic oscillator using 
    # the explicit euler method
    
    t = np.linspace(0, N * h, N)
    
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x_0
    v[0] = v_0
    
    for i in range(0, N-1):
        x[i + 1] = x[i] + h * v[i]
        v[i + 1] = v[i] - h * x[i]
    
    
    realsolx = np.cos(t)
    diffsolx = x - realsolx
    max_error = np.amax(diffsolx)
    
    
    return max_error



def expliciteulerplotter(N, x_0, v_0, h):
    # Calculates the motion of a simple harmonic oscillator using 
    # the explicit euler method and plots 
    
    

    t = np.linspace(0, N * h, N)
    
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x_0
    v[0] = v_0
    
    for i in range(0, N-1):
        x[i + 1] = x[i] + h * v[i]
        v[i + 1] = v[i] - h * x[i]
        
        
    realsolx = np.cos(t)
    realsolv = -1. * np.sin(t)
    
    diffsolx = x - realsolx
    diffsolv = v - realsolv
    
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(t,x)
    ax1.plot(t,v)
    plt.xlabel("time") 
    plt.ylabel("position, velocity")
    fig1.savefig('p1.png')
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, diffsolx)
    ax2.plot(t, diffsolv)
    plt.xlabel("time") 
    plt.ylabel("error")
    fig2.savefig('p2.png')
    
    E = np.square(x) + np.square(v)
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, E)
    plt.xlabel("time") 
    plt.ylabel("energy")
    fig3.savefig('p3.png')
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    plt.xlabel("position") 
    plt.ylabel("velocity")
    
    max_error = np.amax(diffsolx)
    
    
    return max_error



def hprop():
    # Creates a plot of the error behavior depending on h
    
    h_1 = expliciteuler(3000, 1, 0, 1e-6)
    h_2 = expliciteuler(3000, 1, 0, 0.5 * 1e-6)
    h_3 = expliciteuler(3000, 1, 0, 0.25 * 1e-6)
    h_4 = expliciteuler(3000, 1, 0, 0.125 * 1e-6)
    h_5 = expliciteuler(3000, 1, 0, 0.0625 * 1e-6)
    
    t = [1e-6, 0.5 * 1e-6, 0.25 * 1e-6, 0.125 * 1e-6, 0.0625 * 1e-6]
    h = [h_1, h_2, h_3, h_4, h_5]

    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, h)
    plt.xlabel("time") 
    plt.ylabel("error")
    
    
    
    return
   
    

def impliciteuler(N, x_0, v_0, h):
    # Solves the motion of SHO using the implicit euler method
    
    
    t = np.linspace(0, N * h, N)
    
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x_0
    v[0] = v_0
    
    for i in range(0, N-1):
        v[i + 1] = (-1 * h / (1. + h * h) ) * x[i] + (1. / (1. + h * h) ) * v[i]
        x[i + 1] = (1. / (1. + h * h) ) * x[i] + (h / (1. + h * h) ) * v[i]
     
    realsolx = np.cos(t)
    realsolv = -1. * np.sin(t)
    
    diffsolx = x - realsolx
    diffsolv = v - realsolv
        
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(t,x)
    ax1.plot(t,v) 
    plt.xlabel("time") 
    plt.ylabel("position, velocity")
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, diffsolx)
    ax2.plot(t, diffsolv)
    plt.xlabel("time") 
    plt.ylabel("error")
    
    E = np.square(x) + np.square(v)
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, E)
    plt.xlabel("time") 
    plt.ylabel("energy")
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    plt.xlabel("position") 
    plt.ylabel("velocity")
    
    return
    
    
def symplecticteuler(N, x_0, v_0, h):
    # Calculates the motion of a simple harmonic oscillator using 
    # the symplectic euler method
    
    

    t = np.linspace(0, N * h, N)
    
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x_0
    v[0] = v_0
    
    for i in range(0, N-1):
        x[i + 1] = x[i] + h * v[i]
        v[i + 1] = v[i] - h * x[i + 1]
        
        
    realsolx = np.cos(t)
    realsolv = -1. * np.sin(t)
    
    diffsolx = x - realsolx
    diffsolv = v - realsolv
    

    
    E = np.square(x) + np.square(v)
    diffE = E - (np.square(np.cos(t)) + np.square(np.sin(t)))
    
   
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)
    ax5.plot(t, diffE)
    plt.xlabel("time") 
    plt.ylabel("energy error")
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    plt.xlabel("position") 
    plt.ylabel("velocity")
    
    max_error = np.amax(diffsolx)
    

    
    
    return max_error
    
    
    
    
def assignment4(N, x_0, v_0, h):
    # Generates all necessary plots for assignment 4 part 2
    
    
    expliciteulerplotter(N, x_0, v_0, h)
    hprop()
    impliciteuler(N, x_0, v_0, h)
    symplecticteuler(N, x_0, v_0, h)
    
    return
    
    
    
assignment4(N1, x1_0, v1_0, h1)
    
    
    
    
    
    
    
    
    
    
    
    