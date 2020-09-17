# Конвертер, переводящий все величины в литры (дм^3)
value = int(input()) # предлагаем ввести число, которое будем переводить в литры
dimension = input() + '^3' # предлагаем ввести единицы измерения командой input и заносим это в переменную dimension
if dimension == 'sm^3': # в ifах перечисляем возможные варианты переменной dimension и говорим, какую команду (print(арифметическое действие)) для каждого случая надо выполнить
    print(value * (10**(-3)))
elif dimension == 'mm^3': 
    print(value * (10** (-6)))
elif dimension == 'dm^3': 
    print(value * 1)
elif dimension == 'm^3': 
    print(value * 1000)
elif dimension == 'km^3': 
    print(value * 10000)
else: #если ни одно из вышеперечисленных условий не выполнено, конвертер выведет 'Cannot perform operation'
    print('Cannot perform operation')