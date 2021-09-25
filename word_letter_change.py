#Code to change any letter in a "GIVEN WORD" to any other "CHARACTER"
word=input("Enter any word : ")
print("\n>>>> Enterd word is : ", word,  "\n")
word_use=word.lower()

change=input("Type the letter in the word you want to change (not case sensitive ) : ")
change=change.lower()
print("\n>>>> character to change is : ", change,  "\n")

put=input("Type the character than you want to change to : ")
print("\n>>>> letter :- " + change +" ..... [+] will be changed to > ", put,  "\n")

instances = input("Do you want to changes all instances of the letter in the word ? (y/n) \n>>> ")
instances_use = instances.lower()

# print(instances_use)

# *****************************************************************************************
letters=[]
for i in word_use:
    letters.append(i)
#print(letters)
# *****************************************************************************************

# *****************************************************************************************
try:
    change in letters
except:
    print("[-] Letter Not Found; Give a letter in the word :",change,"not in",word_use)
    quit()
# *****************************************************************************************

# *****************************************************************************************
word_instances=list()
count=0
for i in letters:
    if i == change:
        word_instances.append(count)
    count+=1
# *****************************************************************************************

if instances_use == "y":

    print("\n>>>> [+ ]All instances of the letter ", change, "will be changed to ", put)
    
    for each in range(len(letters)):
        if letters[each]==change:
            letters[each]=put
    final= ''.join(letters)
    final=str(final)
    print("\n>>>>>>> The final changed word is :- " + final.capitalize())
    exit

elif instances_use == "n":

    print("\n>>>> The index positions of the selected character are :- >>> ", end="")
    print(word_instances)

    index=input("\nPlease enter the position(s)/Index(s) of the character that you want to change; [?] index position table given above. [+] SEPERATE position(s)/Index(s) WITH ANY CHARACTER eg:-(1 2 or 1,2)  :> ")
    # index=int(index)

    print("\n>>>> [+] The " , index , "th instance(s) of the letter ", change, " .... [+] will be changed to", put)

    temp=list(index)
    #print(temp)
    index_multi_add=[]
    for i in range(len(temp)):
        # print(i)
        if i%2==0:
            index_multi_add.append(temp[i])
    #print(index_multi_add)

    temp_list=list(word_use)
    for indx in index_multi_add:
        temp_list[int(indx)]=put
    final= ''.join(temp_list)
    final=str(final)
    print("\n>>>>>>> The final changed word is :- " + final.capitalize())
    exit


else :
    print("Please give the correct option and try again")

#print(letters)

# def print_name():

#     for i in letters:
#         print(i,end="")

# print("\n>>>>>>> The final changed word is :- ", end="")
# print_name()

# res= ''.join(letters)
# print("\n>>>>>>> The final changed word is :- " + str(res))
