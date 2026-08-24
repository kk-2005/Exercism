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
    count=queue.count(person_name)
    return count
    pass


def remove_the_last_person(queue):
    name=queue.pop()
    return name
    pass


def sorted_names(queue):
    return sorted(queue)
    pass
