def word_count():
    """
    This program counts the occurrences of each word in a given string input by the user.
    Time estimate: 30 minutes.
    """
    # Get input from the user
    user_input = input("Text: ")

    # Split the input into words and create a dictionary to count occurrences
    words = user_input.split()
    word_count_dict = {}

    for word in words:
        # Normalize words to lower case to count them case-insensitively
        word = word.lower()
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    # Sort the dictionary by keys (words)
    sorted_word_count = sorted(word_count_dict.items())

    # Determine the longest word for formatting
    max_length = max(len(word) for word in word_count_dict)

    # Print the word counts with aligned output
    for word, count in sorted_word_count:
        print(f"{word:{max_length}} : {count}")


# Call the function
word_count()
