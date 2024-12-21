#Словарь
my_dict = {'Almaz':2001,'Dima':2007,'Kolya':1987}
print(my_dict['Almaz'])
my_dict['Ivan']= 1895
print(my_dict)
my_dict.update({'Misha':2003,
                'Dasha':2006})
print (my_dict)
a=my_dict.pop('Dima')
print (my_dict)
print(a)
#Множество
my_set = {6,6,6,5,5,4,1,2,3,2,1,1,}
print(my_set)
my_set.add(7)
my_set.add(9)
my_set.discard(3)
print(my_set)
#надеюсь все сделал правильно
