def classify(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    # 2. Find proper divisors
    list_factors = [x for x in range(1, number) if number % x == 0]
    sum_factors = sum(list_factors)
    
    # 3. Classify the number
    if number == sum_factors:
        return "perfect"
    elif sum_factors > number:
        return "abundant"
    else:
        return "deficient"
