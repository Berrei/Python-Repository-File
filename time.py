t=int(input('enter the time in sec: '))
a=t//86400
x=t%86400
b=x//3600
y=x%3600
c=y//60
z=y%60
print('Days:%d'%a,'Hours:%d'%b,'Minutes:%d'%c,'Sec:%d'%z)
input('press enter to exit')