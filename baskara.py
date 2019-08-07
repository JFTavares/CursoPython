# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
from sympy import Symbol
from sympy import solve


#%%
a = input('Valor de a: ')
b = input('Valor de b: ')
c = input('Valor de c: ')


#%%
a= int(a)
b= int(b)
c= int(c)


#%%
def calcula_x(x):
    return a * x**2 - b * x + c


#%%
x = Symbol('x')
y = calcula_x(x)
resultado = solve(y)

print(resultado)


#%%



