import time
import collections
words = []
possible = []
letters = []
rem = []
positions = []
known = 0

#here on down 'words' is the list of all words, do not change it, make new lists that are smaller
#with open(r"C:\Users\Jerry\Desktop\code\google-10000-english-master\google-10000-english-master\20k.txt","r") as file:
with open(r"words.txt","r") as file:
    for line in file:
        words.append(line.strip("\n"))

long = int(input("How many letters is the word? "))

#makes list of all word strings of given length
for word in words:
    if len(word) == long:
        possible.append(word.lower())

#prints most common letters in list of possible words
def best_letters():
    for word in possible:
        for char in word:
            letters.append(char.lower())
    c = collections.Counter(letters)
    print(c.most_common(10))
    del c
    letters.clear()

#takes new known letter and updates possible list
def new_letter(letter):
    for word in possible:
        for p in positions:
            if word[p-1] != letter and word not in rem:
               rem.append(word)
    for e in rem:
        possible.remove(e)
    rem.clear()
    positions.clear()
        
while known != long:
    best_letters()
    l = str(input("What is the new letter?"))
    prompt = input("What position is the new letter in?")
    positions.append(int(prompt))
    while True:
        prompt = input("Are there any other positions the letter appears in? If no, type 'n'.")
        if prompt == 'n':
            break
        else:
            positions.append(int(prompt))
    print(positions)
    new_letter(l)
    print(possible)
    
print("Solved!")
time.sleep(500)






















