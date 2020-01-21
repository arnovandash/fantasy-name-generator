consonant=('b','g','d','t','f','c','h','m','n','p','h','r','l','s','g','k','x','z','ph','sh','ch')
vowel=('a','e','i','o','u','y')

import random

def SetRnd(name, count): #returns random letter, whether consonant or vowel
    IsValid = False
    while IsValid == False:
        if str(random.randint(1,2)) == "1":
            chosenChar = str(random.choice(consonant))
            IsValid = True
        else:
            chosenChar = str(random.choice(vowel))
            #checks whether the chosen char (vowel) is different to previous
            if (count > 0) and (str(chosenChar) != str(name[count-1])):
                IsValid = True
    return chosenChar

def name_gen(length):
    name=[] #create blank list
    count=0 #sets length counter to 0
    while (count < length):
        if (count == length - 1): #if at final position
            if (name[count-1] in consonant): #if penultimate letter is consonant, finish with vowel! eg. -og
                name.insert(count, random.choice(vowel))
            else: #if penultimate letter is vowel, however, consider the pre-penult letter, eg. -[]o[]
                if (name[count-1] in vowel): #if pre-pen letter is vowel, finish with consonant! eg. -oog
                    name.insert(count, random.choice(consonant))
                else: #if pre-pen is consonant, finish with either! eg. -gog
                    name.insert(count, SetRnd(name, count))
        else: #if not at final position, work as normal
            if (count == 0): #if even -1 doesn't exist (eg like in the beginning), set to either
                name.insert(count, SetRnd(name, count))
            else: #otherwise, run as normal
                if (name[count-1] in consonant): #if -1 is consonant, see -2; eg. -[]g[]-
                    if (count == 1): #if -2 doesn't exist, set to vowel, eg. |go-
                        name.insert(count, random.choice(vowel))
                    else:
                        if (name[count-2] in consonant): #if -2 is consonant, set vowel, eg. -ggo-
                            name.insert(count, random.choice(vowel))
                        else: #if -2 is vowel, set to either, eg. -ogo-, -ogg-
                            name.insert(count, SetRnd(name, count))
                else: #if -1 is vowel, see -2; eg. -[]o[]-
                    if (count == 1): #if -2 doesn't exist, set to consonant, eg. |og-
                        name.insert(count, random.choice(consonant))
                    else:
                        if (name[count-2] in consonant): #if -2 is consonant, set to either, eg. -gog-, -goo-
                            #make sure that generated vowel <> -1!
                            name.insert(count, SetRnd(name, count))
                        else: #if -2 is vowel, set to consonant, eg. -oog-
                            name.insert(count, random.choice(consonant))
        count = count + 1
    return ''.join(name).title()

def run():
    while True:
        input("Hit enter to generate a name...")
        len_first=random.randint(2, 8)
        len_last=random.randint(2, 8)
        first = name_gen(len_first)
        last = name_gen(len_last)
        print("{} {}\n".format(first, last))

if __name__ == "__main__":
    run()
