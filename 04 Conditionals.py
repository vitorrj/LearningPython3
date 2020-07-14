### Comparing two values
print(5 != 6)       # True
print(5 == 5)       # True

### Using logical operators
number = 6
print(number>0 and number<4)            # False
print(number%2 == 0 or number%10 == 0)  # True

### Check if an elements is IN a list
mylist = [1,2,3]
mystring = "Vitor"
print(5 in mylist)          # False because 5∉ mylist
print("K" not in mylist)    # True

### if and else
x = 7

if int(x)%2 == 0:
    print("x is even")
else:
    print("x is odd")

### Using Elif instead of nested if and else
print("\n")
x = 10
y = 12

if x > y:
    print("x is bigger than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x is equal to y")




### Exercise 1
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = [0] * len(percent_rain)
count = 0

for percentage in percent_rain:
    if percentage > 90:
        resps[count] = "Bring an umbrella."
        count += 1
    elif percentage > 80:
        resps[count] = "Good for the flowers?"
        count += 1
    elif percentage > 50:
        resps[count] = "Watch out for clouds!"
        count += 1
    else:
        resps[count] = "Nice day!"
        count += 1
print(resps)


percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for percentage in percent_rain:
    if percentage > 90:
        resps.append("Bring an umbrella.")
    elif percentage > 80:
        resps.append("Good for the flowers?")
    elif percentage > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")

print(resps)

