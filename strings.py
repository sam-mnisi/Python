
messageone = 'Hey' #single quotes
messagetwo = "Hey" #double quotes
messagethree = " Mom's favorite show " #double qoutes with apostrophe
messagefour = """Mom's 
favorite show""" #displaying string in different lines, you use three pairs od double quotes and enter text into the next line

print(messageone)
print(messagetwo)
print(messagethree)
print(messagefour)

#advanced concepts in strings
messagefive = "Hello"
print(messagefive[0]) #print position 0, 0 being the first letter of the string
print(messagefive[1]) #second letter in the string
print(messagefive[2]) #third
print(messagefive[3]) #fourth
print(messagefive[4]) #last letter in the string
print(messagefive[-1]) #also displays the last letter in the string
print(len(messagefive)) #length of string, counts everything within string, including spaces, symbols, e.t.c

#python build-in methods for string manipulation
print(messagethree.strip()) #Removes leading(beg) and trailing(end) whitespace
print(messagethree.lower()) #converts all char to lowercase
print(messagethree.lower().strip()) #does both of the above -strip and lowercase
print(messagethree.upper()) #char to uppercase
print(messagethree.split("'")) #split the string into a list based on the symbol e.g apostrophe, comma e.t.c
print(messagetwo.replace('e', 'a')) #replace e with a
print(messagethree.replace('o', 'w', 2)) #replaces o with w in 2 occurances, default is all occurences

#operators on strings
string1 = 'Invest'
string2 = 'today'

print(string1 + " "+ string2) #concationatio joins 2+ strings together
print(string1 * 4) #multiplies text 4 times