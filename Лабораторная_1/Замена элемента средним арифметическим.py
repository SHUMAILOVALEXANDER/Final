#Первое решение
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a=len(numbers)
pos=numbers.index(None)
del numbers[pos]
arif=sum(numbers)/a
numbers.insert(pos,arif)
print(numbers)

#Второе решение
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
p_1 = numbers[:numbers.index(None,0,-1)]
p_2 = numbers[numbers.index(None,0,-1)+1:]
sum_1 = sum(p_1)
sum_2 = sum(p_2)
sum_gen=sum_1+sum_2
n_len = len(numbers)
arif_1=sum_gen/n_len
pos=numbers.index(None,0,-1)
del numbers[pos]
numbers.insert(pos,arif_1)
print(numbers)
# TODO заменить значение пропущенного элемента средним арифметическим

