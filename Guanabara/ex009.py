thisSet = {'apple', 'banana', 'pear', 'watermelon', 'banana'}

otherSet = {'apple', 'pear', 'watermelon', 'banana', 'strawberry', 'grape'}

oneList = ['apple', 'strawberry', True, True]

finalSet = thisSet.union(otherSet)

thisSet.intersection_update(otherSet)

interSet = thisSet.intersection(otherSet)

#thisSet.symmetric_difference_update(otherSet)

symSet = thisSet.symmetric_difference(otherSet)

print(symSet)