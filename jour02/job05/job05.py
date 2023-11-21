for job05 in range(1, 101):
#if = si
#% = operateur modulo y renvoi le reste de la division de deux nombre
    if job05 % 3 == 0 and job05 % 5 == 0:
        print("FizzBuzz")
#elif = et si
    elif job05 % 3 == 0:
        print("Fizz")
    elif job05 % 5 == 0:
        print("Buzz")
#else = sinon
    else:
        print(job05)
