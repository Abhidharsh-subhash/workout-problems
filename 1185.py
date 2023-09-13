# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"

def dayOfTheWeek(day,month,year):
    x={
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }
    if month < 3:
        month += 12
        year -= 1

    J = year // 100
    K = year % 100

    h = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
    return x[h]

day = 15
month = 8
year = 1993
print(dayOfTheWeek(day,month,year))
