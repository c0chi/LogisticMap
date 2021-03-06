# -*- coding: utf-8 -*-
"""mapa_logistico.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xiNjXm6PHTNykyHKjhTJ5OuHF-1OwodW

# Mapa logístico

---

### Intro

*x (t+1) = R . x(t) . (1- x(t) )*

Defino la funcion de arriba como *mapa(x0, R, n, plot )* donde

*  x0:  representa las condiciones iniciales
*  R : constante
*  n : la cantidad de puntos a graficar
*  plot: True/False para graficar o no el mapa creado


(Nota: está pensado para valores iniciales de x entre 0 y 1)
"""

import matplotlib.pyplot as plt
import numpy as np

def mapa(x0, R, n=20, plot = True):

    x = np.zeros(100)
    x[0] = x0

    for i in range(0, 100 - 1):
        x[i + 1] = R * x[i] * (1 - x[i])

    if plot : miplot(x[0:(n+1)],R) # n<=100

    return x
  
  
def miplot(vec, R):
    plt.plot(vec,'o-', linewidth=0.8, color='#340B8C')
    plt.ylim(0,1)
    plt.xlim(0, vec.__len__()-1)
    plt.ylabel('x(t)')
    plt.xlabel('t')
    # plt.grid(True)
    # plt.title(tit)
    plt.title('R = %1.2f' %R)

    plt.show()

"""La función *mapa()* devuelve el vector x(t) generado para el valor de R y las condiciones especificas y además la grafica según *miplot()*"""

mapa(x0=0.2 , R=2, n=10)

"""Se ve como los mapas

```
mapa(x0=0.4 , R=2, n=10)
mapa(x0=0.2 , R=2, n=10)
```

convergen a *xt=0.5* 


En el primer caso le lleva 5 iteraciones, en el segundo 7.
"""

mapa(x0=0.4 , R=2, n=10)
mapa(x0=0.2 , R=2, n=10)

"""Si las condiciones iniciales son más extremas.

```
mapa(x0=0.99 , R=2, n=10)
```

El resultado es el mismo. Una vez que la serie alcanza el valor  0.5  no puede escapar.
"""

mapa(x0=0.99 , R=2, n=20)

"""Para otro valor de R, el punto de convergencia es distinto pero el flujo similar.

```
mapa(x0=0.99 , R=2.6, n=10)
```
"""

mapa(x0=0.99 , R=2.6)

"""Es interesante ver que pasa para otros valores de R.    


Por ejemplo, para R=3.1 la serie no converge a un valor sino que queda oscilando entre 2.

```
mapa(x0=0.2,  R=3.1)
mapa(x0=0.8,  R=3.1)
```

Sin importar las condiciones iniciales (x0), la serie queda para siempre entre : { 0.55801412,  0.76456652 }. Sus *puntos atrayentes*.
"""

mapa(x0=0.2,  R=3.1)
mapa(x0=0.8,  R=3.1)

"""### Bifurcación


Para valores de R entre 3.1 y 3.4, los puntos atrayentes cambian pero siguen siendo 2.

Otros ejemplos:

```
mapa(x0=0.2,  R=3.1)  # {0.55801413, 0.76456652}
mapa(x0=0.5,  R=3.25) # {0.49526517, 0.81242714}
mapa(x0=0.2,  R=3.3)  # {0.47942702, 0.82360328}
```
"""

mapa(x0=0.2,  R=3.3)  # {0.47942702, 0.82360328}

"""Para valores de R entre 3.4 y 3.5, se da otra bifurcación. Los puntos atrayentes finales pasan a ser 4 !!   

Pero, no obstante las condiciones iniciales, conocido el valor de R se puede saber donde terminará la serie.



```
mapa(R=3.42, x0=0.3, n=50)  #{0.44697897, 0.84538559, 0.44702407, 0.84540194}
mapa(R=3.42, x0=0.99, n=50) #{0.44697897, 0.84538559, 0.44702407, 0.84540194}
```
"""

mapa(R=3.42, x0=0.3, n=50)

"""El punto es que a medida que R crece, se vuelven a dar puntos de bifurcación y los puntos atrayentes pasan a ser {8,16, 32,...}.    
Construimos una función simple y aproximada para obtener el valor final al que tiende la serie :
"""

def atractor(vec):
    att = set(vec[-1:-10:-1].round(4))
    return att

"""Ejemplos:


```
atractor(mapa(R=3.1, x0=0.2 , n=100, plot=False))
atractor(mapa(R=3.54, x0=0.2 , n=100, plot=False))
```
"""

atractor(mapa(R=3.54, x0=0.9, plot=False))

# ver redondeo
#for r in np.arange(2, 4, 0.1):
#    a = atractor(mapa(x0=0.2 , R=r, plot=False))
#    print( str(r) + " : " + str(a.__len__()) )
#    print( str(a) )

"""Hasta cierto valor de R, el sistema es predecible en tanto uno podría saber donde convergerá la serie independientemente de las condiciones de partida.



```
mapa(x0=0.9,R=3.54, n=100)
mapa(x0=0.1,R=3.54, n=100)

```
"""

mapa(x0=0.9,R=3.54, n=100);print(atractor(mapa(x0=0.9,R=3.54, plot=False)))
mapa(x0=0.1,R=3.54, n=100);print(atractor(mapa(x0=0.1,R=3.54, plot=False)))

"""### Sistema caótico

Pasado un límite ( R ~ 3.57 ),  el período se vuelve infinito y el sistema se vuelve totalmente dependiente de las condiciones iniciales.
"""

mapa(x0=0.4999,R=3.95, n=100)
mapa(x0=0.5001,R=3.95, n=100)
plt.show()
"""Aca vemos como un pequeño cambio en las condiciones iniciales cambian completamente el mapa luego de un tiempo:

"""




x1 = mapa(x0=0.4999,R=3.95, plot=False)
x2 = mapa(x0=0.5001,R=3.95, plot=False)

plt.ylim(0, 1)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.title('R = 4.00')
plt.plot(x1, '-', linewidth=0.8, color='red')
plt.plot(x2, '-', linewidth=0.8, color='blue')
plt.show()


import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
sess.run(hello)
'Hello, TensorFlow!'
a = tf.constant(10)
b = tf.constant(32)
sess.run(a + b)
42
sess.close()
