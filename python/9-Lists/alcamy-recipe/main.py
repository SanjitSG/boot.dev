
def check_ingredient_match(recipe, ingredients):
    counter = 0
    missing_list = []
    for item in recipe:
       if item in ingredients:
           counter += 1
       else:
           missing_list.append(item)   
    percent = (counter/len(recipe))*100
    
    return percent, missing_list
                