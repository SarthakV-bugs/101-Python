"""numpy- numerical computations and all matrices operations
heart of numpy- n dimension array
numpy.org, pandas.org"""
import sys

import numpy as np
import pandas as pd
# import matplotlib.pylot as plt
# import sys

def numpyops():


    # a = np.arange(15)
    # a = a.reshape(3,5)
    # print(a.shape)
    # print(a.ndim)
    # print(a.size)
    # print(a.itemsize)
    #
    #
    # z = np.zeros((3, 4))
    # print(z)
    # x = np.ones((2, 3, 4), dtype=np.int16)
    # print(x)
    # print(x.ndim)
    # y = np.empty((2, 3))
    # print(y)
    #
    # num_array = np.arange(10, 30, 5)
    # print(num_array)
    # float_array = np.arange(0, 2, 0.3)
    # print(float_array)
    #
    #
    # n = np.linspace(0, 2 ,9)
    # print(n)
    # x = np.linspace(0, 2*np.pi, 100)
    # f = np.sin(x)
    # print(x)
    # print(f)
    # print(type(f))
    #
    #
    # #print arrays
    # #1-d array
    #
    #
    # #
    # # print(np.arange(10000).reshape(100, 100))
    # # np.set_printoptions(threshold=sys.maxsize)
    # # print(np.arange(10000).reshape(100, 100))
    # #
    # # ### basic operations
    # # # arithmetic operators on arrays apply elementwise
    # # a = np.array([20, 30, 40, 50])
    # # b = np.arange(4)
    # # c = a - b
    # # d = b ** 2
    # # s = 10 * np.sin(a)
    # #
    # # A = np.array([[1, 1, 2],
    # #               [0, 1, 2]])
    # # B = np.array([[2, 0],
    # #               [3, 4]])
    # # # C = A * B  # element wise
    # # # print(C)
    # # E = A @ B  # matrix multiplication
    # # D = A.dot(B)
    # # print(D)
    # # print(E)
    #
    # rg = np.random.default_rng(1) #random gen number has an initialisation with SEED, Seed controls the generation of random number everytime
    # a = np.ones((2, 3), dtype=int)
    # b = rg.random((2, 3))
    # a *= 3
    # print(a)
    #
    # # #
    # # a = np.ones(3, dtype=np.int32)
    # # b = np.linspace(0, np.pi, 3)
    # # print(b.dtype.name)
    # # c = a + b
    # # print(c)
    # # print(c.dtype.name)
    # # d = np.exp(c * 1j)
    # # print(d)
    # # print(d.dtype.name)
    #
    # #
    # # a = rg.random((2, 3))
    # # print(a)
    # # print(a.sum())
    # # print(a.min())
    # # print(a.max())
    #
    # # b = np.arange(12).reshape(3, 4)
    # # print(b)
    # # print(b.sum(axis=0))  # sum column-wise
    # # print(b.min(axis=1))     # min of each row)
    # # print(b.cumsum(axis=1))  # cumulative sum along each row)
    # #
    # #
    # # a = np.arange(10) ** 3
    # # print(a)
    # # print(a[2:5])   #0th based index
    #
    #
    # #shape manipulation methods
    #
    # #Raval -  flattening the array, convert a 2*2 into 4*1
    # #Reshape - converts 2*2 into 1*4
    # #vStack - stack the arrays vertically
    # #column stack
    # #Resize
    # #hsplit
    # #column stack
    #
    # # a = np.floor(10 * rg.random((3,4)))
    # # print(a)
    # # print(a.shape)
    # #
    # # print(a.ravel())
    # # print(a.reshape(6,2))
    # # print(a.T)
    # # print(a.T.shape)
    # # print(a.shape)
    # # print(a)
    # # print(a.resize((2,6)))
    # # print(a.reshape(3, -1))
    #
    # a = np.floor(10 * rg.random((2, 2)))
    # print(a)
    # b = np.floor(10 * rg.random((2, 2)))
    # print(b)
    # print(np.vstack((a, b)))
    # print(np.hstack((a, b)))
    #
    # from numpy import newaxis
    # np.column_stack((a, b))  # with 2D arrays
    # a = np.array([4., 2.])
    # b = np.array([3., 8.])
    # c = np.column_stack((a, b))  # returns a 2D array
    # print(c)
    # d = np.hstack((a, b))
    # print(d)
    # e = a[:, newaxis]
    # print(e)
    # f = np.column_stack((a[:, newaxis], b[:, newaxis]))
    # print(f)
    # g = np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same)
    # print(g)
    # # the function row_stack is equivalent to vstack for any input arrays. In fact, row_stack is an alias for vstack:
    # print(np.column_stack is np.hstack)
    # print(np.row_stack is np.vstack)
    #
    #
    # ###splitting the array into smaller ones
    # a = np.floor(10 * rg.random((2, 12)))
    # print(a)
    # h = np.hsplit(a, 3)
    # print(h)

numpyops()