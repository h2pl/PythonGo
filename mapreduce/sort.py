sorted([36, 5, -12, 9, -21])
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'])

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)