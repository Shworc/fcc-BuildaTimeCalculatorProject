def add_time(start, duration):
    start_hour = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1])
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[0])
    ampm = str(start.split(" ")[0])
    sumhour = 0
    summinutes = 0

    summinutes = start_minutes + duration_minutes
    sumhour = start_hour + duration_hour

    if summinutes > 60:
        summinutes -= 60
        sumhour += 1
    if sumhour > 12:
        ampm = "PM"
    else:
        ampm = "AM"

    
    #    
    #print(f"{start_hour}:{start_minutes} {ampm} + {duration}")
    #print(f"{sumhour}:{summinutes} {ampm}")
    new_time = print(f"{sumhour}:{summinutes:02d} {ampm}")


    return new_time