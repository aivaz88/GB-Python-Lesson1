#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
#выдаёт номер четверти плоскости, в которой находится эта точка .

x = int(input('x='))
y = int(input('y='))
if x > 0:
    if y > 0:
        print('I четверть')
    else:
        print('IV четверть')
else:
    if y > 0:
        print('II четверть')
    else:
        print('III четверть')