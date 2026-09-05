def score(x, y):
    distance=((x**2)+(y**2))**(1/2)
    if distance>10:
        return 0
    elif distance>5 and distance<=10:
        return 1
    elif distance>1 and distance<=5:
        return 5
    else:
        return 10
