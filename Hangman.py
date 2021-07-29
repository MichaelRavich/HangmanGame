import colorsys
# The purpose of the program is to implement the Hangman game
# by working with a file and interacting with the user


def choose_word(file_path, index):
    """
    This function returns the word in the specific index from the file
    :param file_path: the path to the words file
    :param index: index of the specific word that chosen to be the secret word
    :return: secret word (type: string)
    """
    num_of_diff_words = 0
    update_index = int(index)
    secret_word = ""
    with open(file_path, "r") as source_file:
        source_temp = source_file.read()
    source_tuple = tuple(map(str, source_temp.split(" ")))
    for word in source_tuple:                           # can be DELETED
        if source_tuple.count(word) == 1:  # can be DELETED
            num_of_diff_words += 1  #add one to the different words counter # can be DELETED

    if (int(index) > len(source_tuple)):
        update_index = int(index) % len(source_tuple)
    secret_word = source_tuple[update_index-1]
    returned_tuple = (num_of_diff_words, secret_word)
    return returned_tuple[1]
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function uses check_valid_input to check the input,
    if its un-valid the func will announce about it,
    print the already guessed letters till here, and return False.
    otherwise, the function will add the letter to the guessed list and return True.
    :param letter_guessed: the guessed letter by user (type: string)
    :param old_letters_guessed: list of all the guessed letters till now
    :return: Boolean value.
    """
    old_letters_guessed_temp = old_letters_guessed  # temp_str for the join method
    old_letters_guessed.sort()
    old_letters_guessed_str = ' -> '.join(old_letters_guessed_temp)
    old_letters_guessed_str.lower()
    print("Already guessed letters:\t")
    print(old_letters_guessed_str)
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True  # append succeed
    else:
        print("X\n (The char isn't a letter or is already guessed!)\n")
        return False
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The func will check if the input is valid and will store the old guesses
    :param letter_guessed: the guessed letter by user (type: string)
    :param old_letters_guessed:  list of all the guessed letters till now
    :return: Boolean Value
    """

    guessed_letter = letter_guessed
    guessed_letter = letter_guessed.lower()
    if (guessed_letter < 'a' or guessed_letter > 'z'):
        return False
    if (len(guessed_letter) > 1):
        return False
    if(guessed_letter in old_letters_guessed):
        return False
    return True
def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function will show the hidden word - a string which consists of letters and underlines,
    so that the letters are from the old_letters_guessed list that are in the secret_word string in their matching index,
     and the rest of the letters in the string (which the player has not yet guessed) as underlines.
    :param secret_word: The secret word that need to be checked (type:string)
    :param old_letters_guessed: list of all the guessed letters till now (type: list)
    :return: None (default)
    """
    show_word = ""
    for char in secret_word:
        if(char in old_letters_guessed):
            show_word += char + " "
        else:
            show_word += " _ "
    print(show_word)
    
    
def check_win(secret_word, old_letters_guessed):
    """
    The function will check if all the secret word letters included in the guessed letters - if so, returns True.
    otherwise - False.
    :param secret_word: The secret word that need to be checked (type:string)
    :param old_letters_guessed:  list of all the guessed letters till now
    :return: Boolean value as described.
    """
    counter = 0
    for char in secret_word:
        if (char in old_letters_guessed):
            counter += 1
    if (counter == len(secret_word)):
        return True
    else:
        return False
def welcome_screen():
    """
    The function will print the welcome screen and the number of allowed attempts
    :return: None     (Default value)
    """

    HANGMAN_ASCII_ART = "Welcome to the Hangman Game!" + """                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n"""
    print("\033[1;36;40m")    # print the output of all the program in Bright Cyan color
    print(HANGMAN_ASCII_ART, "6")



def main():
    MAX_TRIES = 7  # the maximum of allowed tries in the game
    cnt_mistake = 1 # to count number of wrong guesses & iterator for the while loop
    welcome_screen()
    words_file = input("Please enter the path for the words file: \n")
    index_of_secret_word = input("Please enter an index for the secret word:\n")
    secret_word = ""  # the word that the player should guess
    old_letters_guessed = []  # list of all the guessed letters
    num_of_tries = 0 # how many attempts till now
    HANGMAN_PHOTOS = {}  # new dictionary
    HANGMAN_PHOTOS[1] = """        x-------x"""
    HANGMAN_PHOTOS[2] = """
        x-------x
        |
        |
        |
        |
        |
                        """
    HANGMAN_PHOTOS[3] = """ 
        x-------x
        |       |
        |       0
        |
        |
        |"""
    HANGMAN_PHOTOS[4] = """
        x-------x
        |       |
        |       0
        |       |
        |
        |"""
    HANGMAN_PHOTOS[5] = """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |"""
    HANGMAN_PHOTOS[6] = """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |"""
    HANGMAN_PHOTOS[7] = """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""

    secret_word = choose_word(words_file, index_of_secret_word)
    print(HANGMAN_PHOTOS[1])
    show_hidden_word(secret_word, old_letters_guessed)
    while cnt_mistake < MAX_TRIES:
        Flag = True
        while Flag:
            char_guessed = input("Please guess a letter: \n")
            char_guessed = char_guessed.lower()
            if try_update_letter_guessed(char_guessed, old_letters_guessed):
                show_hidden_word(secret_word, old_letters_guessed)
                Flag = False
                if char_guessed not in secret_word:  # if the letter isn't in the secret word
                    cnt_mistake += 1
                    print("): \n")
                    print(HANGMAN_PHOTOS[cnt_mistake])

        if check_win(secret_word, old_letters_guessed):
            print ("WIN! Well done!")
            break
        if cnt_mistake == MAX_TRIES:
            print("LOSE! You have run out of attempts")
            break


if __name__ == "__main__":
    main()
