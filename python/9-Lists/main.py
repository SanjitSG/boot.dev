'''def reverse_list(items):
    reversed_list = []
    for i in range(len(items)):
        reversed_list.append(items[len(items) - 1 - i])
    
    return reversed_list
'''


def reverse_list(items):
    return items[::-1]
