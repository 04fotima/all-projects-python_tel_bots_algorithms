


# import telebot
# from telebot import types
# import random
#
# TOKEN = '6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo'
#
# bot = telebot.TeleBot(TOKEN)
#
# # Dictionary to store user choices for the game between users
# user_choices_users = {}
#
# # Dictionary to store user choices for the game with the bot
# user_choices_bot = {}
#
# # Function to determine the winner in rock-paper-scissors game
# def determine_winner(choice1, choice2):
#     if choice1 == choice2:
#         return None  # It's a tie
#     elif (choice1 == "rock" and choice2 == "scissors") or \
#          (choice1 == "paper" and choice2 == "rock") or \
#          (choice1 == "scissors" and choice2 == "paper"):
#         return 'user1'  # User 1 wins
#     else:
#         return 'user2'  # User 2 wins
#
# # Handler for /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('Play with Bot')
#     itembtn2 = types.KeyboardButton('Play between Users')
#     markup.add(itembtn1, itembtn2)
#     bot.send_message(message.chat.id, "Welcome! Choose an option to play:", reply_markup=markup)
#
# # Handler for user's choice to play with the bot
# @bot.message_handler(func=lambda message: message.text == 'Play with Bot')
# def play_with_bot(message):
#     user_choices_bot[message.chat.id] = []
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('rock')
#     itembtn2 = types.KeyboardButton('paper')
#     itembtn3 = types.KeyboardButton('scissors')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(message.chat.id, "Please select your choice to play with the bot:", reply_markup=markup)
#
# # Handler for user's choice to play between users
# @bot.message_handler(func=lambda message: message.text == 'Play between Users')
# def play_between_users(message):
#     user_choices_users[message.chat.id] = []
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('rock')
#     itembtn2 = types.KeyboardButton('paper')
#     itembtn3 = types.KeyboardButton('scissors')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(message.chat.id, "Player 1, please select your choice to play between users:", reply_markup=markup)
#
# # Handler for user's choice in the game with the bot
# @bot.message_handler(func=lambda message: message.text.lower() in ['rock', 'paper', 'scissors'] and message.chat.id in user_choices_bot)
# def handle_choice_bot(message):
#     user_choice = message.text.lower()
#     bot_choice = random.choice(['rock', 'paper', 'scissors'])
#
#     winner = determine_winner(user_choice, bot_choice)
#
#     if winner == 'user1':
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. You win!")
#     elif winner == 'user2':
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. You lose!")
#     else:
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. It's a tie!")
#
# # Handler for user's choice in the game between users
# @bot.message_handler(func=lambda message: message.text.lower() in ['rock', 'paper', 'scissors'] and message.chat.id in user_choices_users)
# def handle_choice_users(message):
#     user_choice = message.text.lower()
#     chat_id = message.chat.id
#
#     if len(user_choices_users[chat_id]) == 0:
#         user_choices_users[chat_id].append(user_choice)
#         markup = types.ReplyKeyboardMarkup(row_width=1)
#         itembtn1 = types.KeyboardButton('rock')
#         itembtn2 = types.KeyboardButton('paper')
#         itembtn3 = types.KeyboardButton('scissors')
#         markup.add(itembtn1, itembtn2, itembtn3)
#         bot.send_message(chat_id, "Player 2, please select your choice to play between users:", reply_markup=markup)
#     elif len(user_choices_users[chat_id]) == 1:
#         user_choices_users[chat_id].append(user_choice)
#         play_round_users(chat_id)
#
# # Function to play a round of the game between users
# def play_round_users(chat_id):
#     choices = user_choices_users[chat_id]
#     user_choices_users[chat_id] = []  # Reset choices for the next game
#
#     user1_choice = choices[0]
#     user2_choice = choices[1]
#
#     winner = determine_winner(user1_choice, user2_choice)
#
#     if winner == 'user1':
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. Player 1 wins!")
#     elif winner == 'user2':
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. Player 2 wins!")
#     else:
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. It's a tie!")
#
# # Start the bot
# bot.polling()









# import telebot
# from telebot import types
# import random
#
# TOKEN = '6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo'
#
# bot = telebot.TeleBot(TOKEN)
#
# # Dictionary to store user choices for the game between users
# user_choices_users = {}
#
# # Dictionary to store user choices for the game with the bot
# user_choices_bot = {}
#
#
# # Function to determine the winner in rock-paper-scissors game
# def determine_winner(choice1, choice2):
#     if choice1 == choice2:
#         return None  # It's a tie
#     elif (choice1 == "rock 🪨" and choice2 == "scissors ✂️") or \
#             (choice1 == "paper 📃" and choice2 == "rock 🪨") or \
#             (choice1 == "scissors ✂️" and choice2 == "paper 📃"):
#         return 'user1'  # User 1 wins
#     else:
#         return 'user2'  # User 2 wins
#
#
# # Handler for /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('Play with Bot 🤖')
#     itembtn2 = types.KeyboardButton('Play between Users 👥')
#     markup.add(itembtn1, itembtn2)
#     bot.send_message(message.chat.id, "Welcome! Choose an option to play:", reply_markup=markup)
#
#
# # Handler for user's choice to play with the bot
# @bot.message_handler(func=lambda message: message.text == 'Play with Bot 🤖')
# def play_with_bot(message):
#     user_choices_bot[message.chat.id] = []
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('rock 🪨')
#     itembtn2 = types.KeyboardButton('paper 📃')
#     itembtn3 = types.KeyboardButton('scissors ✂️')
#     itembtn4 = types.KeyboardButton('Finish')
#     markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
#     bot.send_message(message.chat.id, "Please select your choice to play with the bot:", reply_markup=markup)
#
#
# # Handler for user's choice to play between users
# @bot.message_handler(func=lambda message: message.text == 'Play between Users 👥')
# def play_between_users(message):
#     user_choices_users[message.chat.id] = []
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('rock 🪨')
#     itembtn2 = types.KeyboardButton('paper 📃')
#     itembtn3 = types.KeyboardButton('scissors ✂️')
#     itembtn4 = types.KeyboardButton('Finish')
#     markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
#     bot.send_message(message.chat.id, "Player 1, please select your choice to play between users:", reply_markup=markup)
#
#
# # Handler for user's choice in the game with the bot
# @bot.message_handler(
#     func=lambda message: message.text.lower() in ['rock 🪨', 'paper 📃', 'scissors ✂️'] and message.chat.id in user_choices_bot)
# def handle_choice_bot(message):
#     user_choice = message.text.lower()
#     bot_choice = random.choice(['rock 🪨', 'paper 📃', 'scissors ✂️'])
#
#     winner = determine_winner(user_choice, bot_choice)
#
#     if winner == 'user1':
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. You win!")
#     elif winner == 'user2':
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. You lose!")
#     else:
#         bot.reply_to(message, f"You chose {user_choice}. Bot chose {bot_choice}. It's a tie!")
#
#
# # Handler for user's choice in the game between users
# @bot.message_handler(func=lambda message: message.text.lower() in ['rock 🪨', 'paper 📃',
#                                                                    'scissors ✂️'] and message.chat.id in user_choices_users)
# def handle_choice_users(message):
#     user_choice = message.text.lower()
#     chat_id = message.chat.id
#
#     if len(user_choices_users[chat_id]) == 0:
#         user_choices_users[chat_id].append(user_choice)
#         markup = types.ReplyKeyboardMarkup(row_width=1)
#         itembtn1 = types.KeyboardButton('rock 🪨')
#         itembtn2 = types.KeyboardButton('paper 📃')
#         itembtn3 = types.KeyboardButton('scissors ✂️')
#         itembtn4 = types.KeyboardButton('Finish')
#         markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
#         bot.send_message(chat_id, "Player 2, please select your choice to play between users:", reply_markup=markup)
#     elif len(user_choices_users[chat_id]) == 1:
#         user_choices_users[chat_id].append(user_choice)
#         play_round_users(chat_id)
#
#
# # Function to play a round of the game between users
# def play_round_users(chat_id):
#     choices = user_choices_users[chat_id]
#     user_choices_users[chat_id] = []  # Reset choices for the next game
#
#     user1_choice = choices[0]
#     user2_choice = choices[1]
#
#     winner = determine_winner(user1_choice, user2_choice)
#
#     if winner == 'user1':
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. Player 1 wins!")
#     elif winner == 'user2':
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. Player 2 wins!")
#     else:
#         bot.send_message(chat_id, f"Player 1 chose {user1_choice}. Player 2 chose {user2_choice}. It's a tie!")
#
#
# # Handler for user's choice to finish the game
# @bot.message_handler(func=lambda message: message.text == 'Finish')
# def finish_game(message):
#     chat_id = message.chat.id
#
#     # Check if the game was with the bot or between users and remove the user's choice data accordingly
#     if chat_id in user_choices_bot:
#         del user_choices_bot[chat_id]
#     elif chat_id in user_choices_users:
#         del user_choices_users[chat_id]
#
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('Play with Bot 🤖')
#     itembtn2 = types.KeyboardButton('Play between Users 👥')
#     markup.add(itembtn1, itembtn2)
#     bot.send_message(chat_id, "choose again please!", reply_markup=markup)
#
#
# # Start the bot
# bot.polling()






#
# import telebot
# from telebot import types
# import random
# import mysql.connector
#
# TOKEN = '6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo'
#
# # Establish MySQL connection
# db_connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="1234"
# )
# cursor = db_connection.cursor()
#
# bot = telebot.TeleBot(TOKEN)
#
#
# # Function to generate a random code
# def generate_code():
#     return ''.join(random.choices('0123456789ABCDEF', k=6))
#
#
# # Handler for /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('Play with Bot 🤖')
#     itembtn2 = types.KeyboardButton('Play between Users 👥')
#     markup.add(itembtn1, itembtn2)
#     bot.send_message(message.chat.id, "Welcome! Choose an option to play:", reply_markup=markup)
#
#
# # Handler for user's choice to play between users
# @bot.message_handler(func=lambda message: message.text == 'Play between Users 👥')
# def play_between_users(message):
#     # Generate a random code for the game session
#     game_code = generate_code()
#
#     # Store the game code and user's chat ID in the database
#     cursor.execute("INSERT INTO game_sessions (code, user1_chat_id) VALUES (%s, %s)", (game_code, message.chat.id))
#     db_connection.commit()
#
#     bot.send_message(message.chat.id, f"Share this code with the second user: {game_code}")
#
#
# # Handler for the second user entering the game code
# @bot.message_handler(func=lambda message: message.text.startswith('Code: '))
# def enter_code(message):
#     game_code = message.text[6:]  # Extract the code from the message
#
#     # Check if the code exists in the database
#     cursor.execute("SELECT user1_chat_id FROM game_sessions WHERE code = %s", (game_code,))
#     result = cursor.fetchone()
#
#     if result:
#         user1_chat_id = result[0]
#         user2_chat_id = message.chat.id
#
#         markup = types.ReplyKeyboardMarkup(row_width=1)
#         itembtn = types.KeyboardButton('Yes')
#         markup.add(itembtn)
#         bot.send_message(user1_chat_id, f"The second user wants to play. Do you want to play?", reply_markup=markup)
#
#         # Store the chat IDs of both users in the database
#         cursor.execute("UPDATE game_sessions SET user2_chat_id = %s WHERE code = %s", (user2_chat_id, game_code))
#         db_connection.commit()
#     else:
#         bot.send_message(message.chat.id, "Invalid code. Please enter a valid code.")
#
#
# # Handler for user's response to play
# @bot.message_handler(func=lambda message: message.text == 'Yes')
# def play(message):
#     bot.send_message(message.chat.id, "Game started!")
#
#
# # Start the bot
# bot.polling()


# import telebot
# from telebot import types
# import random
# import mysql.connector
# from mysql.connector import Error
#
# API_TOKEN = '6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo'
# bot = telebot.TeleBot(API_TOKEN)
#
# def create_connection():
#     return mysql.connector.connect(
#         host='127.0.0.1',
#         database='game',
#         user='root',
#         password='1234'
#     )
#
# def create_table():
#     connection = create_connection()
#     try:
#         cursor = connection.cursor()
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS game_results (
#             game_no INT AUTO_INCREMENT PRIMARY KEY,
#             user_id BIGINT,
#             opponent_id BIGINT,
#             username VARCHAR(255),
#             opponent_username VARCHAR(255),
#             winner VARCHAR(255),
#             user_score INT,
#             opponent_score INT,
#             tie BOOLEAN,
#             game_time_seconds INT,
#             game_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             game_end TIMESTAMP
#         )""")
#         connection.commit()
#     finally:
#         cursor.close()
#         connection.close()
#
# create_table()
#
# choices = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
# user_game_states = {}
# user_queue = []
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row(types.KeyboardButton('Play 🤖'), types.KeyboardButton('Challenge 👥'))
#     markup.row(types.KeyboardButton('Records 📊'), types.KeyboardButton('Analytics 📈'))
#     bot.send_message(message.chat.id, "Welcome! Ready to play Rock, Paper, Scissors?", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == 'Records 📊')
# def show_records(message):
#     send_statistics(message)
#
# @bot.message_handler(func=lambda message: message.text == 'Analytics 📈')
# def show_analytics(message):
#     send_analytics(message)
#
# def send_statistics(message):
#     user_id = message.from_user.id
#     stats = fetch_statistics(user_id)
#     if stats and stats['total_games'] > 0:
#         response = (f"📊 Your Game Statistics 📊\n"
#                     f"Total Games: {stats['total_games']}\n"
#                     f"Wins: {stats['wins']}\n"
#                     f"Losses: {stats['losses']}\n"
#                     f"Ties: {stats['ties']}")
#     else:
#         response = "No game statistics available. Start playing to gather data!"
#     bot.send_message(message.chat.id, response)
#
# def fetch_statistics(user_id):
#     connection = create_connection()
#     try:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("""
#             SELECT
#                 COUNT(*) AS total_games,
#                 SUM(CASE WHEN winner = %s THEN 1 ELSE 0 END) AS wins,
#                 SUM(CASE WHEN winner != %s AND winner != 'Tie' THEN 1 ELSE 0 END) AS losses,
#                 SUM(CASE WHEN tie = TRUE THEN 1 ELSE 0 END) AS ties
#             FROM game_results
#             WHERE user_id = %s
#         """, (user_id, user_id, user_id))
#         stats = cursor.fetchone()
#         return stats if stats else {'total_games': 0, 'wins': 0, 'losses': 0, 'ties': 0}
#     finally:
#         cursor.close()
#         connection.close()
#
# def send_analytics(message):
#     user_id = message.from_user.id
#     analytics = fetch_analytics(user_id)
#     if analytics:
#         response = (f"📈 Detailed Analytics 📈\n"
#                     f"Highest Score: {analytics['highest_score']}\n"
#                     f"Lowest Score: {analytics['lowest_score']}\n"
#                     f"Average Score: {analytics['average_score']:.2f}\n"
#                     f"Total Games: {analytics['total_games']}")
#     else:
#         response = "No detailed analytics available. Start playing to gather data!"
#     bot.send_message(message.chat.id, response)
#
#
# def fetch_analytics(user_id):
#     connection = create_connection()
#     try:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("""
#             SELECT
#                 MAX(user_score) AS highest_score,
#                 MIN(user_score) AS lowest_score,
#                 AVG(user_score) AS average_score,
#                 COUNT(*) AS total_games
#             FROM game_results
#             WHERE user_id = %s
#         """, (user_id,))
#         analytics = cursor.fetchone()
#         return analytics if analytics['total_games'] > 0 else None
#     finally:
#         cursor.close()
#         connection.close()
#
# @bot.message_handler(func=lambda message: message.text in ['Play 🤖', 'Challenge 👥'])
# def game_setup(message):
#     user_id = message.from_user.id
#     chat_id = message.chat.id
#     mode = 'AI' if message.text == 'Play 🤖' else 'PvP'
#     opponent_id = 'AI' if mode == 'AI' else None
#
#     if mode == 'PvP':
#         if len(user_queue) > 0:
#             opponent_id = user_queue.pop(0)
#         else:
#             user_queue.append(user_id)
#             bot.send_message(chat_id, "You're in the queue. Waiting for another player.")
#             return
#
#     user_game_states[user_id] = {'opponent': opponent_id, 'user_score': 0, 'opponent_score': 0, 'round': 1, 'chat_id': chat_id}
#     if opponent_id != 'AI':
#         user_game_states[opponent_id] = {'opponent': user_id, 'user_score': 0, 'opponent_score': 0, 'round': 1, 'chat_id': bot.get_chat(opponent_id).id}
#         bot.send_message(user_game_states[opponent_id]['chat_id'], "Your match is ready!")
#         send_options(user_game_states[opponent_id]['chat_id'])
#
#     send_options(chat_id)
#
# def send_options(chat_id):
#     markup = types.InlineKeyboardMarkup()
#     for key, emoji in choices.items():
#         markup.add(types.InlineKeyboardButton(text=f"{emoji} {key}", callback_data=key))
#     bot.send_message(chat_id, "Choose Rock, Paper, or Scissors:", reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: call.data in choices)
# def handle_choice(call):
#     user_id = call.from_user.id
#     chat_id = call.message.chat.id
#     user_move = call.data
#     user_state = user_game_states.get(user_id)
#
#     if user_state['opponent'] == 'AI':
#         opponent_move = random.choice(list(choices.keys()))
#         result = determine_winner(user_move, opponent_move)
#         update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result, ai=True)
#     else:
#         opponent_id = user_state['opponent']
#         opponent_state = user_game_states.get(opponent_id)
#         opponent_move = opponent_state.get('move', None)
#         if opponent_move:
#             result = determine_winner(user_move, opponent_move)
#             update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result)
#             update_scores_and_respond(opponent_id, opponent_state['chat_id'], opponent_move, user_move, 'opponent' if result == 'user' else 'user')
#             opponent_state.pop('move', None)
#             user_state.pop('move', None)
#         else:
#             user_state['move'] = user_move
#             bot.answer_callback_query(call.id, "Move recorded. Waiting for your opponent.")
#
# def determine_winner(user_move, opponent_move):
#     rules = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
#     if user_move == opponent_move:
#         return 'tie'
#     elif rules[user_move] == opponent_move:
#         return 'user'
#     else:
#         return 'opponent'
#
# def update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result, ai=False):
#     user = user_game_states[user_id]
#     user['user_score'] += 1 if result == 'user' else 0
#     user['opponent_score'] += 1 if result == 'opponent' else 0
#     round_end_msg = "Round over! " if user['round'] == 3 else ""
#
#     message = f"{round_end_msg}Your move: {choices[user_move]} vs. Opponent's move: {choices[opponent_move]}"
#     if result == 'user':
#         message += " You win this round! 🎉"
#     elif result == 'opponent':
#         message += " You lose this round! 😢"
#     else:
#         message += " It's a tie! 😐"
#
#
#     bot.send_message(chat_id, message)
#     if user['round'] >= 3:
#         finalize_game(user_id, 'AI' if ai else user['opponent'])
#     else:
#         user['round'] += 1
#         send_options(chat_id)
#
# def finalize_game(user_id, opponent):
#     user = user_game_states[user_id]
#     chat_id = user['chat_id']
#     user_score = user['user_score']
#     opponent_score = user['opponent_score']
#     if opponent == 'AI':
#         winner = 'User' if user_score > opponent_score else 'AI' if user_score < opponent_score else 'Tie'
#         save_game_results_to_db(user_id, bot.get_chat(user_id).username, None, 'AI', winner, user_score, opponent_score)
#     else:
#         opponent_data = user_game_states[opponent]
#         opponent_chat_id = opponent_data['chat_id']
#         winner = 'User' if user_score > opponent_score else 'Opponent' if user_score < opponent_score else 'Tie'
#         save_game_results_to_db(user_id, bot.get_chat(user_id).username, opponent, bot.get_chat(opponent).username, winner, user_score, opponent_score)
#         bot.send_message(opponent_chat_id, f"Game over! Final score - You: {opponent_score}, Opponent: {user_score}. Winner: {winner} 🏆")
#         user_game_states.pop(opponent, None)
#
#     bot.send_message(chat_id, f"Game over! Final score - You: {user_score}, Opponent: {'AI' if opponent == 'AI' else opponent_score}. Winner: {winner} 🎆")
#     user_game_states.pop(user_id, None)
#
# def save_game_results_to_db(user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score):
#     connection = create_connection()
#     cursor = connection.cursor()
#     try:
#         cursor.execute(
#             "INSERT INTO game_results (user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#             (user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score))
#         connection.commit()
#     finally:
#         cursor.close()
#         connection.close()
#
# bot.polling()
# # 6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo
#
import telebot
from telebot import types
import random
import mysql.connector
from mysql.connector import Error

API_TOKEN = '6543371995:AAGySQpdM8Vvhu7wnkYMJ9fw5nMmvIPSlfo'
bot = telebot.TeleBot(API_TOKEN)

def create_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        database='game',
        user='root',
        password='1234'
    )

def create_table():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_results (
            game_no INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT,
            opponent_id BIGINT,
            username VARCHAR(255),
            opponent_username VARCHAR(255),
            winner VARCHAR(255),
            user_score INT,
            opponent_score INT,
            tie BOOLEAN,
            game_time_seconds INT,
            game_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            game_end TIMESTAMP
        )""")
        connection.commit()
    finally:
        cursor.close()
        connection.close()

create_table()

choices = {"Rock": "🪨", "Paper": "📃", "Scissors": "✂️"}
user_game_states = {}
user_queue = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('play with bot 🤖'), types.KeyboardButton('play with users 👥'))
    markup.row(types.KeyboardButton('total '), types.KeyboardButton('Analytics '))
    bot.send_message(message.chat.id, "Welcome! Ready to play Rock, Paper, Scissors?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Records ')
def show_records(message):
    send_statistics(message)

@bot.message_handler(func=lambda message: message.text == 'Analytics ')
def show_analytics(message):
    send_analytics(message)

def send_statistics(message):
    user_id = message.from_user.id
    stats = fetch_statistics(user_id)
    if stats and stats['total_games'] > 0:
        response = (f" Your Game Statistics \n"
                    f"Total Games: {stats['total_games']}\n"
                    f"Wins: {stats['wins']}\n"
                    f"Losses: {stats['losses']}\n"
                    f"Ties: {stats['ties']}")
    else:
        response = "No game statistics available. Start playing to gather data!"
    bot.send_message(message.chat.id, response)

def fetch_statistics(user_id):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                COUNT(*) AS total_games,
                SUM(CASE WHEN winner = %s THEN 1 ELSE 0 END) AS wins,
                SUM(CASE WHEN winner != %s AND winner != 'Tie' THEN 1 ELSE 0 END) AS losses,
                SUM(CASE WHEN tie = TRUE THEN 1 ELSE 0 END) AS ties
            FROM game_results
            WHERE user_id = %s
        """, (user_id, user_id, user_id))
        stats = cursor.fetchone()
        return stats if stats else {'total_games': 0, 'wins': 0, 'losses': 0, 'ties': 0}
    finally:
        cursor.close()
        connection.close()

def send_analytics(message):
    user_id = message.from_user.id
    analytics = fetch_analytics(user_id)
    if analytics:
        response = (f" Detailed Analytics \n"
                    f"Highest Score: {analytics['highest_score']}\n"
                    f"Lowest Score: {analytics['lowest_score']}\n"
                    f"Average Score: {analytics['average_score']:.2f}\n"
                    f"Total Games: {analytics['total_games']}")
    else:
        response = "No detailed analytics available. Start playing to gather data!"
    bot.send_message(message.chat.id, response)


def fetch_analytics(user_id):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                MAX(user_score) AS highest_score,
                MIN(user_score) AS lowest_score,
                AVG(user_score) AS average_score,
                COUNT(*) AS total_games
            FROM game_results
            WHERE user_id = %s
        """, (user_id,))
        analytics = cursor.fetchone()
        return analytics if analytics['total_games'] > 0 else None
    finally:
        cursor.close()
        connection.close()

@bot.message_handler(func=lambda message: message.text in ['play with bot 🤖', 'play with users 👥'])
def game_setup(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    mode = 'AI' if message.text == 'play with bot 🤖' else 'PvP'
    opponent_id = 'AI' if mode == 'AI' else None

    if mode == 'PvP':
        if len(user_queue) > 0:
            opponent_id = user_queue.pop(0)
        else:
            user_queue.append(user_id)
            bot.send_message(chat_id, "You're in the queue. Waiting for another player.")
            return

    user_game_states[user_id] = {'opponent': opponent_id, 'user_score': 0, 'opponent_score': 0, 'round': 1, 'chat_id': chat_id}
    if opponent_id != 'AI':
        user_game_states[opponent_id] = {'opponent': user_id, 'user_score': 0, 'opponent_score': 0, 'round': 1, 'chat_id': bot.get_chat(opponent_id).id}
        bot.send_message(user_game_states[opponent_id]['chat_id'], "Your match is ready!")
        send_options(user_game_states[opponent_id]['chat_id'])

    send_options(chat_id)

def send_options(chat_id):
    markup = types.InlineKeyboardMarkup()
    for key, emoji in choices.items():
        markup.add(types.InlineKeyboardButton(text=f"{emoji} {key}", callback_data=key))
    bot.send_message(chat_id, "Choose Rock, Paper, or Scissors:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in choices)
def handle_choice(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    user_move = call.data
    user_state = user_game_states.get(user_id)

    if user_state['opponent'] == 'AI':
        opponent_move = random.choice(list(choices.keys()))
        result = determine_winner(user_move, opponent_move)
        update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result, ai=True)
    else:
        opponent_id = user_state['opponent']
        opponent_state = user_game_states.get(opponent_id)
        opponent_move = opponent_state.get('move', None)
        if opponent_move:
            result = determine_winner(user_move, opponent_move)
            update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result)
            update_scores_and_respond(opponent_id, opponent_state['chat_id'], opponent_move, user_move, 'opponent' if result == 'user' else 'user')
            opponent_state.pop('move', None)
            user_state.pop('move', None)
        else:
            user_state['move'] = user_move
            bot.answer_callback_query(call.id, "Move recorded. Waiting for your opponent.")

def determine_winner(user_move, opponent_move):
    rules = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
    if user_move == opponent_move:
        return 'tie'
    elif rules[user_move] == opponent_move:
        return 'user'
    else:
        return 'opponent'

def update_scores_and_respond(user_id, chat_id, user_move, opponent_move, result, ai=False):
    user = user_game_states[user_id]
    user['user_score'] += 1 if result == 'user' else 0
    user['opponent_score'] += 1 if result == 'opponent' else 0
    round_end_msg = "Round over! " if user['round'] == 3 else ""

    message = f"{round_end_msg}Your move: {choices[user_move]} vs. Opponent's move: {choices[opponent_move]}"
    if result == 'user':
        message += " You win this round! 🎉"
    elif result == 'opponent':
        message += " You lose this round!"
    else:
        message += " It's a tie!"


    bot.send_message(chat_id, message)
    if user['round'] >= 3:
        finalize_game(user_id, 'AI' if ai else user['opponent'])
    else:
        user['round'] += 1
        send_options(chat_id)

def finalize_game(user_id, opponent):
    user = user_game_states[user_id]
    chat_id = user['chat_id']
    user_score = user['user_score']
    opponent_score = user['opponent_score']
    if opponent == 'AI':
        winner = 'User' if user_score > opponent_score else 'AI' if user_score < opponent_score else 'Tie'
        save_game_results_to_db(user_id, bot.get_chat(user_id).username, None, 'AI', winner, user_score, opponent_score)
    else:
        opponent_data = user_game_states[opponent]
        opponent_chat_id = opponent_data['chat_id']
        winner = 'User' if user_score > opponent_score else 'Opponent' if user_score < opponent_score else 'Tie'
        save_game_results_to_db(user_id, bot.get_chat(user_id).username, opponent, bot.get_chat(opponent).username, winner, user_score, opponent_score)
        bot.send_message(opponent_chat_id, f"Game over! Final score - You: {opponent_score}, Opponent: {user_score}. Winner: {winner} 🏆")
        user_game_states.pop(opponent, None)

    bot.send_message(chat_id, f"Game over! Final score - You: {user_score}, Opponent: {'AI' if opponent == 'AI' else opponent_score}. Winner: {winner} 🎆")
    user_game_states.pop(user_id, None)

def save_game_results_to_db(user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO game_results (user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, username, opponent_id, opponent_username, winner, user_score, opponent_score))
        connection.commit()
    finally:
        cursor.close()
        connection.close()

bot.polling()

