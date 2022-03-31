import re


if __name__=='__main__':

    greeting = open("greeting.txt", "r")
    content = greeting.read()
    print(content)

    words = open("words.txt", "r")
    content = words.read()


    print("Enter 5 letter word: \n")
    turns = 1
    ans="sushi"
    letters = {}
    for x in ans:
        if x in letters:
            letters[x]+=1
        else:
            letters[x]=1
    print(letters)
    non_letters=[]
    correct=[]
    while turns <=6:
        print(turns)
        word = input("--> ")

        guess=""
        if not re.match("^[a-z]*$",word) or not len(word)==5 or word not in content:
            print("Error! Word must be a-z, 5 characters long, and a valid word")
            print("---------------------------------------")

        else:
            i=0
            while i < 5:
                if word[i] == ans[i]:
                    guess+=word[i].upper()
                    correct.append(word[i].upper())
                    letters[word[i]]-=1
                elif word[i] in ans:
                    if word[i].upper() in correct or letters[word[i]]>0:
                        guess+=word[i]
                    else:
                        guess+="_"
                elif word[i] not in ans:
                    guess+="_"
                    if word[i] not in non_letters:
                        non_letters.append(word[i])
                i+=1

            print(guess)
            print("These letters are not there: ", non_letters)
            print("---------------------------------------")
            if guess == ans.upper():
                print("CONGRATS U GOT IT!!")
                break
            turns+=1
