import re
import random


if __name__=='__main__':

    greeting = open("greeting.txt", "r")
    content = greeting.read()
    print(content)

    words = open("words.txt", "r")
    content = words.read()
    content = content.replace("[", "")
    content = content.replace("]", "")
    content = content.replace("\"", "")
    content = content.split(",")


    print("Enter 5 letter word: \n")
    turns = 1
    ans= content[random.randint(0,len(content)-1)]
    letters = {}
    for x in ans:
        if x in letters:
            letters[x]+=1
        else:
            letters[x]=1
    print(letters)
    non_letters=[]
    correct=[]
    place=[]
    guess=["_", "_", "_", "_","_"]
    while turns <=6:
        print(turns)
        word = input("--> ")

        if not re.match("^[a-z]*$",word) or not len(word)==5 or word not in content:
            print("Error! Word must be a-z, 5 characters long, and a valid word")
            print("---------------------------------------")

        else:
            i=0
            while i < 5:
                if word[i] == ans[i]:
                    if guess[i] == "_":
                        guess[i]=word[i].upper()
                        #correct.append(word[i].upper())
                        letters[word[i]]-=1
                        if word[i] in correct and letters[word[i]] == 0:
                            correct.remove(word[i])
                elif word[i] in ans:
                    if word[i] not in correct and letters[word[i]]>0:
                        correct+=word[i]
                    elif word[i] in correct and letters[word[i]]==0:
                        correct = [y for y in correct if y != word[i]]
                    else:
                        pass
                elif word[i] not in ans:
                    #guess+="_"
                    if word[i] not in non_letters:
                        non_letters.append(word[i])
                i+=1

            print(*guess)
            print("These letters are not there: ", non_letters)
            print("These letters are in the wrong place:", correct )
            print("---------------------------------------")
            if '_' not in guess:
                print("CONGRATS U GOT IT!!")
                break
            turns+=1
