from sys import exit, argv
from random import choice
from time import sleep

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QToolTip, QPushButton, QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator

WORDS = ['Captivity', 'America', 'Europe', 'Federal', 'Gluten', 'Ridiculous', 'Automatic', 'Television', 'Difficult', 'Severe', 'Interesting', 'Indonesia', 'Industrial',
     'Automotive', 'President', 'Terrestrial', 'Academic', 'Comedic', 'Comical', 'Genuine', 'Suitcase', 'Vietnam', 'Achievement', 'Careless', 'Monarchy', 'Monetary', 
     'Quarantine', 'Supernatural', 'Illuminate', 'Optimal', 'Application', 'Scientist', 'Software', 'Hardware', 'Program', 'Colonial', 'Algorithm', 'Intelligent', 
     'Electricity', 'Verification', 'Broadband', 'Quality', 'Validation', 'Online', 'Telephone', 'Dictionary', 'Keyboard', 'China', 'London', 'Jamaica', 'Biology', 
     'Chemistry', 'History', 'Historian', 'Africa', 'Mathematics', 'Computer', 'Literature', 'Gravity', 'Guitar', 'Violin', 'Illuminate', 'England', 'China', 'Japan',
     'Canada', 'Suitcase', 'Wireless', 'Internet']

HANGMAN_PARMS = 100, 200, Qt.KeepAspectRatio, Qt.FastTransformation

class hangman(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('background.jpg').scaled(201, 352, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        self.background.move(-1, -1)

        self.number = 1
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('hangman_{}.png'.format(self.number)).scaled(*HANGMAN_PARMS))
        self.image.move(60, 0.5)

        self.word = choice(WORDS)
        blank_word = '_ ' * len(self.word)
        blank_word.rstrip()  

        self.blank_word_label = QLabel(blank_word, self)
        font1 = self.blank_word_label.font()
        font1.setPointSize(14)
        self.blank_word_label.setFont(font1)
        self.blank_word_label.setFixedWidth(200)
        self.blank_word_label.setToolTip('Attempt to fill in the blanks')
        self.blank_word_label.move(0,200)
        self.blank_word_label.setAlignment(Qt.AlignCenter)

        self.guessed_letters = ''

        self.btn = QPushButton('Check', self)
        self.btn.setFont(QFont('SansSerif', 20))
        self.btn.setToolTip('Click to check if the entered letter is in the word')
        self.btn.clicked.connect(self.check_letter)
        self.btn.resize(102, 43)
        self.btn.move(99, 228)

        self.entered_letter = QLineEdit(self)
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)
        self.entered_letter.setValidator(validator)
        font2 = self.entered_letter.font()
        font2.setPointSize(24)
        self.entered_letter.setFont(font2)
        self.entered_letter.setMaxLength(1)
        self.entered_letter.setToolTip('Enter a letter and check if it is in the word')
        self.entered_letter.setFocus(True)
        self.entered_letter.returnPressed.connect(self.check_letter)
        self.entered_letter.resize(100, 43)
        self.entered_letter.move(0.5, 228)

        self.correct_or_incorrect = QLabel(self)
        self.correct_or_incorrect.move(1, 232)
        self.correct_or_incorrect.setVisible(False)

        self.you_lose = QLabel(self)
        self.you_lose.setPixmap(QPixmap('game_over.jpg').scaled(200, 160, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        self.you_lose.move(0.5, 0.5)
        self.you_lose.setVisible(False)

        self.you_win = QLabel(self)
        self.you_win.setPixmap(QPixmap('congratulations.jpg').scaled(200, 160, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        self.you_win.move(0.5, 0.5)
        self.you_win.setVisible(False)

        self.correct_word = QLabel('The word was:', self)
        font1 = self.correct_word.font()
        font1.setPointSize(14)
        self.correct_word.setFont(font1)
        self.correct_word.setFixedWidth(200)
        self.correct_word.move(0,170)
        self.correct_word.setAlignment(Qt.AlignCenter)
        self.correct_word.setVisible(False)

        self.replay_btn = QPushButton('Play Again', self)
        self.replay_btn.setFont(QFont('SansSerif', 15))
        self.replay_btn.setToolTip('Click to play another game of Hangman')
        self.replay_btn.clicked.connect(self.replay)
        self.replay_btn.resize(202, 33)
        self.replay_btn.move(-1, 239.8)
        self.replay_btn.setVisible(False)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(1390, 30, 200, 270)
        self.setFixedSize(self.size())
        self.setWindowTitle('Hangman')
        self.setWindowIcon(QIcon('icon.png'))      
        self.show()

    def check_letter(self):

            if self.entered_letter.text().lower() in self.word.lower():
                self.guessed_letters += self.entered_letter.text().lower()
                self.correct_or_incorrect.setPixmap(QPixmap('correct.png').scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
                self.correct_or_incorrect.setVisible(True)
                QApplication.processEvents()
                sleep(0.1)
                self.correct_or_incorrect.setVisible(False)
                QApplication.processEvents()

            else:
                self.number += 1
                self.image.setPixmap(QPixmap('hangman_{}.png'.format(self.number)).scaled(*HANGMAN_PARMS))
                self.correct_or_incorrect.setPixmap(QPixmap('incorrect.png').scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
                self.correct_or_incorrect.setVisible(True)
                QApplication.processEvents()
                sleep(0.1)
                self.correct_or_incorrect.setVisible(False)
                QApplication.processEvents()

            blank_word = ''
            for i in self.word:
                if i.lower() in self.guessed_letters:
                    blank_word += i   

                else:
                    blank_word += '_ '

            blank_word.rstrip()

            self.blank_word_label.setText(blank_word)
            self.entered_letter.setText('')
            self.entered_letter.setFocus(True)

            if self.number == 7:
                self.blank_word_label.setText(self.word)
                self.image.setVisible(False)
                self.entered_letter.setVisible(False)
                self.btn.setVisible(False)
                self.you_lose.setVisible(True)
                self.correct_word.setVisible(True)
                self.replay_btn.setVisible(True)

            if blank_word == self.word:
                self.image.setVisible(False)
                self.entered_letter.setVisible(False)
                self.btn.setVisible(False)
                self.you_win.setVisible(True)
                self.correct_word.setVisible(True)
                self.replay_btn.setVisible(True)

    def replay(self):
        self.number = 1
        self.image.setPixmap(QPixmap('hangman_{}.png'.format(self.number)).scaled(*HANGMAN_PARMS))
        self.word = choice(WORDS)
        blank_word = '_ ' * len(self.word)
        blank_word.rstrip()
        self.blank_word_label.setText(blank_word)
        self.guessed_letters = ''
        self.you_lose.setVisible(False)
        self.you_win.setVisible(False)
        self.correct_word.setVisible(False)
        self.replay_btn.setVisible(False)
        self.image.setVisible(True)
        self.entered_letter.setVisible(True)
        self.btn.setVisible(True)
        self.entered_letter.setFocus(True)                  



if __name__ == '__main__':

    app = QApplication(argv)
    ex = hangman()
    ex.show()
    exit(app.exec_())