# import required lib......
import wiotp.sdk.device
import time
import os
import datetime
import random
#import board
#import adafruit_dht
#import psutil


# We first check if a libgpiod process is running. If yes, we kill it!....
#for proc in psutil.process_iter():
#    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
#        proc.kill()
#sensor = adafruit_dht.DHT11(board.D23)


#config informations...
myconfig = {
    "identity": {
        "orgId": "z69c1z",
        "typeId": "w_dev",
        "deviceId": "w_dev1"
    },
    "auth": {
        "token": "SJAYik-EXtra_TXPDQ"
    }
}


#Connect IBM IOT cloud...
client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
client.connect()


#Declaring values
ms="OFF"
appmode="AUTO"


#Get responding data from IBM cloud... 
def myCommandCallback(cmd):
    print("Msg received from IBM IOT platform:%s" % cmd.data['command'])
    global ms
    global appmode
    
    #Get motor & Application state...
    m = cmd.data['command']

    if (m == "motoron"):
        print("Motor is switched ON")
        ms="ON"
    elif (m == "motoroff"):
        print("motor is switched OFF")
        ms="OFF"
    elif(m == "auto"):
        print("Application is changed to Automatic")
        appmode="AUTO"
    elif (m == "manual"):
        print("Application is changed to Manual")
        appmode="MANUAL"
    print(" ")


#Start the Process...
while True:
    soil = random.randint(0, 100)
    temp = random.randint(5, 150)
    hum = random.randint(0, 100)

    #Set all sensor and motor,Application State...
    myData = {'sensor_moisture': soil,
              'sensor_temperature': temp,
              'sensor_humidity': hum,
              'sensor_mstate': ms,
              'sensor_amode': appmode
              }

    #Push the Data into IBM Cloud...
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data successfully: %s", myData)

    #Check the any response from IBM Cloud...
    time.sleep(2)
    client.commandCallback = myCommandCallback

    #In Auto mode change motor state correspondingly... 
    if(appmode == "AUTO"):
        if(soil < 40):
            print("Motor is switched ON")
            ms="ON"
        else:
            print("motor is switched OFF")
            ms="OFF"
        print(" ")


#close the connection...
client.disconnect()
