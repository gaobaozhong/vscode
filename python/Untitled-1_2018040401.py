import matplotlib.pyplot as plt

from matplotlib import animation

import numpy as np

import math

from scipy import optimize


def xin():
    t = np.linspace(0, math.pi * 2, 1000)
    x = np.cos(5 * t)
    y = np.sin(3 * t)
    plt.plot(x, y, color='blue', linewidth=2, label='func')
    plt.xlabel('t')
    plt.ylabel('h')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1, 1)
    plt.legend()
    plt.show()
    return


# xin()


def fangcheng():
    x = np.arange(-100.1, 100.1, .01)
    y = np.arange(-100.1, 100.1, .01)
    x, y = np.meshgrid(x, y)

    # f = np.abs(x)*x + np.abs(y)*y - 1
    # f = 4*x*x+13/2*y*y+10*x*y-2*x-2*y
    f = x * x + y * y
    plt.figure()
    plt.contour(
        x,
        y,
        f,
        0,
    )
    plt.title(r'$\left|x\right|+\left|y\right|=1$')
    plt.show()
    return


# fangcheng()


#直线方程函数
def f_1(x, A, B):
    return A * x + B


#二次曲线方程
def f_2(x, A, B, C):
    return A * x * x + B * x + C


#三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D


def plot_test():

    plt.figure()

    #拟合点
    x0 = [1, 2, 3, 4, 5]
    y0 = [1, 3, 8, 18, 36]

    #绘制散点
    plt.scatter(x0[:], y0[:], 25, "red")

    #直线拟合与绘制
    A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
    x1 = np.arange(0, 6, 0.01)
    y1 = A1 * x1 + B1
    plt.plot(x1, y1, "blue")

    #二次曲线拟合与绘制
    A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]
    x2 = np.arange(0, 6, 0.01)
    y2 = A2 * x2 * x2 + B2 * x2 + C2
    plt.plot(x2, y2, "green")

    #三次曲线拟合与绘制
    A3, B3, C3, D3 = optimize.curve_fit(f_3, x0, y0)[0]
    x3 = np.arange(0, 6, 0.01)
    y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3
    plt.plot(x3, y3, "purple")

    plt.title("test")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

    return

plot_test()