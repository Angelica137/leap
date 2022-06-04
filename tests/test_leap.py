from scripts.leap import leap


def test_year_divisible_by_400():
    assert leap(2000) == "leap 🐰"
