#git pull - check status 

#*** example of the thermostat***
# current tempretature of room 

current_temp = 26
# заданное значение диапазона температуры 
min_temp = 10
max_temp = 25

# параметр "люди есть или нет"
#h = true = люди есть 
#h = false = людей нет
h = True


# the logic of thermostat
if current_temp < min_temp and not h: 
    print (f"heating turned on until {min_temp}")
elif current_temp < max_temp and h:
    print (f"heating turned on until {max_temp}")
else: 
    print ("heating turned off")

