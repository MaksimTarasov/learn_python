fishing_pl = ('Pregel','Gvardeysk', (23.2332,56.3433))# в кортеже еще  один кортеж. он раскрываетяы доп переменные
# и переменные передаются аргументами
#пример расскрытия картежа. Также пример применения функции формат {"номер аргумента":"количество знаков"}
print (fishing_pl[2])
(a,b)= fishing_pl[2]
print('{:15} | {:^9} | {:9}'.format('','lat.','long.'))
print('You fishing on river {0:15}, city {1:9} with coords: {2:8},{3:8}'.format(fishing_pl[0],fishing_pl[1],a,b))