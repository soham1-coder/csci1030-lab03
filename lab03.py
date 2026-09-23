# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):

    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return word + "way"
    
    else:
        new_word = word[1:] + word[0] + "ay"
        return new_word


def word_lengths(sentence):
    
    sentence = sentence.split()
    lengths = []

    for word in sentence:   

        lengths.append(len(word))   

    return lengths


def reverse_words(sentence):

    sentence = sentence.split()
    reverse = ""

    for word in range(len(sentence)-1,-1,-1):  

        reverse = reverse + " " + (sentence[word])   

    return reverse


def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    #print(pig_latin("banana"))                    # ananabay
    #print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    #print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
