startday = input("Day of the week of first day: ").strip()
match startday:
    case "Sunday":
        firstday = 0
    case "Monday":
        firstday = 1
    case "Tuesday":
        firstday = 2
    case "Wednesday":
        firstday = 3
    case "Thursday":
        firstday = 4
    case "Friday":
        firstday = 5
    case "Saturday":
        firstday = 6
    case _:
        print("Error")
allday = int(input("Days in the month: "))
counter = 0
weekday = firstday

print("\\begin{tabular}{@{}*7r@{}}")

def fillspace(n):
    s = str(n)
    if len(s) < 2:
        s += " "
    return s

while counter < allday:
    out = ""
    if weekday > 0:
        out += "   & "*weekday
    while weekday < 7:
        out += fillspace(counter+1) + " & "
        weekday += 1
        counter += 1
        if counter >= allday:
            break
    print(out[:-3] + " \\\\")
    weekday = 0

print("\\end{tabular}")