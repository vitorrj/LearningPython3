path = "assets/grades.csv"

mycsv = open(path, 'r')
csvlines = mycsv.readlines()
print(csvlines)

# reading data
for line in csvlines[1:]:
    characters = line.strip().split(',')
    print("{} | {} | {}".format(characters[0], characters[1], characters[2]))

