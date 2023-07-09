## Mad Libs Generator Project
# This MLG project enhances the use of Strings, Variables and Concatenation.
* The Mad Libs Generator gathers and manipulates user input data as an adjective, a pronoun, and a verb.
* The program takes this data and arranges it to build a story.

# Terminologies Used
* Here's a breakdown of the code line by line:

* `def mad_libs():`: This line defines a function called `mad_libs` without any parameters. This function will generate the Mad Libs sentence based on user inputs.

*  `noun = input("Enter a noun: ")`: This line prompts the user to enter a noun and stores the input in the `noun` variable.

*  `verb = input("Enter a verb: ")`: This line prompts the user to enter a verb and stores the input in the `verb` variable.

*  `adjective = input("Enter an adjective: ")`: This line prompts the user to enter an adjective and stores the input in the `adjective` variable.

*  `adverb = input("Enter an adverb: ")`: This line prompts the user to enter an adverb and stores the input in the `adverb` variable.

*  `mad_lib = f"The {adjective} {noun} {verb} {adverb}."`: This line constructs the Mad Libs sentence using the user inputs. The sentence is formed by combining the values of `adjective`, `noun`, `verb`, and `adverb` using an f-string.

*  `print(mad_lib)`: This line prints the generated Mad Libs sentence to the console.

*  `mad_libs()`: This line calls the `mad_libs` function, starting the execution of the Mad Libs generator.

## When you run the code, it will prompt you to enter a noun, verb, adjective, and adverb. After you provide the inputs, it will construct a sentence using those inputs and print it out.
