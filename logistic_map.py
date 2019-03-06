import matplotlib.pyplot as plt
import numpy as np
# np.set_printoptions(formatter={'float_kind':'{:f}'.format})

# R = 2


def miplot(vec, R):
    plt.plot(vec,'-', linewidth=0.8, color='#340B8C')
    plt.ylim(0,1)
    plt.xlim(0, vec.__len__()-1)
    plt.ylabel('x(t)')
    plt.xlabel('t')
    # plt.grid(True)
    # plt.title(tit)
    plt.title('R = %1.2f' %R)

    plt.show()


def mapa(x0, R, n=20, plot = True):

    x = np.zeros(100)
    x[0] = x0

    for i in range(0, 100 - 1):
        x[i + 1] = R * x[i] * (1 - x[i])

    if plot : miplot(x[0:(n+1)],R)

    return x




mapa(x0=0.2 , R=2, n=5)
mapa(x0=0.99, R=2)
mapa(x0=0.2,  R=3.1)
mapa(x0=0.2,  R=3.49)

mapa(R=4   , x0=0.2, n=50)
mapa(R=4   , x0=0.20000001, n=50)


def attractor(vec):
    att = set(vec[-1:-10:-1].round(2))
    return att



for r in np.arange(2.8, 4, 0.1):
    # print(r)
    a = attractor(mapa(x0=0.2 , R=r, plot=False))
    print( str(r) + " : " + str(a.__len__()) )
    print( str(a) )
    # print(str(r) + " : " + str( attractor(mapa(x0=0.2 , R=r, plot=False)) )


mapa(x0=0.2, R=3.9, n=100, plot=True)
attractor(mapa(x0=0.2 , R=3.9, n=100, plot=True))

