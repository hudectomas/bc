def check_value(x):
    if (x > 0 and x < 100) or (x >= 1 and x <= 99):  # Redundantná podmienka
        return True
    return False
