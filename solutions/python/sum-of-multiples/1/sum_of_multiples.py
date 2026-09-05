def sum_of_multiples(limit, multiples):
    # Create a set to store all unique multiples
    unique_multiples = set()
    
    # Generate multiples for each number and add them to the set
    for factor in multiples:
        if factor > 0:  # Prevent step-size errors for 0
            unique_multiples.update(range(factor, limit, factor))
            
    return sum(unique_multiples)