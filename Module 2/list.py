foodList = ['Vadapav','Pizza','Dabeli','Panipuri','Burger','Dosa','Salad']

#To Print whole List
print(foodList)

#To fetch particular value from the list
print(foodList[2])
print(foodList[-1])

#To slice the list
print(foodList[0:3])
print(foodList[2:])
print(foodList[:4])

#To find length of list
print(len(foodList))

#To Print all values in the list
for items in foodList:
    print(items)

#To find index value of any item .index('item')
print(foodList.index('Dosa'))


#To add an item at last, in the list .append('item')
print(foodList.append('Sandwich'))
print(foodList)

#To insert an item at a specific index, in the list .insert(index, 'item')
foodList.insert(2, "Maskabun")
print(foodList)

#To remove an item from the list .remove('item')
foodList.remove('Burger')
print(foodList)

#To remove the last item from  list .pop()
foodList.pop()
print(foodList)

#To remove the item from list from a specific index value .pop(index)
foodList.pop(2)
print(foodList)

#To reverse the list .reverse()
foodList.reverse()
print(foodList)


#To sort items in list .sort
foodList.sort()
print(foodList)


#To clear or empty the list .clear()
foodList.clear()
print(foodList)

#To delete the list 'del listname'
del foodList
#print(foodList) This will give an error as the list does not exist

foodList = ['Vadapav','Pizza','Dabeli','Panipuri','Burger','Dosa','Salad']
restaurantList = ['PizzaHut','Dominos','Hocco','Subway','McDonalds','KFC']

#To print Merged two lists
print(restaurantList + foodList)

#To add a list to another list .extend(list)
restaurantList.extend(foodList)
print(restaurantList)