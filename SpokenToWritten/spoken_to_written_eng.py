class SpokenEngToWrittenEng:
    def __init__(self):
        self.rules = {"Numbers": {"zero": 0, "one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10},
            "Tuples": {"single":1, "double":2, "triple":3},
            "General": {"C M": "CM", "P M": "PM", "D M": "DM", "A M": "AM", "F M": "FM"}}
        self.para = ""
        self.output_para = ""

    def get_user_input(self):
        self.para = input("Enter Your paragraph of spoken english:\n")

    def show_output(self):
        print("The input Spoken English Paragraph:\n", self.para)
        print()
        print("Converted Written English Paragraph:\n", self.output_para)

    def convert(self):
        import re
        words = self.para.split()
        i = 0
        while i < len(words):
            if i < len(words) - 1:
                if words[i][-1] == '.' or words[i][-1] == ',':
                    words.insert(i+1, words[i][-1])
                    words[i] = words[i][:-1]
                    i += 1
            else:
                words.append(words[i][-1])
                words[i] = words[i][:-1]
                break
            i += 1
        numbers = self.rules['Numbers']
        tuples = self.rules['Tuples']
        general = self.rules['General']
        i = 0
        while i < len(words):
            if i < len(words)-1 and words[i].lower() in numbers.keys() and (words[i+1].lower() == 'dollars' or words[i+1].lower() == 'dollars'):
                self.output_para = self.output_para + ' $' + str(numbers[words[i].lower()])
                i += 2
            elif i < len(words)-1 and words[i].lower() in tuples.keys():
                self.output_para = self.output_para + ' ' + words[i+1] * tuples[words[i]]
                i += 2
            elif i < len(words)-1 and words[i] + ' ' + words[i+1] in general.keys():
                self.output_para = self.output_para + ' ' + general[words[i]+' '+words[i+1]]
                i += 2
            else:
                self.output_para = self.output_para + ' ' + words[i]
                i += 1
        self.output_para = re.sub(r'\s+([?.!"])', r'\1', self.output_para)

def convert_spoken_to_written_eng():
    obj = SpokenEngToWrittenEng()
    obj.get_user_input()
    obj.convert()
    obj.show_output()