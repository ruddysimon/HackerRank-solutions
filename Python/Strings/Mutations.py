def mutate_string(string, position, character):
    word = list(string)
    # print(word)
    word[position] = character
    string = ''.join(word)
    return(string)