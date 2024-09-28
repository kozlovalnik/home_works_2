for n in range(3, 21):
    str_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                str_ += str(i) + str(j)

    print(n, '-', str_)
