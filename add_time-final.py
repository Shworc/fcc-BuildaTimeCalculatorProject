def add_time(start, duration, next_day=False):
    start_hour = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1].split(" ")[0])
    ampm = start.split(" ")[1]
    ampm_flip = {"AM":"PM", "PM":"AM"}
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    #days = ((start_hour + duration_hour) // 24)

    summinutes = (start_minutes + duration_minutes)
    sumhour = (start_hour + duration_hour)
    #print(f"{sumhour}:{summinutes} {ampm} after sum")
    #print(days)

    if summinutes >= 60:
        summinutes -= 60
        sumhour += 1
    
    days = ((start_hour + duration_hour) // 24)
    
    count_ampm_flip = sumhour // 12
    endH = sumhour % 12

    endH = endH=12 if endH == 0 else endH
    if(ampm == "PM" and sumhour + (summinutes%12) >= 12):
        days += 1
    #else:
    #    days = 0
    
    ampm = ampm_flip[ampm] if count_ampm_flip % 2 == 1 else ampm
    
    tRime = f"{endH}:{summinutes:02d} {ampm}"
    
    if next_day:
        next_day = next_day.lower().capitalize()
        if next_day in week:
            next_day_index = week.index(next_day)
            print(f"next_day_index {next_day_index} + days {days}")
            week_index = (next_day_index + days) % 7
            print(f"next_day_index {next_day_index} + days {days} = week_index {week_index}")
            day = week[week_index]
            print(f"day {day}")
            tRime += f", {day}"
    if days == 1:
        tRime += f" (next day)"
    elif days > 1:
        tRime += f" ({days} days later)"

    return tRime
print(repr(add_time('2:59 AM', '24:00', 'saturDay')))
