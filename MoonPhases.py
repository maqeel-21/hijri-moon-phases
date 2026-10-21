# Enter a day (1-30) of the Hijri calendar and get the approximate moon phase.
Moon = ""
n = int(input("Enter a day from the Hijri calendar month: "))
if n < 0 or n > 30:
    Moon = "Please enter a valid day"
elif n >=1 and n <=5:
    Moon = "waxing crescent"
elif n >=6 and n <=8:
    Moon = "first quarter"
elif n>=9 and n<=13:
    Moon = "waxing gibbous"
elif n >=14 and n<=16:
    Moon = "Full Moon"
elif n>=17 and n<=21:
    Moon = "waning gibbous"
elif n>=22 and n<=23:
    Moon = "Last quarter"
elif n>=24 and n<=28:
    Moon = "waning crescent"
else:
    Moon = "New Moon"
print(Moon)
input("Press Enter to exit")