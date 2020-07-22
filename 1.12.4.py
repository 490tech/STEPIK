z = str(input()) #тип комнаты
if z=="треугольник":
  a = float(input()) #сторона1
  b = float(input()) #сторона2
  c = float(input()) #сторона3
  y = (a+b+c)/2
  print ((y*(y-a)*(y-b)*(y-c))**0.5)

if z=="прямоугольник":
  a = float(input()) #сторона1
  b = float(input()) #сторона2
  print ((a*b))
  
if (z == 'круг'):
  r = float(input()) #радиус
  p = 3.14 #пи
  print (p*r**2)
