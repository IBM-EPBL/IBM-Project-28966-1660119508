import random
Temperature=random.randint(1,100)
Humidity=random.randint(1,100)
print("Temperature= ",Temperature)
print("Humidity= ",Humidity)
if(Temperature>50):
    print("Warning........High temperature: ",Temperature)
elif(Temperature<10):
    print("Warning........Low temperature: ",Temperature)