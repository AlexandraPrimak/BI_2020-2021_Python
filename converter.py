# Конвертер, переводящий все величины в литры (дм^3)
# предлагаем ввести число, которое будем переводить в литры
value = int(input()) 
# предлагаем ввести единицы измерения командой input и заносим это в dimension
dimension = input() + '^3'  
# в ifах перечисляем возможные варианты переменной dimension и говорим, 
# какую команду (print(арифметич. действие)) для каждого случая надо выполнить
if dimension == 'sm^3':
    print(value * (10 ** (-3)))
elif dimension == 'mm^3':
    print(value * (10 ** (-6)))
elif dimension == 'dm^3':
    print(value * 1)
elif dimension == 'm^3':
    print(value * 1000)
elif dimension == 'km^3':
    print(value * (10000 ** 3))
# если ни одно из вышеперечисленных условий не выполнено, 
# конвертер выведет 'Cannot perform operation'
else:
    print('Cannot perform operation')
