def weird_number(num):
    if not isinstance(num, (int, float, str)):
        raise TypeError("this function only accepts integers, floats and strings.")
    try:
        num = float(num)
    except:
        num = 0
    else:
        num = num**3
    finally:
        num += 1
        return num
