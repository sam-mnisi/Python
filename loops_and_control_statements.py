#control statements when using loops include break, continue, pass

#for loop
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # exits the loop if cherry is found, won't display cherry or any string after
    print(fruit)
    
print()
    
for fruit in fruits:
    if fruit == "cherry":
        continue # skips cherry and moves to the next iteration
    print(fruit) 
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass # can be used when altering data. It's a placeholder, no action is needed for cherry. So when doing alteration it would change all specified data except for cherry hence "pass", here it returns it as is since alterations are done
    print(fruit) 

print()   
#while loop

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #exits the loop when the count is reached in this case 3.
    
    #continue and pass follow the same sentiment (will test later)