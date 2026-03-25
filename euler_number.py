def factorial(i):
    f = 1
    if i == 0:
        f = 1
    else:
        for i in range(1,i+1):
            f = i * f
            i = i + 1
    return f
        
def euler_number(place):
    n = 0
    e = 0
    for n in range(0,place):
        e += 1/(factorial(n))
        n += 1
    return e
place = int(input('enter no of terms to be considered:'))
e = euler_number(place)
print(f"{e}")
    