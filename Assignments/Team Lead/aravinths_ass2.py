import random
Random_Temperature=random.randint(1,100)
Random_Humidity=random.randint(1,100)
print("Current Temperature is ",Random_Temperature)
print("Current Humidity is ",Random_Humidity)
if(Random_Temperature>90):
    print(" Temperature is more than 90 , very Hot ")
elif(Random_Temperature>50):
    print(" Temperature is more than 50 , Hot ")
elif(Random_Temperature<=10):
    print(" Temperature is less than 10 , Cold ")