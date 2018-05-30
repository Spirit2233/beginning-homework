'''
import math

def quadratic(a, b, c):
    if a==0:
        print('x等于',-c/b)
    elif b**2<4*a*c:
        print('没有解')
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        print('x1等于',x1,'\nx2等于',x2)
        #return x1,x2

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

quadratic(a,b,c)
'''

import math

def quadratic(a, b, c):
    if a==0:
        return -c/b
    elif b**2<4*a*c:
        return('none')
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

q=[quadratic(a,b,c)]
for x in q:
    print('结果是：',q)
