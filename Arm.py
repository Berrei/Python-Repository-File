x=input('Enter the number')
i=len(x)
sum=0
for j in range(0,i):
     sum+=int(x[j])**i
if int(x)==sum:
     print(x,'is the Armstrong number')
else:
     print(x,'is not the Armstrong number') 
