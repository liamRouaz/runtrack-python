def est_premier(job06):
    if job06 < 2:
        return False
    i = 2
    while i*i <= job06:
        if job06 % i == 0:
            return False
        i += 1
    return True

job06 = 1
while job06 <= 1000:
    if est_premier(job06):
        print(job06)
    job06 += 1
