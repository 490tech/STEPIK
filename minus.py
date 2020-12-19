

# print(min(int(input()), int(input()),int(input()),int(input())))

# v = int(input())

# print('детство' if v <= 13 else 'молодость' if 13 < v < 25 else 'зрелость' if 24 < v < 60 else 'старость' )
 
a,b,c = int(input()), int(input()),int(input())

if a < 0:
    a=0
if b < 0:
    b=0
if c < 0:
    c=0
print ('0' if a+b+c <= 0 else a+b+c)
# x=a+b+c
#	if x < 0:
#	x==0
#	print (x)
