def get_season(month):
    """Счисление начинается с 1"""
    if (month >= 1 and month <= 2) or month == 12:
        return "Зима"
    elif month >= 3 and month <= 5:
        return "Весна"
    elif month >= 6 and month <= 8:
        return "Лето"
    elif month >= 9 and month <= 11:
        return "Осень"

def get_season2(month):
    seasons = {"Зима": (1, 2, 12),
               "Весна": (3, 4, 5),
               "Лето": (6, 7, 8),
               "Осень": (9, 10, 11)}

    for key in seasons.keys():
        if month in seasons[key]:
            return(key)

def test_season():
    assert get_season(1) == ("Зима")

def test_season2():
    assert get_season(12) == ("Зима")

def test_season3():
    assert get_season(3) == ("Весна")

def test_season4():
    assert get_season(6) == ("Лето")

def test_season5():
    assert get_season(9) == ("Осень")


def test_season2_1():
    assert get_season2(1) == ("Зима")

def test_season2_2():
    assert get_season2(12) == ("Зима")

def test_season2_3():
    assert get_season2(3) == ("Весна")

def test_season2_4():
    assert get_season2(6) == ("Лето")

def test_season2_5():
    assert get_season2(9) == ("Осень")