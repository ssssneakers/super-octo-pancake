import json


def is_valid_answer(answer):
    return answer in ["a", "b", "c", "d"]


class Quiz:
    def __init__(self):

        self.questions = {
            "cs go": {
                "question": "В каком году вышла игра 'CS:GO'?",
                "answers": {
                    "a": "2000",
                    "b": "2012",
                    "c": "2016",
                    "d": "2020"
                },
                "correct_answer": "b"
            },
            "gta 5": {
                "question": "Какое название у последней части игры Grand Theft Auto?",
                "answers": {
                    "a": "GTA 4",
                    "b": "GTA V",
                    "c": "GTA: San Andreas",
                    "d": "GTA: Vice City"
                },
                "correct_answer": "b"
            },
            "portal 2": {
                "question": "Кто является главным героем игры Portal 2?",
                "answers": {
                    "a": "Гордон Фримен",
                    "b": "Алекс Вэнс",
                    "c": "Shell",
                    "d": "Человек-паук"
                },
                "correct_answer": "c"
            },
            "spider-man": {
                "question": "Кто главный герой комиксов о человеке пауке?",
                "answers": {
                    "a": "Майлз Моралез",
                    "b": "Патрик бейтман",
                    "c": "Питер Паркер",
                    "d": "Том Холонд"
                },
                "correct_answer": "c"
            },

            "Cyberpunk": {
                "question": "Как называется имплант замедляющий время?",
                "answers": {
                    "a": "Берсерк",
                    "b": "Богомол",
                    "c": "Монострун",
                    "d": "Сандевистан"
                },
                "correct_answer": "d"
            },
            "Rust": {
                "question": "Сколько спит каждый растер?",
                "answers": {
                    "a": "8 часов в день",
                    "b": "они не спят....",
                    "c": "2 часа",
                    "d": "5 часов"
                },
                "correct_answer": "b"

            },
            "prank": {
                "question": "Макс олух?",
                "answers": {
                    "a": "да",
                    "b": "нет"
                },
                "correct_answer": "a"
            }

        }
        self.quiz_data = {}
        self.load_quiz_data()

    def is_valid_answer(self, answer):
        return answer in ["a", "b", "c", "d"]

    def reset_quiz_data(self, chat_id):
        self.quiz_data[chat_id] = {
            "current_question": 0,
            "answers": {}
        }

    def get_current_question(self, chat_id):
        current_question_index = self.quiz_data[chat_id]["current_question"]
        if current_question_index >= len(self.questions):
            return None
        current_question = list(self.questions.keys())[current_question_index]
        return self.questions[current_question]["question"]

    def get_current_answers(self, chat_id):
        current_question_index = self.quiz_data[chat_id]["current_question"]
        if current_question_index >= len(self.questions):
            return None
        current_question = list(self.questions.keys())[current_question_index]
        answers = self.questions[current_question]["answers"]
        return [f'{answer}: {answers[answer]}' for answer in answers]

    def save_answer(self, chat_id, answer):
        current_question_index = self.quiz_data[chat_id]["current_question"]
        current_question = list(self.questions.keys())[current_question_index]
        self.quiz_data[chat_id]['answers'][current_question] = answer
        self.quiz_data[chat_id]["current_question"] += 1

    def calculate_result(self, chat_id):
        user_answers = self.quiz_data[chat_id]['answers']
        correct_answers = 0
        for question in user_answers:
            if user_answers[question] == self.questions[question]["correct_answer"]:
                correct_answers += 1
        return f"{correct_answers}/{len(self.questions)}"

    def save_quiz_data(self):
        with open("quiz_data.json", "w") as file:
            json.dump(self.quiz_data, file)

    def load_quiz_data(self):
        try:
            with open("quiz_data.json", "r") as file:
                self.quiz_data = json.load(file)
        except FileNotFoundError:
            self.quiz_data = {}
