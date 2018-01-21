from sympy import *
import numpy as np

t = symbols('t', real=True)
p = plot( sin(2*pi*t/5), 0.5*cos(2*pi*t/3),
(t,-10,10), show=False, legend=True,
axis=True )
p.title='SymPy Plot\n'
p.ylabel='$f(t)$'
p.xlabel='$t$'
p[0].line_color='g'
p[1].line_color='b'
p.show()