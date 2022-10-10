import random
t=random.randint(0,100)
h=random.randint(1,100)
print("Temperature= ",t)
print("Humidity= ",h)
if(t>70):
    print("Danger!!!!!!   Very High temperature: ",t)
elif(t>50):
    print("Danger!!!!!!   High temperature: ",t)
