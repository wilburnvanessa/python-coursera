fruit_to_colour ={
    'plum': 'purple',
    'watermelon': 'green',
    'banana': 'yellow',
    'pomegranate': 'red',
    'peach': 'orange',
    'orange': 'orange',
    'pear': 'green',
    'cherry': 'red'}

# Invert fruit_to_colour.
colour_to_fruit = {}
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
##    colour_to_fruit[colour] = fruit
    # If colour is not already a key in the accumulator,
    # add colour: [fruit] as an entry.
    if not (colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]

    # Otherwise, append fruit to the existing list.
    else:
        colour_to_fruit[colour].append(fruit)

    
