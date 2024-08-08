

#####Uzimni codim#####
# import random
# import json
#
# with open("Autotest/rus.json", 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# user_data = {
#     "Question_id": [],
#     "Correct_answer": [],
#     "Incorrect_answer": [],
#     "Questions": []  # Initialize 'Questions' key as an empty list
# }
#
# def print_question(q_id):
#     options = ["a", "b", "c", "d", "e"]
#     print(data[q_id]["question"])
#     for x in range(0, len(data[q_id]["choises"])):
#         print(options[x], ")", data[q_id]["choises"][x]["text"])
#         user_data["Questions"].append(data[q_id]["choises"][x]["text"])  # Append the question text to 'Questions' list
#
#
# def check(q_id, user_answer):
#     answer_index = ord(user_answer) - ord('a')  # Convert user's letter answer to index
#     correct_answer = data[q_id]["choises"][answer_index]["answer"]
#     if correct_answer:
#         print("Correct")
#         user_data["Correct_answer"].append(True)
#     else:
#         print("False")
#         user_data["Correct_answer"].append(False)
#
#
# copy_data = data[:]
# random.shuffle(copy_data)
# no_question = int(input("Enter number of questions: "))
# for x in range(0, no_question):
#     print_question(x)
#     user_answer = input("Your choice: ")
#     check(x, user_answer)








#
# import random
# import json
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot("6984024564:AAFkonur9eb0HCCFRq_xMeI8JWs81rSa4uI")
#
# with open("Autotest/rus.json", 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# user_data = {
#     "Question_id": [],
#     "Correct_answer": [],
#     "Incorrect_answer": [],
#     "Questions": []
# }
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Welcome to the Quiz Bot! Press /quiz to start the quiz.")
#
# @bot.message_handler(commands=['quiz'])
# def quiz(message):
#     bot.send_message(message.chat.id, "How many questions would you like in the quiz? (Enter a number)")
#     bot.register_next_step_handler(message, start_quiz)
#
# def start_quiz(message):
#     try:
#         num_questions = int(message.text)
#         if num_questions <= 0:
#             bot.send_message(message.chat.id, "Please enter a positive number.")
#             return
#         copy_data = data[:]
#         random.shuffle(copy_data)
#         user_data['current_question'] = 0
#         user_data['score'] = 0
#         user_data['num_questions'] = min(num_questions, len(data))
#         user_data['incorrect_answers'] = []  # Initialize list to store incorrectly answered questions
#         send_question(message.chat.id, copy_data[0])
#     except ValueError:
#         bot.send_message(message.chat.id, "Please enter a valid number.")
#
# def send_question(chat_id, question_data):
#     options = ["a", "b", "c", "d", "e"]
#     question_text = question_data["question"]
#     choices = question_data["choises"]
#
#     markup = types.InlineKeyboardMarkup()
#
#     for i in range(len(choices)):
#         button = types.InlineKeyboardButton(f"{options[i]}: {choices[i]['text']}", callback_data=str(i))
#         markup.add(button)
#
#     bot.send_message(chat_id=chat_id, text=question_text, reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def button(call):
#     choice_index = int(call.data)
#     correct_answer = data[user_data['current_question']]["choises"][choice_index]["answer"]
#
#     if correct_answer:
#         user_data['score'] += 1
#     else:
#         user_data['score'] -= 0.25  # Deduct 0.25 for wrong answer
#         user_data['incorrect_answers'].append(data[user_data['current_question']])  # Add incorrectly answered question to list
#
#
#     user_data['current_question'] += 1
#
#     if user_data['current_question'] < user_data['num_questions']:
#         send_question(call.message.chat.id, data[user_data['current_question']])
#     else:
#         bot.send_message(call.message.chat.id, f"Quiz completed! Your score: {user_data['score']}/{user_data['num_questions']}")
#
# @bot.message_handler(commands=['show_incorrect'])
# def show_incorrect(message):
#     if user_data['incorrect_answers']:
#         bot.send_message(message.chat.id, "Here are the incorrectly answered questions:")
#         for question in user_data['incorrect_answers']:
#             bot.send_message(message.chat.id, question["question"])
#             for choice in question["choises"]:
#                 bot.send_message(message.chat.id, f"{choice['text']}: {'Correct' if choice['answer'] else 'Incorrect'}")
#     else:
#         bot.send_message(message.chat.id, "No incorrect answers.")
#
# @bot.message_handler(commands=['Show_Num_incorrect_correct_ans'])
# def show_stats(message):
#     correct_answers = user_data['score']
#     total_questions = user_data['num_questions']
#     incorrect_answers = len(user_data['incorrect_answers'])
#     bot.send_message(message.chat.id, f"Number of correct answers: {correct_answers}\nNumber of incorrect answers: {incorrect_answers}\nTotal questions: {total_questions}")
#
# bot.polling()



# import random
# import json
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot("6984024564:AAFkonur9eb0HCCFRq_xMeI8JWs81rSa4uI")
#
# # Load quiz data
# with open("Autotest/rus.json", 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
#
# # Initialize user data
# user_data = {
#     "Question_id": [],
#     "Correct_answer": [],
#     "Incorrect_answer": [],
#     "Questions": [],
#     "score": 0,
#     "num_questions": 0,
#     "incorrect_answers": [],
#     "grade": "",
#     "status": "",
#     "percentage": 0,
#     "gpa": 0
# }
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Welcome to the Quiz Bot! Press /quiz to start the quiz.")
#
# @bot.message_handler(commands=['quiz'])
# def quiz(message):
#     bot.send_message(message.chat.id, "How many questions would you like in the quiz? (Enter a number)")
#     bot.register_next_step_handler(message, start_quiz)
#
# def start_quiz(message):
#     try:
#         num_questions = int(message.text)
#         if num_questions <= 0:
#             bot.send_message(message.chat.id, "Please enter a positive number.")
#             return
#         copy_data = data[:]
#         random.shuffle(copy_data)
#         user_data['current_question'] = 0
#         user_data['score'] = 0
#         user_data['num_questions'] = min(num_questions, len(data))
#         user_data['incorrect_answers'] = []  # Initialize list to store incorrectly answered questions
#         send_question(message.chat.id, copy_data[0])
#     except ValueError:
#         bot.send_message(message.chat.id, "Please enter a valid number.")
#
# def send_question(chat_id, question_data):
#     options = ["a", "b", "c", "d", "e"]
#     question_text = question_data["question"]
#     choices = question_data["choices"]
#
#     markup = types.InlineKeyboardMarkup()
#
#     for i in range(len(choices)):
#         button = types.InlineKeyboardButton(f"{options[i]}: {choices[i]['text']}", callback_data=str(i))
#         markup.add(button)
#
#     bot.send_message(chat_id=chat_id, text=question_text, reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def button(call):
#     choice_index = int(call.data)
#     correct_answer = data[user_data['current_question']]["choices"][choice_index]["answer"]
#
#     if correct_answer:
#         user_data['score'] += 1
#     else:
#         user_data['score'] -= 0.25  # Deduct 0.25 for wrong answer
#         user_data['incorrect_answers'].append(data[user_data['current_question']])  # Add incorrectly answered question to list
#
#     user_data['current_question'] += 1
#
#     if user_data['current_question'] < user_data['num_questions']:
#         send_question(call.message.chat.id, data[user_data['current_question']])
#     else:
#         calculate_results(call.message.chat.id)
#
# def calculate_results(chat_id):
#     total_questions = user_data['num_questions']
#     correct_answers = user_data['score']
#     incorrect_answers = len(user_data['incorrect_answers'])
#     percentage = (correct_answers / total_questions) * 100
#
#     # Calculate GPA and grade based on your grading scale and criteria
#     # Example grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
#     if percentage >= 90:
#         grade = "A"
#     elif percentage >= 80:
#         grade = "B"
#     elif percentage >= 70:
#         grade = "C"
#     elif percentage >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#
#     # Determine pass/fail status based on your passing criteria
#     passing_criteria = 60
#     status = "Passed" if percentage >= passing_criteria else "Failed"
#
#     # Calculate GPA based on your GPA calculation method
#     # Example GPA calculation method: (A=4, B=3, C=2, D=1, F=0)
#     gpa_scale = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
#     gpa = gpa_scale.get(grade, 0)
#
#     user_data.update({
#         "grade": grade,
#         "status": status,
#         "percentage": percentage,
#         "gpa": gpa
#     })
#
#     # Send results to the user
#     bot.send_message(chat_id, f"Number of correct answers: {correct_answers}\nNumber of incorrect answers: {incorrect_answers}\nTotal questions: {total_questions}\nGrade: {grade}\nStatus: {status}\nPercentage: {percentage}%\nGPA: {gpa}")
#
# @bot.message_handler(commands=['show_incorrect'])
# def show_incorrect(message):
#     if user_data['incorrect_answers']:
#         bot.send_message(message.chat.id, "Here are the incorrectly answered questions:")
#         for question in user_data['incorrect_answers']:
#             bot.send_message(message.chat.id, question["question"])
#             for choice in question["choices"]:
#                 bot.send_message(message.chat.id, f"{choice['text']}: {'Correct' if choice['answer'] else 'Incorrect'}")
#     else:
#         bot.send_message(message.chat.id, "No incorrect answers.")
#
# bot.polling()












































































# import random
# import json
# import telebot
# import os
# from telebot import types
#
# bot = telebot.TeleBot("6984024564:AAFkonur9eb0HCCFRq_xMeI8JWs81rSa4uI")
#
# # Language options
# languages = {
#     "Russian": "Autotest/rus.json",
#     "Uzbek (Cyrillic)": "Autotest/uzkiril.json",
#     "Uzbek (Latin)": "Autotest/uzlotin.json"
# }
#
# users = {}
#
# # Start command handler
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for lang_name in languages:
#         markup.add(types.KeyboardButton(lang_name))
#     bot.send_message(message.chat.id, "Welcome! Please choose your language:", reply_markup=markup)
#
# # Language choice handler
# @bot.message_handler(func=lambda message: message.text in languages.keys())
# def language_choice(message):
#     language_choice = message.text
#     with open(languages[language_choice], "r", encoding="utf-8") as f:
#         data = json.load(f)
#         users[message.chat.id] = {"language": language_choice, "data": data}
#         bot.send_message(message.chat.id, "How many questions do you want to answer?")
#
# # Quiz command handler
# @bot.message_handler(func=lambda message: message.text.isdigit())
# def quiz(message):
#     if message.chat.id not in users:
#         bot.reply_to(message, "Please choose your language first.")
#         return
#
#     question_count = int(message.text)
#     start_quiz(message.chat.id, question_count)
#
# # Start the quiz
# def start_quiz(chat_id, question_count):
#     user_info = users[chat_id]
#     data = user_info["data"]
#     random.shuffle(data)
#     questions = data[:question_count]
#     users[chat_id]["questions"] = questions
#     users[chat_id]["question_index"] = 0
#     users[chat_id]["score"] = 0
#     users[chat_id]["correct_answers"] = 0
#     users[chat_id]["incorrect_answers"] = []
#     users[chat_id]["answered_questions"] = set()
#     print_question(chat_id)
#
# # Print question function
# def print_question(chat_id):
#     user_info = users[chat_id]
#     question_index = user_info["question_index"]
#     if question_index >= len(user_info["questions"]):
#         bot.send_message(chat_id, "End of questions.")
#         show_summary(chat_id)
#         return
#
#     question = user_info["questions"][question_index]
#     bot.send_message(chat_id, question["question"])
#
#     # Check if media exists and send it if available
#     if question["media"]["exist"]:
#         media_path = f"Autotest/{question['media']['name']}.png"  # Change the file extension if necessary
#         if os.path.exists(media_path):
#             with open(media_path, "rb") as photo:
#                 bot.send_photo(chat_id, photo)
#         else:
#             bot.send_message(chat_id, "Media file not found.")
#
#     markup = types.InlineKeyboardMarkup(row_width=6)
#
#     # Generate variants as A, B, C, D, E
#     variants = ['A', 'B', 'C', 'D', 'E']
#     for i, choice in enumerate(question["choices"]):
#         markup.add(types.InlineKeyboardButton(f'{variants[i]}. {choice["text"]}', callback_data=f'answer_{i}'))
#
#     # Add a Skip button
#     markup.add(types.InlineKeyboardButton('Skip', callback_data='skip'))
#
#     bot.send_message(chat_id, "Please select your answer:", reply_markup=markup)
#
# # Answer handler
# @bot.callback_query_handler(func=lambda call: call.data.startswith('answer_') or call.data == 'skip')
# def answer(call):
#     user_info = users[call.message.chat.id]
#     question_index = user_info["question_index"]
#     question = user_info["questions"][question_index]
#
#     if call.data == 'skip':
#         users[call.message.chat.id]["question_index"] += 1
#         users[call.message.chat.id]["score"] += 0  # Score of 0 for skipping
#         print_question(call.message.chat.id)
#         return
#
#     user_answer_index = int(call.data.split('_')[1])
#
#     if question_index in user_info["answered_questions"]:
#         bot.answer_callback_query(call.id, text="You have already answered this question.", show_alert=True)
#         return
#
#     user_info["answered_questions"].add(question_index)
#     correct_option_index = next((i for i, option in enumerate(question["choices"]) if option["answer"]), None)
#     if user_answer_index == correct_option_index:
#         users[call.message.chat.id]["score"] += 1
#         users[call.message.chat.id]["correct_answers"] += 1
#
#         bot.send_message(call.message.chat.id, "✅")
#     else:
#         users[call.message.chat.id]["score"] -= 0.25
#         users[call.message.chat.id]["incorrect_answers"].append(question)
#
#         bot.send_message(call.message.chat.id, "❌")
#
#     users[call.message.chat.id]["question_index"] += 1
#     print_question(call.message.chat.id)
#
# # Show summary
# def show_summary(chat_id):
#     user_info = users[chat_id]
#     total_questions = len(user_info["questions"])
#     correct_answers = user_info["correct_answers"]
#     incorrect_answers = user_info["incorrect_answers"]
#     score = user_info["score"]
#
#     bot.send_message(chat_id, f"Summary:\n"
#                               f"Total Questions: {total_questions}\n"
#                               f"Correct Answers: {correct_answers}\n"
#                               f"Incorrect Answers: {len(incorrect_answers)}\n"
#                               f"Total Score: {score}\n"
#                               f"Grade: {calculate_grade(score)}")
#
#     if incorrect_answers:
#         bot.send_message(chat_id, "Here are the incorrectly answered questions:")
#         for question in incorrect_answers:
#             bot.send_message(chat_id, question["question"])
#             for choice in question["choices"]:
#                 bot.send_message(chat_id, f"{choice['text']}: {'Correct' if choice['answer'] else 'Incorrect'}")
#     else:
#         bot.send_message(chat_id, "No incorrect answers.")
#
# # Calculate grade
# def calculate_grade(score):
#     percentage = (score / 100) * 100  # Assuming total possible score is 100
#     if percentage >= 70:
#         return f"Pass - {percentage}%"
#     else:
#         return f"Fail - {percentage}%"
#
# # Start the bot
# bot.polling()





import random
import json
import telebot
import os
import mysql.connector
from telebot import types

import mysql.connector

# Establish MySQL connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="qiuz_bot"
)
cursor = db_connection.cursor()

# Define the SELECT query
select_query = "SELECT * FROM quiz_results ORDER BY score DESC"

# Execute the SELECT query
cursor.execute(select_query)

# Fetch all records
records = cursor.fetchall()

# Display the records
for record in records:
    print(record)

# Close cursor and connection
cursor.close()
db_connection.close()
bot = telebot.TeleBot("6984024564:AAFkonur9eb0HCCFRq_xMeI8JWs81rSa4uI")

# Language options
languages = {
    "Russian": "Autotest/rus.json",
    "Uzbek-Cyrillic": "Autotest/uzkiril.json",
    "Uzbek-Latin": "Autotest/uzlotin.json"

}

users = {}


# Start command handler
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for lang_name in languages:
        # if lang_name == "Russian":
        #     flag_emoji = "🇷🇺"
        # elif lang_name == "Uzbek-Cyrillic":
        #     flag_emoji = "🇺🇿"
        #     flag_emoji = "🇺🇿"

        markup.add(types.KeyboardButton(f" {lang_name}"))
    bot.send_message(message.chat.id, "Welcome! Please choose your language:", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text in languages.keys())
def language_choice(message):
    language_choice = message.text
    with open(languages[language_choice], "r", encoding="utf-8") as f:
        data = json.load(f)
        users[message.chat.id] = {"language": language_choice, "data": data}
        bot.send_message(message.chat.id, "How many questions do you want to answer?")

# Quiz command handler
@bot.message_handler(func=lambda message: message.text.isdigit())
def quiz(message):
    if message.chat.id not in users:
        bot.reply_to(message, "Please choose your language first.")
        return

    question_count = int(message.text)
    start_quiz(message.chat.id, question_count)

# Start the quiz
def start_quiz(chat_id, question_count):
    user_info = users[chat_id]
    data = user_info["data"]
    random.shuffle(data)
    questions = data[:question_count]
    users[chat_id]["questions"] = questions
    users[chat_id]["question_index"] = 0
    users[chat_id]["score"] = 0
    users[chat_id]["correct_answers"] = 0
    users[chat_id]["incorrect_answers"] = []
    users[chat_id]["answered_questions"] = set()
    print_question(chat_id)

# Print question function
def print_question(chat_id):
    user_info = users[chat_id]
    question_index = user_info["question_index"]
    if question_index >= len(user_info["questions"]):

        show_summary(chat_id)
        return

    question = user_info["questions"][question_index]
    bot.send_message(chat_id, question["question"])

    # Check if media exists and send it if available
    if question["media"]["exist"]:
        media_path = f"Autotest/{question['media']['name']}.png"  # Change the file extension if necessary
        if os.path.exists(media_path):
            with open(media_path, "rb") as photo:
                bot.send_photo(chat_id, photo)
        else:
            bot.send_message(chat_id, "Media file not found.")

    markup = types.InlineKeyboardMarkup(row_width=6)

    # Generate variants as A, B, C, D, E
    variants = ['A', 'B', 'C', 'D', 'E']
    for i, choice in enumerate(question["choices"]):
        markup.add(types.InlineKeyboardButton(f'{variants[i]}. {choice["text"]}', callback_data=f'answer_{i}'))

    # Add a Skip button
    markup.add(types.InlineKeyboardButton('Skip', callback_data='skip'))

    bot.send_message(chat_id, "Please select your answer:", reply_markup=markup)

# Answer handler
@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_') or call.data == 'skip')
def answer(call):
    user_info = users[call.message.chat.id]
    question_index = user_info["question_index"]
    question = user_info["questions"][question_index]

    if call.data == 'skip':
        users[call.message.chat.id]["question_index"] += 1
        users[call.message.chat.id]["score"] += 0  # Score of 0 for skipping
        print_question(call.message.chat.id)
        return

    user_answer_index = int(call.data.split('_')[1])

    if question_index in user_info["answered_questions"]:
        bot.answer_callback_query(call.id, text="You have already answered this question.", show_alert=True)
        return

    user_info["answered_questions"].add(question_index)
    correct_option_index = next((i for i, option in enumerate(question["choices"]) if option["answer"]), None)
    if user_answer_index == correct_option_index:
        users[call.message.chat.id]["score"] += 1
        users[call.message.chat.id]["correct_answers"] += 1

        bot.send_message(call.message.chat.id, "✅")
    else:
        users[call.message.chat.id]["score"] -= 0.25
        users[call.message.chat.id]["incorrect_answers"].append(question)

        bot.send_message(call.message.chat.id, "❌")

    users[call.message.chat.id]["question_index"] += 1
    print_question(call.message.chat.id)

# Show summary
def show_summary(chat_id):
    user_info = users[chat_id]
    total_questions = len(user_info["questions"])
    correct_answers = user_info["correct_answers"]
    incorrect_answers = user_info["incorrect_answers"]
    score = user_info["score"]

    bot.send_message(chat_id, f"Summary:\n"
                              f"Total Questions: {total_questions}\n"
                              f"Correct Answers: {correct_answers}\n"
                              f"Incorrect Answers: {len(incorrect_answers)}\n"
                              f"Total Score: {score}\n"
                              f"Grade: {calculate_grade(score)}")

    if incorrect_answers:
        bot.send_message(chat_id, "Here are the incorrectly answered questions:")
        for question in incorrect_answers:
            bot.send_message(chat_id, question["question"])
            for choice in question["choices"]:
                bot.send_message(chat_id, f"{choice['text']}: {'Correct' if choice['answer'] else 'Incorrect'}")
    else:
        bot.send_message(chat_id, "No incorrect answers.")

# Calculate grade
def calculate_grade(score):
    percentage = (score / 100) * 100  # Assuming total possible score is 100
    if percentage >= 70:
        return f"Pass - {percentage}%"
    else:
        return f"Fail - {percentage}%"

# Start the bot
bot.polling()

