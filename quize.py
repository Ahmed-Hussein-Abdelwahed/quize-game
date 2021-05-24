import os
import random

from pip._vendor.colorama import Fore


class Game:
    total_score = 5

    def __init__(self):
        self.right_answers = 0
        self.wrong_answers = 0
        self.lines_number = 0

    def set_file_lines(self):  # count file lines (each question consists of 5 lines)
        if self.is_file_exist():
            file = open('questions.txt', 'r')
            questions = file.read()
            content = questions.split('\n')
            counter = 0
            for i in content:
                if i:
                    counter += 1
            self.lines_number = counter
            file.close()
        else:
            print(Fore.RED + 'Questions file is not exist')

    def is_file_exist(self):  # make sure that questions file exist
        file_location = os.getcwd() + '\questions.txt'
        if os.path.exists(file_location):
            return True
        else:
            return False

    def start_game(self):  # pass list consist of 5 questions indices to show_question()
        question_index = []
        question = 0
        self.set_file_lines()
        while len(question_index) != 5:
            question = random.randrange(0, self.lines_number, 1)
            if question % 5 == 0 and question not in question_index:
                question_index.append(question)
        self.show_question(question_index)

    def show_question(self, questions_list):  # show question tag only then pass index of first choice
        if self.is_file_exist():
            file = open('questions.txt')
            content = file.readlines()
            counter = 1
            for question in questions_list:
                print(Fore.BLUE + f'[{counter}] ' + content[question])
                self.generate_choices(question + 1)
                counter += 1
            file.close()
        else:
            print(Fore.RED + 'Questions file is not exist')

    def generate_choices(self, choice_index):  # generate random indices of question choices then call take_user_answer
        file = open('questions.txt')
        content = file.readlines()
        right_answer = content[choice_index]
        choices = []
        choice = 0
        while len(choices) != 4:
            choice = random.randrange(choice_index, choice_index + 4, 1)
            if choice not in choices:
                choices.append(choice)
        file.close()
        self.take_user_answer(right_answer, choices)

    def take_user_answer(self, right_answer, indices):
        file = open('questions.txt')
        content = file.readlines()
        user_answer = ''
        print('[A] ' + content[indices[0]], end='', flush=True)
        print('[B] ' + content[indices[1]], end='', flush=True)
        print('[C] ' + content[indices[2]], end='', flush=True)
        print('[D] ' + content[indices[3]], end='', flush=True)
        while True:
            user_answer = input()
            if user_answer.lower() == 'a':
                if right_answer == content[indices[0]]:
                    self.right_answers += 1
                else:
                    self.wrong_answers += 1
                break
            elif user_answer.lower() == 'b':
                if right_answer == content[indices[1]]:
                    self.right_answers += 1
                else:
                    self.wrong_answers += 1
                break
            elif user_answer.lower() == 'c':
                if right_answer == content[indices[2]]:
                    self.right_answers += 1
                else:
                    self.wrong_answers += 1
                break
            elif user_answer.lower() == 'd':
                if right_answer == content[indices[3]]:
                    self.right_answers += 1
                else:
                    self.wrong_answers += 1
                break
            else:
                print(Fore.RED + 'Invalid choice ... must be A,B,C,or D only')
        file.close()

    def show_score(self):
        if self.right_answers == 5:
            print(Fore.GREEN)
        elif self.right_answers == 4 or self.right_answers == 3:
            print(Fore.YELLOW)
        else:
            print(Fore.RED)
        print('Your score = {} out of {}'.format(self.right_answers, self.total_score))
        print('Number of questions solved = {}'.format(self.total_score))
        print('Number of right answers = {}'.format(self.right_answers))
        print('Number of wrong answers = {}'.format(self.wrong_answers))

    def interface(self):
        user_choice = ''
        while True:
            print(Fore.WHITE + '\n[1] Start new game')
            print('[2] Exit')
            user_choice = input()
            if user_choice == '1':
                if self.is_file_exist():
                    self.start_game()
                    self.show_score()
                else:
                    print(Fore.RED + 'Unfortunately questions file is not exist attach it then rerun the program')
                    break
            elif user_choice == '2':
                break
            else:
                print(Fore.RED + 'Invalid choice ... must be 1 or 2 only')
