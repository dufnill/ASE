def sum(m,n):
    add_step = 1 if n > 0 else -1
    for i in range (0,abs(n)):
        m += add_step
    return m

def divide (a,b):
    i = 0
    negres = a > 0 and b > 0 or a < 0 and b < 0
    a = abs(a)
    b = abs(b)
    if b == 0:
        i = "Can't divide by 0"
    else:
        while a-b >= 0:
            a -= b
            i += 1
    if negres == 0:
        return i*-1
    else:
        return i