#!/usr/bin/python3
print('Mad Libs Generator')
print('---------------------------')

# Questions for the user to answer
adjective1 = input('Choose an adjective: ')
noun1 = input('Choose a noun: ')
verb = input('Choose a verb: ')
adjective2 = input('Choose another adjective: ')
noun2 = input('Choose another noun: ')
place = input('Name a place: ')
verb_past_tense = input('Choose a verb in past tense: ')
adjective3 = input('Choose one more adjective: ')

# Print a story from the user input
print('---------------------------')
print('Once upon a time, there was a', adjective1, noun1, 'who loved to', verb, '.')
print('The', adjective2, noun2, 'joined in the adventure and they went to', place, '.')
print('They', verb_past_tense, 'through the', adjective3, 'landscape and had a great time.')
print('---------------------------')
