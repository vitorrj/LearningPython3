### RANGE
number = list(range(1,11))
print(number)

for i in range(5):
    print(i)               # 0 1 2 3 4


# | ------------------ |
# | ------- FOR ------ |
# | ------------------ |

for _ in range(3):
    print("Hello, Vitor!")

##### Printing a list
myParty = ["Vitor", "Marghie", "Seba", "Giuseppe"]

for name in myParty:
    print("Hey", name, "you have been invited to my party")

#### Printing a  string
name = "Vitor Rodrigues"
i = 0
for letter in name:
    print(letter)                       # V i t o r R o d r i g u e s
    i+=1
print("There are", i, "letters")

#### Check lenght of a string without len()
str1 = "Vitor Rodrigues"
numbs = 0
for _ in str1:
    numbs += 1
print(numbs)

# | ------------------ |
# | ------ WHILE ----- |
# | ------------------ |
print("----- While -----")

x = 1
while x <= 3:
    print(x)
    x += 1

### break and continue
while x < 10:
    if x%2 == 0:
        x += 2
        print(x)
        continue

