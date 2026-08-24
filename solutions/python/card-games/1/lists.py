def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand):
    """Calculate and return the true average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    true_avg = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return true_avg == first_last_avg or true_avg == middle_card


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    evens_avg = card_average(hand[0::2])
    odds_avg = card_average(hand[1::2])
    
    return evens_avg == odds_avg


def maybe_double_last(hand):
    """Multiply a Jack card value (11) in the last index position by 2."""
    output_hand = hand.copy()
    if output_hand[-1] == 11:
        output_hand[-1] *= 2
        
    return output_hand

