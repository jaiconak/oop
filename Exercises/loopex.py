'''
Write a script  that will ask for a string and tell if a letter is a vowel or a Consonants

'''

wordInput = input("Input a word for analysis for vowel or Consonants: ")
vowel = ['a','e', 'i', 'o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
collectionVowel = set()
collectionConsonants = set()
countVowel = 0
countCo = 0

# for i in wordInput :
#     if i in vowel :
#         collectionVowel.add(i)
#     if i in consonants:
#         collectionConsonants.add(i)
# print("These are the findings")
# print (f"Consonants: {collectionConsonants}")
# print (f"Vowels:  {collectionVowel}")



for i in wordInput :
    if i in vowel :
        # print(f"{i} are the vowels in the word")
        collectionVowel.add(i)
        countVowel +=1
    elif i in consonants :
        # print (f"{i} are the consonants in the word")
        collectionConsonants.add(i)
        countCo +=1
print(f"The total amount of vowels used: {countVowel} , These are the vowels used: {collectionVowel}")
print(f"The total amount of consonants used: {countCo}, These are the consonants used{collectionConsonants}")

