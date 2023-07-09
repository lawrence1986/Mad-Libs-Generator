def mad_libs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    mad_lib = f"The {adjective} {noun} {verb} {adverb}."
    print(mad_lib)

mad_libs()
