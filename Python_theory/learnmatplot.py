# import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
#for gui



def matplotlibsops():

    #matplot plot histogram
    # rg = np.random.default_rng(1)
    # mu, sigma = 2, 0.5
    # v = rg.normal(mu, sigma, 10000)
    # plt.hist(v, bins=50, density=True)
    # plt.show()
    # plt.savefig('plot.png')

    np.random.seed(seed=0)
    x = np.random.randn(1000)
    y = np.random.randn(100)
    z = np.random.randn(10)
    fig, ax = plt.subplots()
    ax.boxplot((x, y, z), vert=True, showmeans=True, meanline=True,
               labels=('x', 'y', 'z'), patch_artist=True,
               medianprops={'linewidth': 2, 'color': 'purple'},
               meanprops={'linewidth': 2, 'color': 'red'})
    plt.show()

    # pie chart
    x, y, z = 128, 256, 1024
    colors = ['#b70b53','#e49ab0','#7a1453'] #hex color codes
    fig, ax = plt.subplots()
    ax.pie((x, y, z), labels=('Sarthak', 'y', 'z'), autopct='%1.1f%%', colors=colors)
    plt.show()

matplotlibsops()