#1
class Validator: 
    def valid_password(self, password): 
        if len(password) < 8: 
            print("Invalid:  Maximun length of 8 characters.") 
        elif not any(char.isupper() for char in password): 
            print("Invalid: At least one uppercase letter.") 
        elif not any(char.islower() for char in password): 
            print("Invalid: At least one lowercase letter.") 
        elif not any(char.isdigit() for char in password): 
            print("Invalid:  At least one digit.") 
        elif not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/|" for char in password): 
            print("Invalid: At least one special character.") 
        else: 
            print("Password is valid!") 
 
pass_wo= input("Enter your password: ") 
vali = Validator() 
vali.valid_password(pass_wo)
#2
class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.List=[]
    def split_into_sentences(self):
        punctuation = ['.', '!', '?']
        sent = ""
        for char in self.text:
            sent += char
            if char in punctuation:
                self.List.append(sent.strip())
                sent= ""
        if sent.strip():  
                self.List.append(sent.strip())
        for i in self.List:
            print(i)
    def process_sentences(self):
        for sent in self.List:
            word_count = len(sent.split())
            print("Sentence:",sent,", Word Count:",word_count)
text = input()
p = TextProcessor(text)
p.split_into_sentences()
p.process_sentences()
