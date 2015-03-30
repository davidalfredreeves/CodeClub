# Problem 16 - Pig Latin Translator

def toPig(word):
    if word == "":
        return word
    elif len(word) == 1:
        return word + "yay"
    else:
        return translate(word)

def translate(word):
    firstvowel = findVowel(word)
    prefix = word[0:firstvowel]
    stem = word[firstvowel:]
    word = stem + prefix + "ay"
    return word.title()

def findVowel(word):
    firstvowel = 0
    for i in range(0, len(word)):
        if word[i].upper() == "A":
            firstvowel = i
            return firstvowel
        elif word[i].upper() == "E":
            firstvowel = i
            return firstvowel
        elif word[i].upper() == "O":
            firstvowel = i
            return firstvowel
        elif word[i].upper() == "I":
            firstvowel = i
            return firstvowel
        elif word[i].upper() == "Y":
            firstvowel = i
            return firstvowel
        elif word[i].upper() == "U":
            firstvowel = i
            return firstvowel
        elif word[i] == "!":
            firstvowel = i
            return firstvowel

def pigLatin(sentence):
    newSentence = ""
    sentenceList = []
    newSentenceList = []
    sentenceList = sentence.split(" ")
    for each in sentenceList:
        newSentenceList.append(toPig(each))
    for each in newSentenceList:
        newSentence += each + " "
    return newSentence

##print toPig("Same")
##print "Expected: amesay"
##print toPig("Because")
##print "Expected: ecausebay"
##print toPig("Rythym")
##print "Expected: ythymray"

print ("I am a cat!")
print (pigLatin("I am a cat!"))
print ("Expected: 'Iyay maay ayay atcay!'")
print ("MEAT is good for you.")
print (pigLatin("MEAT is good for you."))
print ("Expected: 'EATMAY isay oodgay orfay youay.'")
print ("But aren't lions dangerous?")
print (pigLatin("But aren't lions dangerous?"))
print ("Expected: 'Utbay aren'tay ionlay angerousday?'")
