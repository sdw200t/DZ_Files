from pprint import pprint

def readcook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='UTF-8') as f:
        name = ''
        list_ingredients = []
        for line in f:
            if name == '':
                name = line[:-1]
                continue
            ingredients = line.split(' | ')
            if len(ingredients) == 1 and line != '\n':
                continue
            if line == '\n':
                cook_book[name] = list_ingredients
                list_ingredients = []
                name = ''
                continue
            list_ingredients.append({'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2][:-1]})
        cook_book[name] = list_ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = readcook_book()
    dict_ingredients = {}
    for cook in dishes:
        list_ingr = cook_book[cook]
        for ingr in list_ingr: 
            if ingr['ingredient_name'] in dict_ingredients:
                dict_ingredients[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count    
            else:
                dict_ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}    
                  

    return dict_ingredients

dict_ingredients = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(dict_ingredients)
