def add_time(start, duration, next_day=None):
    start_hour = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1].split(" ")[0])
    ampm = start.split(" ")[1]
    ampm_flip = {"AM":"PM", "PM":"AM"}
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    summinutes = start_minutes + duration_minutes
    sumhour = start_hour + duration_hour

    days = int(duration_hour+duration_minutes) // 24
    
    if summinutes >= 60:
        summinutes -= 60
        sumhour += 1

    count_ampm_flip = sumhour // 12
    endH = sumhour % 12

    endH = endH=12 if endH == 0 else endH
    if(ampm == "PM" and start_hour + (duration_minutes%12) >= 12):
        days += 1

    ampm = ampm_flip[ampm] if count_ampm_flip % 2 == 1 else ampm
    
    tRime = f"{endH}:{summinutes:02d} {ampm}"
    
    if next_day:
        next_day = next_day.lower().capitalize()
        if next_day in week:
            #print(next_day)
            #next_day_index = week.index(next_day)
            week_index = ((week.index(next_day) + days) % 7)
            day = week[week_index]
            tRime += f", {day}"

    if days == 1:
        tRime += f" (next day)"
    elif days > 1:
        tRime += f" ({days} days later)"

    return tRime