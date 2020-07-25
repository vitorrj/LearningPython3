overal_score = [(3, 0, 0, 0, 0), (1, 0, 2, 2, 0), (1, 2, 1, 0, 1), (3, 1, 1, 0, 1), (6, 0, 2, 0, 2), (9, 5, 2, 0, 2), (19, 0, 2, 0, 2), (0, 0, 0, 3, -3), (0, 0, 0, 2, -2), (82, 2, 4, 0, 4), (0, 0, 0, 1, -1), (0, 0, 1, 0, 1), (47, 0, 1, 0, 1), (2, 1, 1, 0, 1), (0, 2, 1, 0, 1), (0, 0, 2, 1, 1), (4, 6, 3, 0, 3), (19, 0, 2, 1, 1), (0, 0, 1, 1, 0)]

myfile = open("resulting_data.csv", 'w')
myfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')    # Create heading

for value in overal_score:
    valueInString = '{}, {}, {}, {}\n'.format(value[0], value[1], value[2], value[3])
    myfile.write(valueInString)

myfile.close()