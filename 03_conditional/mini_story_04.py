# thermostat alert system

device_status = "active"
temperature = int(input("Measure Temperature "))
if device_status == "active":
    if temperature > 35 :
        print("high temperature")
    else:
        print("tempratur normal")
else:
    print("device is offline")
  