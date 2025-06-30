def get_champion_slices(champions):
    lenght = len(champions)
    list_one = champions[2:]
    list_two = champions[:lenght - 1]
    list_three = champions[::2]

    return list_one, list_two, list_three

    