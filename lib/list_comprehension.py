#!/usr/bin/env python3

def return_evens(num_list):
    new_list = list()
    new_list = [num_list[n] for n in range(len(num_list)) if num_list[n] % 2 == 0]
    return new_list

def make_exclamation(sentence_list):
    new_list = list()
    new_list = [sentence_list[n] + '!' for n in range(len(sentence_list))]
    return new_list
