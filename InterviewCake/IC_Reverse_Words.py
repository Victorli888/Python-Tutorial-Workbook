"""You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major
European National Cake Vault. The message has been mostly deciphered, but all the words are backward!
Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and
reverses the order of the words in place. ↴"""


# Create Reverse Method
def Reverse(alist):
    # pointers
    left = 0
    right = len(alist)-1

    # reverse the list items
    while left < right:
        temp = alist[left]
        alist[left] = alist[right]
        alist[right] = temp

    # in and decrement pointers
        left += 1
        right -= 1
    return alist

def Reverse_characters(string):
    separated_word_list = [character for character in string]
    R_separated_word_list = Reverse(separated_word_list)
    reversed_phrase = ''.join(R_separated_word_list)
    return reversed_phrase


encoded = "sdrawkcab nettirw ma I"
decoded = Reverse_characters(encoded)
print(decoded)

