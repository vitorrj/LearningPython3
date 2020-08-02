# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name, prizeMoney=0, prizes=[]):
        self.name = name
        self.prizeMoney = prizeMoney
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        message = "{} has ${} \n\nCategory: {} \nPhrase:  {} \nGuessed: {} \n\nGuess a letter, phrase, or type 'exit' or 'pass':".format(
            self.name, self.prizeMoney, self.category, self.obscured_phrase.self.guessed)
        prompt = input(message)
        return prompt


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty, prizeMoney=0):
        self.difficulty = difficulty
        self.name = name
        self.prizeMoney = prizeMoney

    def smartCoinFlip():
        number = random.randint(1, 10)
        if number > self.difficulty:
            return True
        else:
            return False


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        random_number = random.randint(1, 10)
        if random_number > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed=[]):
        lst = []
        for i in LETTERS:
            if self.prizeMoney < VOWEL_COST:
                if i not in guessed and i not in VOWELS:
                    lst.append(i)
            else:
                if i not in guessed:
                    lst.append(i)
        return lst

    def getMove(self, category, obscuredPhrase, guessed=[]):
        possible_letters = self.getPossibleLetters(guessed)

        if not possible_letters:
            return 'pass'
        else:
            if self.smartCoinFlip():
                for letter in self.SORTED_FREQUENCIES[::-1]:
                    if letter in possible_letters:
                        return letter
            else:
                return random.choice(possible_letters)

testingClass = WOFComputerPlayer("Vitor")