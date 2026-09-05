def steps(number):
    steps=0
    counter=number
    if not isinstance(number,int) or number<=0:
        raise ValueError("Only positive integers are allowed")
    while counter!=1:
        if counter%2==0:
            counter/=2
        else:
            counter=3*counter+1
        steps+=1
    return steps