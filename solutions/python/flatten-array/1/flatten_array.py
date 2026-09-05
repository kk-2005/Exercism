def flatten(iterable):
    iterable = list(iterable) 
    i=0
    while i<len(iterable):
        if iterable[i] is None:                     # 1. Use 'is None' for safety
            iterable.pop(i)                         # 2. Pop by index, do NOT increment i
            continue                                # 3. Skip to next iteration
        if isinstance(iterable[i], (list, tuple, set)): 
            iterable=iterable[:i]+list(iterable[i])+iterable[i+1:]
        else:
            i+=1
    return iterable