import telebot

from telebot import types

from info import Quiz

TOKEN = '6922861550:AAG6-PugcPBe68GTOQ3TcvgJtHlI9_rtLc0'

bot = telebot.TeleBot(TOKEN)

quiz = Quiz()


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Привет! Добро пожаловать в викторину по видеоиграм!")

    reset_quiz_data(chat_id)

    send_question(chat_id)


@bot.message_handler(commands=['info'])
def handle_info(message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Викторина по видеоиграм.\nОтвечайте на вопросы, выбирая один из вариантов ответа .")


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = message.chat.id

    user_answer = message.text.lower().split(':')[0].strip()  # get the first character of the answer

    if not is_valid_answer(user_answer):
        bot.send_message(chat_id, "Пожалуйста, напишите один из вариантов ответа указанный на кнопке.")

        return

    save_answer(chat_id, user_answer)

    send_question(chat_id)


def is_valid_answer(answer):
    return answer in ["a", "b", "c", "d"]


def reset_quiz_data(chat_id):
    quiz.reset_quiz_data(chat_id)


def send_question(chat_id):
    question = quiz.get_current_question(chat_id)

    if question is None:

        send_quiz_result(chat_id)


    else:

        answers = quiz.get_current_answers(chat_id)

        markup = types.ReplyKeyboardMarkup(row_width=2)

        for answer in answers:
            markup.add(types.KeyboardButton(answer))

        bot.send_message(chat_id, question, reply_markup=markup)


def send_quiz_result(chat_id):
    result = quiz.calculate_result(chat_id)

    bot.send_photo(chat_id,

                   'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fupload.wikimedia.org'


                   '%2Fwikipedia%2Fcommons%2Fthumb%2F9%2F97%2FSigma_Logo.svg%2F1600px-Sigma_Logo.svg.png&lr=8&p=6&pos'


                   '=16&rpt=simage&text=%D1%81%D0%B8%D0%B3%D0%BC%D0%B0')

    bot.send_message(chat_id, f"Вы завершили викторину! Ваш результат: {result}")


def save_answer(chat_id, answer):
    quiz.save_answer(chat_id, answer)


bot.polling()


