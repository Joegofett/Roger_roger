def clean(data): 
    """
    Final returns incremental keys 0-x each corresponding to a value that is a string example below 

    Message: Hello all this is a message 

    final = {0: 'Hello', 1 : 'All', 2 : 'this', 3 : 'is', 4 : 'a', 5 : 'message' }

    """
    new_data = data
    newList = new_data.split(' ')
    final = {}
    key = 0
    for info in newList:
        final[key] = info
        key += 1
    return final


def question(data):
    new_data = data
    newList = new_data.split(':')
    final = {}
    key = 0
    for info in newList:
        final[key] = info
        key += 1
    return final



