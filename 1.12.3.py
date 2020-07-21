a = float(input())
b = float(input())
c = str(input())
if (c == '+'):
    print (a + b)
if (c=='-'):
    print (a - b)
if ( c=='*'):
    print(a*b)
if (c=='pow'):
    print(a**b) 
if (b==0.0) and (c=='mod' or (c=='/') or (c=='div')):
    print('Деление на 0!')      
elif (c=='/'):
    print (a/b)
elif (c=='mod'):
    print (a%b)      
elif (c=='div'):
    print ( a//b)
