# TODO Найдите количество книг, которое можно разместить на дискете
import math
# в рамках учебного процесса решил воспользовься словарем, естественно для сокращения кода такой подход не уместен
dic={
    'p':100,
    'str':50,
    'sy':25,
}
x=dic['p']
y=dic['str']
z=dic['sy']
byt=x*y*z*4
print(type(byt))
Mb=byt/1024**2
print(type(Mb))
n=1.44/Mb
n_final=math.floor(n)
print(n_final)

