#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }


def recipe_batches(recipe, ingredients):
	# capturing the value of the ingredient we have the least of (the limiting factor for num of batches we can make)
	lowest_ingredient = 10000
	# comparing ingredients in both recipes and ingredients
	# in the case that we don't have all the ingredients
	for ingredient in recipe:
		# if the recipe calls for more than we have (or if we don't have the ingredient at all), we can't make it
		if ingredient not in ingredients or recipe[ingredient] > ingredients[ingredient]:
			return 0
		# otherwise, divide the amount of ingredients we have by what the recipe calls for, set that to "lowest_ingredient" if it is
		elif ingredients[ingredient] / recipe[ingredient] < lowest_ingredient:
			lowest_ingredient = ingredients[ingredient] / recipe[ingredient]

	# then we're going to floor this int to get the total number of batches
	return int(lowest_ingredient)





print(recipe_batches(recipe, ingredients))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))