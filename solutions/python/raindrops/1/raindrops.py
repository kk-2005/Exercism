def convert(number):
    string=""
    if number%3==0:
        string+="Pling"
    if number%5==0:
        string+="Plang"
    if number%7==0:
        string+="Plong"
    elif number%3!=0 and number%5!=0 and number%7!=0:
        string=str(number)
    return string
    pass
