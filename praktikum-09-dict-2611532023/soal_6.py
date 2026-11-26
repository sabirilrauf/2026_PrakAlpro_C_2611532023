schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day =" "
most = 0
for day, courses in schedule.items():
    if len(courses)>most:
        most = len(courses)
        busiest_day = day
print("busiest day: "+ busiest_day+ " ("+str(most)+")")

course=input()
count = 0
for courses in schedule.values():
    if course in courses:
        count = count + 1
print(course+": "+str(count)+" days")