#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:35:35 2017

@author: linus
"""

#Here are the changes for ph20_week4_problem 1.4


import math as m
import numpy as np
from matplotlib import pyplot as plt 


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
    realsolv = -1. * np.sin(t)
    
    diffsolx = x - realsolx
    diffsolv = v - realsolv
    
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(t,x)
    ax1.plot(t,v)
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, diffsolx)
    ax2.plot(t, diffsolv)
    
    E = np.square(x) + np.square(v)
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, E)
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    
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
    
    print(h)
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, h)
    
    
    
    return
   
    

def impliciteuler(N, x_0, v_0, h):
    # Solves the motion of SHO using the implicit euler method
    
    
    t = np.linspace(0, N * h, N)
    
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x_0
    v[0] = v_0
    
    for i in range(0, N-1):
        v[i + 1] = (-1 * h / (1. - h * h) ) * x[i] + (1. / (1. - h * h) ) * v[i]
        x[i + 1] = (1. / (1. - h * h) ) * x[i] + (h / (1. - h * h) ) * v[i]
     
    realsolx = np.cos(t)
    realsolv = -1. * np.sin(t)
    
    diffsolx = x - realsolx
    diffsolv = v - realsolv
        
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(t,x)
    ax1.plot(t,v)    
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, diffsolx)
    ax2.plot(t, diffsolv)
    
    E = np.square(x) + np.square(v)
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, E)
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    
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
    
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(t,x)
    ax1.plot(t,v)
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, diffsolx)
    ax2.plot(t, diffsolv)
    
    E = np.square(x) + np.square(v)
    diffE = E - (np.square(np.cos(t)) + np.square(np.sin(t)))
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(t, E)
    
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)
    ax5.plot(t, diffE)
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x, v)
    ax4.plot(realsolx, realsolv)
    
    max_error = np.amax(diffsolx)
    

    
    
    return max_error
    
    
    
    
    