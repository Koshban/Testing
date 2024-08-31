'''
Write a function for doing an in-place ↴ shuffle of a list.
The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.
Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
'''

import random


def get_random(floor, ceiling) -> int:
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list : list[int]) -> list[int]:
    if len(the_list) <= 1:
        return the_list
    
    last_index = len(the_list) -1

    for index_of_list_weare_shuffling in range(0, last_index):
        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_of_list_weare_shuffling, last_index)

        if random_choice_index != index_of_list_weare_shuffling:
            the_list[index_of_list_weare_shuffling], the_list[random_choice_index]  = the_list[random_choice_index], the_list[index_of_list_weare_shuffling]
    
    return the_list