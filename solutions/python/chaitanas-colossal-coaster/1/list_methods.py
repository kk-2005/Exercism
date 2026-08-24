def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type==1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue
    pass


def find_my_friend(queue, friend_name):
    try:
        idx=queue.index(friend_name)
        return idx
    except ValueError:
        pass


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index,person_name)
    return queue
    pass


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue
    pass


def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name you wish to count or track.

    Returns:
        int: The number of times the name appears in the queue.
    """
    count=queue.count(person_name)
    return count
    pass


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        str: The name that has been removed from the end of the queue.
    """
    name=queue.pop()
    return name
    pass


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        list: A copy of the queue in alphabetical order.
    """
    return sorted(queue)
    pass
