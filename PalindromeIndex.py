#QUESTION DESCRIPTION

# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be
# removed to make the string a palindrome. There may be more than one solution, but any will do. If the word
# is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to
# remove.

#LET'S SOLVE IT

# The function accepts STRING s as parameter.

def palindromeIndex(s):

    list_s = list(s)

    # As first step let's define a function that checks if a list is a palindrome

    def is_palindrome(lis):
        return list == list(reversed(lis))

    # If the string is already a palindrome:

    if is_palindrome(lis):
        return -1


    n = len(list_s)
    for i in range(n):
        if list_s[i] != list_s[n-i-1]:
            if is_palindrome(lista_s[:i] + lista_s[i+1:]):
                return i
            elif is_palindrome(lista_s[:n-i-1] + lista_s[n-i:]):
                return n-i-1
            else:
                return -1
