def leap(year):
    return "leap 🐰" if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else "not leap 📆"
