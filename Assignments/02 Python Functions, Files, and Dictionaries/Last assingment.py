# EXERCISE 1

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
   print(word)
   for ch in punctuation_chars:
       word = word.replace(ch, '')
   return word




# EXERCISE 2
# punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for ch in punctuation_chars:
        word = word.replace(ch, '')
    return word


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(words):
    count = 0
    list_words = words.split()
    for word in list_words:
        word = strip_punctuation(word)
        lower_word = word.lower()
        if lower_word in positive_words:
            count += 1
    return count

# EXERCISE 3


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for ch in punctuation_chars:
        word = word.replace(ch, '')
    return word


def get_neg(word):
    list_words = word.split()
    count = 0
    for word in list_words:
        word = strip_punctuation(word)
        word = word.lower()
        if word in negative_words:
            count += 1
    return count




# LAST EXERCISE


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# FUNCTIONS CREATED BY ME

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '\n']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# ----- FUNCTIONS CREATED BY ME -----

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '\n']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# ----- FUNCTIONS CREATED BY ME -----
def strip_punctuation(word):
    for ch in punctuation_chars:
        word = word.replace(ch, '')
    return word


def get_pos(words):
    count = 0
    list_words = words.split()
    for word in list_words:
        word = strip_punctuation(word)
        lower_word = word.lower()
        if lower_word in positive_words:
            count += 1
    return count


def get_neg(word):
    list_words = word.split()
    count = 0
    for word in list_words:
        word = strip_punctuation(word)
        word = word.lower()
        if word in negative_words:
            count += 1
    return count


def remove_n(word):
    word.replace('\n', '')
    return int(word)


# Declaration
myfile = open("project_twitter_data.csv", 'r')
overal_score = []
lines = myfile.readlines()
del lines[0]  # delete header
index = 0  # index of my lines

# ------ READING TWEETS -----
for tweet in lines:
    count_pos = get_pos(tweet)
    count_neg = -get_neg(tweet)

    tweet_list = tweet.split(',')
    print(tweet_list)

    number_rt = int(tweet_list[1])
    number_re = remove_n(tweet_list[2])  # remove \n and covert to int
    tupple = (number_rt, number_re, count_pos, count_neg, count_pos + count_neg)
    overal_score.append(tupple)

    # Printing values
    print(count_pos)
    print(count_neg)
    print(overal_score[index])
    index += 1

# ----- WRITING IN CSV -----
myfile = open("resulting_data.csv", 'w')
myfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')  # Create heading

for value in overal_score:
    valueInString = '{}, {}, {}, {}, {}\n'.format(value[0], value[1], value[2], value[3], value[4])
    myfile.write(valueInString)

myfile.close()



