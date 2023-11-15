data ="From stephen.marquaz@uct.ac.za Sat Jan 5 09:14:16 2008"
x= data.find("@")
print(x)
y =data.find(" ",x)
print(y)
z=data[x :y]
print(z)