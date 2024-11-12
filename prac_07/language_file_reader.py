import csv
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year,PointerArithmetic
        in_file.readline()  # 'Consume' the first line (header) - we don't need its contents
        
        # All other lines are language data
        for line in in_file:
            parts = line.strip().split(',')
            # Reflection and PointerArithmetic are stored as strings (Yes/No) and need to be converted to Booleans
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            # Construct a ProgrammingLanguage object using the elements
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            # Add the language we've just constructed to the list
            languages.append(language)
    
    # Display all languages (using their str method)
    for language in languages:
        print(language)


main()
