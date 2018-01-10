'''
Created on 2018. 1. 10.

Number letter counts
Problem 17 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer 21124

@author: sharb
'''

def num_to_word(num):
    words = ['and', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']

    n = num.__str__()
    word_len = n.__len__()

    if word_len == 1 or num < 21:
        return words[int(num)]
    elif word_len == 2:
        if num < 30:
            return words[20] + num_to_word(n[-1])
        elif num == 30:
            return words[21]
        elif num < 40:
            return words[21] + num_to_word(n[-1])
        elif num == 40:
            return words[22]
        elif num < 50:
            return words[22] + num_to_word(n[-1])
        elif num == 50:
            return words[23]
        elif num < 60:
            return words[23] + num_to_word(n[-1])
        elif num == 60:
            return words[24]
        elif num < 70:
            return words[24] + num_to_word(n[-1])
        elif num == 70:
            return words[25]
        elif num < 80:
            return words[25] + num_to_word(n[-1])
        elif num == 80:
            return words[26]
        elif num < 90:
            return words[26] + num_to_word(n[-1])
        elif num == 90:
            return words[27]
        elif num < 100:
            return words[27] + num_to_word(n[-1])
    elif word_len == 3:
        if num%100 == 0:
            return num_to_word(n[0]) + words[28]
        else:
            return num_to_word(n[0]) + words[28] + words[0] + num_to_word(int(n[1:]))
    elif word_len == 4:
        return 'onethousand' # not going to implement due to not needed for challenge

sumNum = 0
for i in range(1, 1001):
    word = num_to_word(i)
    sum += word.__len__()
    # print word # debugging to make sure numbers are done right

print(sumNum)
