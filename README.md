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

* When you run the code, it will prompt you to enter a noun, verb, adjective, and adverb. After you provide the inputs, it will construct a sentence using those inputs and print it out.

## mlb2.py has same concept as mad_libs_gen.py

## mlb3 script is explained below
Here's a breakdown of the code for mlb3.py line by line:

* `print('Mad Libs Generator')`: This line simply prints the title of the Mad Libs generator to the console.

* `print('---------------------------')`: This line prints a horizontal line separator for visual separation.

* `adjective1 = input('Choose an adjective: ')`: This line prompts the user to enter an adjective and stores the input in the variable `adjective1`.

* `noun1 = input('Choose a noun: ')`: This line prompts the user to enter a noun and stores the input in the variable `noun1`.

* `verb = input('Choose a verb: ')`: This line prompts the user to enter a verb and stores the input in the variable `verb`.

* `adjective2 = input('Choose another adjective: ')`: This line prompts the user to enter another adjective and stores the input in the variable `adjective2`.

* `noun2 = input('Choose another noun: ')`: This line prompts the user to enter another noun and stores the input in the variable `noun2`.

* `place = input('Name a place: ')`: This line prompts the user to enter a place and stores the input in the variable `place`.

* `verb_past_tense = input('Choose a verb in past tense: ')`: This line prompts the user to enter a verb in the past tense and stores the input in the variable `verb_past_tense`.

* `adjective3 = input('Choose one more adjective: ')`: This line prompts the user to enter one more adjective and stores the input in the variable `adjective3`.

* `print('---------------------------')`: This line prints another horizontal line separator for visual separation.

*  The following lines construct the story using the user's inputs. Each line uses the `print()` function to display a sentence or phrase that incorporates the user's inputs. The story is formed by combining the strings and variables using commas. The story is printed to the console.

* `print('---------------------------')`: This line prints a final horizontal line separator for visual separation.

When you run the code, it will prompt you to enter various words to fill in the blanks of the story. After you provide the inputs, the program will construct the story using your inputs and print it out to the console.
