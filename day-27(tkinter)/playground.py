def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


total = add(1, 48, 78, 23, 777, 45)

print(total)

def calculate(val ,**kwargs):
    result = val
    if kwargs["div"]:
        result = result / kwargs["div"]
    if kwargs["multi"]:
        result = result * kwargs.get("multi")
    if kwargs["add"]:
        result = result * kwargs.get("add")
    if kwargs["sub"]:
        result = result - kwargs["sub"]     
    return result


cal_value = calculate(val=10, div=2, multi=100, add=85, sub=500)

print(cal_value)