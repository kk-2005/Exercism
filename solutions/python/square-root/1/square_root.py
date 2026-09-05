def square_root(number):
    i=0
    while i*i<=number:
        if i*i==number:
            return i
        else:
            i+=1
    pass
