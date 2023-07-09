#!/usr/bin/python3
def mad_libs():
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")

    mad_lib = f"{name} went to {place} and saw a {adjective} {noun} {verb}!"
    print(mad_lib)

mad_libs()
