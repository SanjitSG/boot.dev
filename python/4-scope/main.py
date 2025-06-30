def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")

##
player_level = 4

# Don't touch below this line

def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

'''
pi = 3.14

def get_area_of_circle(radius):
    area = pi * radius * radius
    return area

Q: Does the get_area_of_circle function have access to the pi variable?
A: Yes, because the pi variable is in the glovbal scope

Q: Can the area variable inside the get_area_of_circle function be accessed outside of the function?
A: No, the variable defined inside a function are not accessible outside of it
'''