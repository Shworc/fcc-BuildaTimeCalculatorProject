def add_time(start, duration):
    start_hour = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1])
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    sumhour = 0
    summinutes = 0

    summinutes = start_minutes + duration_minutes
    sumhour = start_hour + duration_hour

    if summinutes > 60:
        summinutes -= 60
        sumhour += 1

    # parse_time function try
    """[h, m] = parse_time(start)
    print(f"h={h} m={m}")
    [ah, am] = parse_duration(duration)
    print(f"\nah={ah} am={am}")
    m += am
    print(f"\nm={m}")
    h += ah
    print(f"\nh={h}")
    if m > 60:
        m %= 60
        h += 1
        indicator="AM"
        print(f"\nm={m} h={h}")"""
        
    #    
    #print(f"{start_hour}:{start_minutes}")
    #print(f"{sumhour}:{summinutes}")


    return new_time