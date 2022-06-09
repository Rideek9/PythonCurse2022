data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def calendar(month,days):
    print()
    print(month, end='\n')
    list_day = []
    for day in days:
        if day <= 8:
            list_day.append(f"0{str(day+1)}")
        else:
            list_day.append(f"{str(day+1)}")
    week = ""
    for index, day in enumerate(list_day):
        if (index+1) % 8!= 0:
            week+= f"{day} "
        else:
            week+=f"\n"
    print(week)


def calendar_year():
    for index, i in enumerate(data):
        calendar(data[index][0], data[index][1])


calendar_year()


