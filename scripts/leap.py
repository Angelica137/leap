def leap(year):
    if year % 400 == 0:
        return "leap 🐰"
    elif year % 100 == 0:
        return "not leap 📆"
    elif year % 4 == 0:
        return "leap 🐰"
