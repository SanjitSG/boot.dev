def reverse_list(items):
    reverse_list = []
    for i in range(len(items)):
        reverse_list.append(items[len(items) - 1 - i])
    
    return reverse_list


'''
def reverse_list(items):
    return items[::-1]
'''