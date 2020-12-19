


s = int(input())

a = (s % 10**3) // 10**2
b = (s % 10**2) // 10
c = (s % 10) // 10**0


print (a,b,c, sep = '' )
print (a,c,b, sep = '' )
print (b,a,c, sep = '' )
print (b,c,a, sep = '' )
print (c,a,b, sep = '' )
print (c,b,a, sep = '' )
