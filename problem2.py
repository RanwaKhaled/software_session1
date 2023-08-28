#Problem 2: Coleman - liau formula
import string
OGstring = input('enter your string: ')

#to count words
words = OGstring.split()
wordCount = len(words)

#to count letters
#1- remove punctuation
letters=OGstring.translate(str.maketrans('','',string.punctuation))
#2-remove spaces
letters = letters.replace(" ","")
letterCount = len(letters)

#to count sentences
sentenceCount = 0
for i in OGstring:
    if i == '.' or i == '!' or i == '?':
        sentenceCount += 1

print(f"the sentence has {letterCount} letters, {wordCount} words and {sentenceCount} sentences")
#the colman-liau formula
L = float(letterCount/wordCount)*100
S = float(sentenceCount/wordCount)*100

grade = round((0.0588*L)-(0.296*S)-15.8)
if(grade<1):
    print('Below grade 1')
elif(grade>=16):
    print('Grade 16+')
else:
    print(f'Grade {grade}')