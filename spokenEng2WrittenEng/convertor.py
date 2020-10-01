# Helper Functions here

# Function checkCommas: checks if word has comma at front or at last or at both if true then return front,word and last
def checkCommas(word):
    start = ""
    last = ""
    if(len(word) > 1):
        if word[-1] == ',' or word[-1] == '.':
            last = word[-1]
            word = word[:-1]
        if word[0] == ',' or word[0] == '.':
            start = word[0]
            word = word[1:]
    return start, word, last

# Function getRules: define all the rules of written english here


def getRules():
    rules = {"Numbers": {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "forteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000
    },
        "Tuples": {
        "single": 1,
        "double": 2,
        "triple": 3,
        "quadruple": 4,
        "quintuple": 5,
        "sextuple": 6,
        "septuple": 7,
        "octuple": 8,
        "nonuple": 9,
        "decuple": 10
    },
        "General": {
        "C M": "CM",
        "P M": "PM",
        "D M": "DM",
        "A M": "AM"
    }
    }
    return rules


# MAIN CLASS for the logic: spEngtoWritEng
class spEngtoWritEng:

    def __init__(self):

        self.rules = getRules()
        self.paragraph = ""
        self.convertedPara = ""

    # to get input from user in the form of paragraph
    def getInput(self):

        self.paragraph = input("\nEnter spoken english:\n\t")

        if not self.paragraph:
            raise ValueError("Error: You entered nothing.")

    # to print the output after converting to written english
    def printOutput(self):
        print("\nConverted Written English Paragraph: \n\n \"" +
              self.convertedPara+"\"")

    # main function to convert spoken to written english

    def convert(self):

        # splitting paragraph into individual words
        words_of_para = self.paragraph.split()

        numbers = self.rules['Numbers']
        tuples = self.rules['Tuples']
        general = self.rules['General']
        i = 0
        no_of_words = len(words_of_para)

        while i < no_of_words:

            start, word, last = checkCommas(words_of_para[i])

            if i+1 != no_of_words:
                # when word is of the form e.g.: two
                front_n, next_word, last_n = checkCommas(words_of_para[i+1])
                # checking dollar
                if word.lower() in numbers.keys() and (next_word.lower() == 'dollars' or next_word.lower() == 'dollar'):
                    self.convertedPara = self.convertedPara+" " + \
                        start+"$"+str(numbers[word.lower()])+last
                    i = i+2

                elif word.lower() in tuples.keys() and len(next_word) == 1:
                    # when word is of form Triple A
                    self.convertedPara = self.convertedPara+" " + \
                        front_n+(next_word*tuples[word.lower()])+last_n
                    i = i+2
                elif (word+" "+next_word) in general.keys():
                    # if word is of form P M or C M
                    self.convertedPara = self.convertedPara+" "+start+word+next_word+last_n
                    i = i+2
                else:
                    self.convertedPara = self.convertedPara + \
                        " "+words_of_para[i]
                    i = i+1
            else:
                self.convertedPara = self.convertedPara+" "+words_of_para[i]
                i = i+1


# main function
def convert_sp_to_wr():
    # creating class object
    obj_spoken = spEngtoWritEng()
    # taking input
    obj_spoken.getInput()
    # conversion
    obj_spoken.convert()

    # showing output
    obj_spoken.printOutput()
