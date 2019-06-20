import subprocess
import threading
import wordninja
import timeit

class Tts:
    code = [["Ae", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Zee"]]

    def __init__(self):
        self.sentence = ""
        self.current_row = -1
        self.wpm = 90
        
    def select_row(self, key):
        self.current_row = key
        self.wpm = 110
        self.speak(self.code[key][0])
        self.speak("too")
        self.speak(self.code[key][4])
        self.wpm = 90

    def select_letter(self, key):
        letter = self.code[self.current_row][key]
        self.current_row = -1
        self.sentence += letter[0]
        self.speak([letter])
        
    def play_sentence(self):
        sentence = " ".join(wordninja.split(self.sentence))
        self.speak([sentence])
        self.sentence = ""
        self.current_row = -1

    '''
    0-4 = rows/letters
    5 = speak sentence
    6 = go back
    '''
    def handle_action(self, key):
        if key == 5:
            self.play_sentence()
        elif key == 6:
            pass
        else:
            if self.current_row == -1:
                self.select_row(key)
            else:
                self.select_letter(key)
    
    def speak(self, sentence):
        print(sentence)
        t = threading.Thread(target=lambda: subprocess.run(["espeak", sentence])).start()
