from scripts.leap import leap


def test_year_divisible_by_400():
    assert leap(2000) == "leap 🐰"


def test_year_divisible_by_100():
    assert leap(1900) == "not leap 📆"
