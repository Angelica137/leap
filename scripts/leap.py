def leap(year):
    return "leap 🐰" if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else "not leap 📆"
    if year % 400 == 0:
        return "leap 🐰"
    elif year % 100 == 0:
        return "not leap 📆"
    elif year % 4 == 0:
        return "leap 🐰"
    return "not leap 📆"
