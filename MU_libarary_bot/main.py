import json
import types
#
# import json
# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# # Load book data from JSON
# try:
#     with open("books.json", "r") as file:
#         books_data = json.load(file)
# except FileNotFoundError:
#     print("Error: books.json file not found.")
#     exit()
# except json.JSONDecodeError:
#     print("Error: Invalid JSON format in books.json.")
#     exit()
#
# # Initialize the Telegram Bot with your bot token
# bot = telebot.TeleBot("7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s")
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query):
#     results = []
#     for book in books_data['books']:
#         if query.lower() in book['title'].lower() or \
#            query.lower() in book['isbn'].lower() or \
#            query.lower() in book['author'].lower():
#             results.append(book)
#     return results
#
# # Function to handle the /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = ReplyKeyboardMarkup(row_width=1)
#     search_title_btn = KeyboardButton('/search_title')
#     search_isbn_btn = KeyboardButton('/search_isbn')
#     search_author_btn = KeyboardButton('/search_author')
#     markup.add(search_title_btn, search_isbn_btn, search_author_btn)
#     bot.send_message(message.chat.id, "Choose an option to search:", reply_markup=markup)
#
#
# @bot.message_handler(commands=['search_title'])
# def search_title(message):
#     bot.send_message(message.chat.id, "Enter the title of the book you want to search for:")
# @bot.message_handler(commands=["search_title"])
# @bot.message_handler(commands=["search_title"])
#
# # Function to handle the search ISBN command
# @bot.message_handler(commands=['search_isbn'])
# def search_isbn(message):
#     bot.send_message(message.chat.id, "Enter the ISBN of the book you want to search for:")
#
# # Function to handle the search author command
# @bot.message_handler(commands=['search_author'])
# def search_author(message):
#     bot.send_message(message.chat.id, "Enter the name of the author you want to search for:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.startswith('/search_title'):
#         query = message.text.replace('/search_title', '').strip()
#     elif message.text.startswith('/search_isbn'):
#         query = message.text.replace('/search_isbn', '').strip()
#     elif message.text.startswith('/search_author'):
#         query = message.text.replace('/search_author', '').strip()
#     else:
#         query = message.text.strip()
#
#     results = search_book(query)
#     if results:
#         for book in results:
#             if 'image' in book:
#                 image_path = book['image']
#                 try:
#                     with open(image_path, 'rb') as image:
#                         bot.send_photo(message.chat.id, image, caption=f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#                 except Exception as e:
#                     print(f"Error sending photo: {e}")
#             else:
#                 bot.send_message(message.chat.id, f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#     else:
#         bot.send_message(message.chat.id, "No books found matching your query.")
#
# # Start the bot
# bot.polling()









# import telebot
# import requests
#
# # Initialize your bot with your Telegram bot token
# bot = telebot.TeleBot("7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s")
#
#
# # Function to handle the /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message,
#                  "Hi! Send me the title, author, ISBN, or ID of a book, and I will provide information about it.")
#
#
# # Function to handle normal text messages
# @bot.message_handler(func=lambda message: True)
# def get_book_info(message):
#     search_query = message.text
#
#     try:
#         if search_query.startswith('author:'):
#             author_name = search_query.split(':')[1].strip()
#             response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{author_name}", timeout=10)
#         else:
#             response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search_query}", timeout=10)
#
#         if response.status_code == 200:
#             data = response.json()
#             if 'items' in data:
#                 books_info = data['items']
#                 for book_item in books_info:
#                     book_info = book_item['volumeInfo']
#                     title = book_info.get('title', 'Title not available')
#                     authors = book_info.get('authors', ['Author not available'])
#                     description = book_info.get('description', 'Description not available')[
#                                   :200]  # Truncate description to 200 characters
#                     isbn = \
#                     book_info.get('industryIdentifiers', [{'type': 'ISBN', 'identifier': 'ISBN not available'}])[0][
#                         'identifier']
#                     page_count = book_info.get('pageCount', 'Page count not available')
#                     categories = book_info.get('categories', 'Categories not available')
#                     language = book_info.get('language', 'Language not available')
#                     published_date = book_info.get('publishedDate', 'Published date not available')
#                     image_links = book_info.get('imageLinks', {})
#                     image_url = image_links.get('thumbnail', None)
#
#                     response_text = f"Title: {title}\nAuthors: {', '.join(authors)}\nDescription: {description}\nISBN: {isbn}\nPage Count: {page_count}\nCategories: {', '.join(categories)}\nLanguage: {language}\nPublished Date: {published_date}"
#
#                     bot.send_photo(message.chat.id, image_url, caption=response_text)
#             else:
#                 response_text = "No books found with the given search terms."
#                 bot.reply_to(message, response_text)
#         else:
#             response_text = "Error accessing the Google Books API."
#             bot.reply_to(message, response_text)
#     except requests.exceptions.Timeout:
#         bot.reply_to(message,
#                      "Sorry, there was a timeout while accessing the Google Books API. Please try again later.")
#
#
# # Start the bot
# bot.polling()


import telebot
# import json
# import zipfile
#
# with open('books.json', 'r') as file:
#     data = json.load(file)
#
# # Initialize the bot
# TOKEN = '6986251787:AAHySNmV4o4nxL8pXMMCIz0TJhuVx9KCC0Q'
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['books'])
# def send_books(message):
#     bot.send_message(message.chat.id, "Please enter the title, author, or ISBN of the book you are searching for:")
#     bot.register_next_step_handler(message, process_book_search)
#
# def process_book_search(message):
#     search_query = message.text.lower()
#     found_books = []
#     for book in data['books']:
#         if search_query in book['title'].lower() or search_query in book['author'].lower() or search_query == book['isbn']:
#             book_info = f"Title: {book['title']}\n" \
#                         f"Author: {book['author']}\n" \
#                         f"ISBN: {book['isbn']}\n" \
#                         f"Available: {'Yes' if book['available'] else 'No'}\n" \
#                         f"Location: {book['location']}\n"
#             if 'image' in book:
#                 image_path = book['image']
#                 with open(image_path, 'rb') as image:
#                     try:
#                         bot.send_photo(message.chat.id, image,  timeout=60)
#                     except Exception as e:
#                         print(f"Error sending photo: {e}")
#             if 'pdf' in book:
#                 pdf_path = book['pdf']
#                 if zipfile.is_zipfile(pdf_path):
#                     with zipfile.ZipFile(pdf_path, 'r') as z:
#                         pdf_filename = z.namelist()[0]
#                         with z.open(pdf_filename) as pdf:
#                             try:
#                                 bot.send_document(message.chat.id, pdf, caption=book_info, timeout=60)
#                             except Exception as e:
#                                 print(f"Error sending document: {e}")
#                 else:
#                     with open(pdf_path, 'rb') as pdf:
#                         try:
#                             bot.send_document(message.chat.id, pdf, caption=book_info, timeout=60)
#                         except Exception as e:
#                             print(f"Error sending document: {e}")
#             else:
#                 bot.send_message(message.chat.id, book_info)
#             found_books.append(book_info)
#
#     if not found_books:
#         bot.send_message(message.chat.id, "Book not found.")
#
# bot.polling(none_stop=True, timeout=


# Start Menu Functionality: send initial options
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
#     keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
#     telebot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     # keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     # mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     # world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     # amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     # keyboard.add(mu_library_button, world_book_button,amazon_books_button)
#     channel_link = "https://t.me/MillatUmidi_library"
#     join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
#                    f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
#                    f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
#     bot.reply_to(message,join_message)
#     start_menu(message.chat.id)
# @bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
# def mu_library_meesage(message):
#     with open("mu_lib (1).png", "rb") as image_file:
#         bot.send_photo(message.chat.id, image_file.read())
#     mu_library_options(message)
# def mu_library_options(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     register_button = types.KeyboardButton("✅ REGISTER 📝")
#     books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
#     books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
#     back_button = types.KeyboardButton("Back ↩️")
#     keyboard.add(register_button,books_mu_library,books_mu_faculty,back_button)
#     bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University",reply_markup=keyboard)
#
# # Load book data from JSON
# try:
#     with open("books.json", "r") as file:
#         books_data = json.load(file)
#         if not isinstance(books_data, list):
#             raise TypeError("Invalid JSON format: books.json should contain a list of dictionaries.")
# except FileNotFoundError:
#     print("Error: books.json file not found.")
#     exit()
# except json.JSONDecodeError:
#     print("Error: Invalid JSON format in books.json.")
#     exit()
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query, field):
#     results = []
#     for book in books_data:
#         if query.lower() in book[field].lower():
#             results.append(book)
#     return results
#
# # Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
# @bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
# def books_in_mu_library(message):
#     keyboard = types.InlineKeyboardMarkup()
#     search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
#     search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
#     search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
#     keyboard.add(search_title, search_author, search_isbn)
#     bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)
#
# # Callback query handler for initiating book search
# @bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
# def search_by(call):
#     field = call.data.split('_')[-1]
#     if field == 'title':
#         bot.send_message(call.message.chat.id, "Please enter the title of the book:")
#     elif field == 'author':
#         bot.send_message(call.message.chat.id, "Please enter the author of the book:")
#     elif field == 'isbn':
#         bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.startswith("Please enter"):
#         field = message.text.split("Please enter ")[1].split(" ")[0].lower()
#         query = message.text.split("Please enter ")[1].split(" of the book:")[1].strip()
#         results = search_book(query, field)
#         if results:
#             for book in results:
#                 caption = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 if 'image' in book:
#                     image_path = book['image']
#                     with open(image_path, 'rb') as image:
#                         bot.send_photo(message.chat.id, image, caption=caption)
#                 else:
#                     bot.send_message(message.chat.id, caption)
#         else:
#             bot.send_message(message.chat.id, "No books found matching your query.")


# import telebot
# from telebot import types
# import json
#
# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot('7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s')
#
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
#     keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
#     bot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     channel_link = "https://t.me/MillatUmidi_library"
#     join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
#                    f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
#                    f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
#     bot.send_message(message.chat.id, join_message)
#     start_menu(message.chat.id)
#
# @bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
# def mu_library_message(message):
#     with open("1.jpg", "rb") as image_file:
#         bot.send_photo(message.chat.id, image_file.read())
#     mu_library_options(message)
#
# def mu_library_options(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     register_button = types.KeyboardButton("✅ REGISTER 📝")
#     books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
#     books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
#     back_button = types.KeyboardButton("Back ↩️")
#     keyboard.add(register_button, books_mu_library, books_mu_faculty, back_button)
#     bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University", reply_markup=keyboard)
#
# # Load book data from JSON
# try:
#     with open("books.json", "r") as file:
#         books_data = json.load(file)
#         if not isinstance(books_data, list):
#             raise TypeError("Invalid JSON format: books.json should contain a list of dictionaries.")
# except FileNotFoundError:
#     print("Error: books.json file not found.")
# except json.JSONDecodeError:
#     print("Error: Invalid JSON format in books.json.")
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query, field):
#     results = []
#     for book in books_data:
#         if query.lower() in book[field].lower():
#             results.append(book)
#     return results
#
# # Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
# @bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
# def books_in_mu_library(message):
#     keyboard = types.InlineKeyboardMarkup()
#     search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
#     search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
#     search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
#     keyboard.add(search_title, search_author, search_isbn)
#     bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)
#
# # Callback query handler for initiating book search
# @bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
# def search_by(call):
#     field = call.data.split('_')[-1]
#     if field == 'title':
#         bot.send_message(call.message.chat.id, "Please enter the title of the book:")
#     elif field == 'author':
#         bot.send_message(call.message.chat.id, "Please enter the author of the book:")
#     elif field == 'isbn':
#         bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.startswith("Please enter"):
#         field = message.text.split("Please enter ")[1].split(" ")[0].lower()
#         query = message.text.split("Please enter ")[1].split(" of the book:")[1].strip()
#         results = search_book(query, field)
#         if results:
#             for book in results:
#                 caption = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 if 'image' in book:
#                     image_path = book['image']
#                     with open(image_path, 'rb') as image:
#                         bot.send_photo(message.chat.id, image, caption=caption)
#                 else:
#                     bot.send_message(message.chat.id, caption)
#         else:
#             bot.send_message(message.chat.id, "No books found matching your query.")
#
# # Start the bot
# bot.polling()
#
# import telebot
# from telebot import types
# import json
# import time
#
# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot('7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s')
#
# # Flag to ensure only one instance of the bot is running
# running = True
#
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
#     keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
#     bot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     channel_link = "https://t.me/MillatUmidi_library"
#     join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
#                    f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
#                    f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
#     bot.send_message(message.chat.id, join_message)
#     start_menu(message.chat.id)
#
# @bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
# def mu_library_message(message):
#     with open("photo_2024-05-13_20-24-25.jpg", "rb") as image_file:
#         bot.send_photo(message.chat.id, image_file.read())
#     mu_library_options(message)
#
# def mu_library_options(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     register_button = types.KeyboardButton("✅ REGISTER 📝")
#     books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
#     books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
#     back_button = types.KeyboardButton("Back ↩️")
#     keyboard.add(register_button, books_mu_library, books_mu_faculty, back_button)
#     bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University", reply_markup=keyboard)
#
# # Load book data from JSON
# def load_books_data():
#     try:
#         with open("books.json", "r") as file:
#             books_data = json.load(file)
#             if not isinstance(books_data, list):
#                 raise TypeError("Invalid JSON format: books.json should contain a list of dictionaries.")
#         return books_data
#     except FileNotFoundError:
#         print("Error: books.json file not found.")
#     except json.JSONDecodeError:
#         print("Error: Invalid JSON format in books.json.")
#     return []
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query, field, books_data):
#     results = []
#     for book in books_data:
#         if query.lower() in book[field].lower():
#             results.append(book)
#     return results
#
# # Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
# @bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
# def books_in_mu_library(message):
#     keyboard = types.InlineKeyboardMarkup()
#     search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
#     search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
#     search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
#     keyboard.add(search_title, search_author, search_isbn)
#     bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)
#
# # Callback query handler for initiating book search
# @bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
# def search_by(call):
#     field = call.data.split('_')[-1]
#     if field == 'title':
#         bot.send_message(call.message.chat.id, "Please enter the title of the book:")
#     elif field == 'author':
#         bot.send_message(call.message.chat.id, "Please enter the author of the book:")
#     elif field == 'isbn':
#         bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     global running  # Use the global variable
#     if message.text.startswith("Please enter"):
#         field = message.text.split("Please enter ")[1].split(" ")[0].lower()
#         query = message.text.split("Please enter ")[1].split(" of the book:")[1].strip()
#         books_data = load_books_data()
#         results = search_book(query, field, books_data)
#         if results:
#             for book in results:
#                 book_info = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 bot.send_message(message.chat.id, book_info)
#         else:
#             bot.send_message(message.chat.id, "No books found matching your query.")
#     running = False  # Stop the bot after processing the message
# bot.polling()



# # Start the bot with connection retries
# # while running:
# #     try:
# #         bot.polling(none_stop=False)
# #     except Exception as e:
# #         print(f"Error occurred: {e}")
# #         print("Retrying in 10 seconds...")
# #         time.sleep(10)

# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# import json
#
# # Load book data from JSON
# try:
#     with open("books.json", "r") as file:
#         books_data = json.load(file)
# except FileNotFoundError:
#     print("Error: books.json file not found.")
#     exit()
# except json.JSONDecodeError:
#     print("Error: Invalid JSON format in books.json.")
#     exit()
#
# # Initialize the Telegram Bot with your bot token
# bot = telebot.TeleBot("7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s")
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query, field):
#     results = []
#     for book in books_data['books']:
#         if query.lower() in book[field].lower():
#             results.append(book)
#     return results
#
# # Function to handle the /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = ReplyKeyboardMarkup(row_width=1)
#     search_title_btn = KeyboardButton('/search_title')
#     search_isbn_btn = KeyboardButton('/search_isbn')
#     search_author_btn = KeyboardButton('/search_author')
#     markup.add(search_title_btn, search_isbn_btn, search_author_btn)
#     bot.send_message(message.chat.id, "Choose an option to search:", reply_markup=markup)
#
# # Function to handle the search title command
# @bot.message_handler(commands=['search_title'])
# def search_title(message):
#     bot.send_message(message.chat.id, "Enter the title of the book you want to search for:")
#
# # Function to handle the search ISBN command
# @bot.message_handler(commands=['search_isbn'])
# def search_isbn(message):
#     bot.send_message(message.chat.id, "Enter the ISBN of the book you want to search for:")
#
# # Function to handle the search author command
# @bot.message_handler(commands=['search_author'])
# def search_author(message):
#     bot.send_message(message.chat.id, "Enter the name of the author you want to search for:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.startswith('/search_title'):
#         query = message.text.replace('/search_title', '').strip()
#         field = 'title'
#     elif message.text.startswith('/search_isbn'):
#         query = message.text.replace('/search_isbn', '').strip()
#         field = 'isbn'
#     elif message.text.startswith('/search_author'):
#         query = message.text.replace('/search_author', '').strip()
#         field = 'author'
#     else:
#         query = message.text.strip()
#         field = 'title'  # Default to title search if no specific command is given
#
#     results = search_book(query, field)
#     if results:
#         for book in results:
#             if 'image' in book:
#                 image_path = book['image']
#                 try:
#                     with open(image_path, 'rb') as image:
#                         bot.send_photo(message.chat.id, image, caption=f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#                 except Exception as e:
#                     print(f"Error sending photo: {e}")
#             else:
#                 bot.send_message(message.chat.id, f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#     else:
#         bot.send_message(message.chat.id, "No books found matching your query.")
#
# # Start the bot
# bot.polling()
#

#
# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# import json
#
# # Load book data from JSON
# try:
#     with open("books.json", "r") as file:
#         books_data = json.load(file)
# except FileNotFoundError:
#     print("Error: books.json file not found.")
#     exit()
# except json.JSONDecodeError:
#     print("Error: Invalid JSON format in books.json.")
#     exit()
#
# # Initialize the Telegram Bot with your bot token
# bot = telebot.TeleBot("7031144721:AAEUW58qenrejdeEfxiHLnFYSHhZ1aPehaU")
#
# # Introduction message
# intro_message = """
# Hello! Welcome to the Book Search Bot. You can use this bot to search for books by title, author, or ISBN.
# To get started, simply click one of the buttons below to choose how you want to search for books:
# """
#
# # Function to search for a book by title, ISBN, or author
# def search_book(query, field):
#     results = []
#     for book in books_data['books']:
#         if query.lower() in book[field].lower():
#             results.append(book)
#     return results
#
# # Function to handle the /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = ReplyKeyboardMarkup(row_width=1)
#     search_title_btn = KeyboardButton('/search_title')
#     search_isbn_btn = KeyboardButton('/search_isbn')
#     search_author_btn = KeyboardButton('/search_author')
#     markup.add(search_title_btn, search_isbn_btn, search_author_btn)
#     bot.send_message(message.chat.id, intro_message, reply_markup=markup)
#
# # Function to handle the search title command
# @bot.message_handler(commands=['search_title'])
# def search_title(message):
#     bot.send_message(message.chat.id, "Enter the title of the book you want to search for:")
#
# # Function to handle the search ISBN command
# @bot.message_handler(commands=['search_isbn'])
# def search_isbn(message):
#     bot.send_message(message.chat.id, "Enter the ISBN of the book you want to search for:")
#
# # Function to handle the search author command
# @bot.message_handler(commands=['search_author'])
# def search_author(message):
#     bot.send_message(message.chat.id, "Enter the name of the author you want to search for:")
#
# # Function to handle user messages for searching
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.startswith('/search_title'):
#         query = message.text.replace('/search_title', '').strip()
#         field = 'title'
#     elif message.text.startswith('/search_isbn'):
#         query = message.text.replace('/search_isbn', '').strip()
#         field = 'isbn'
#     elif message.text.startswith('/search_author'):
#         query = message.text.replace('/search_author', '').strip()
#         field = 'author'
#     else:
#         query = message.text.strip()
#         field = 'title'  # Default to title search if no specific command is given
#
#     results = search_book(query, field)
#     if results:
#         for book in results:
#             if 'image' in book:
#                 image_path = book['image']
#                 try:
#                     with open(image_path, 'rb') as image:
#                         bot.send_photo(message.chat.id, image, caption=f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#                 except Exception as e:
#                     print(f"Error sending photo: {e}")
#             else:
#                 bot.send_message(message.chat.id, f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}")
#     else:
#         bot.send_message(message.chat.id, "No books found matching your query.")
#
# # Start the bot
# bot.polling()

# import telebot
# from telebot import types
#
# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot("7031144721:AAEUW58qenrejdeEfxiHLnFYSHhZ1aPehaU")
#
# # Introduction message
# intro_message = """
# Hello! Welcome to the Book Search Bot. You can use this bot to search for books by title, author, or ISBN.
# To get started, simply click one of the buttons below to choose how you want to search for books:
# """
#
# # Function to send the introduction message
# @bot.message_handler(commands=['start', 'help'])
# def send_intro_message(message):
#     bot.send_message(message.chat.id, intro_message)
#     start_menu(message.chat.id)
#
# # Function to display the start menu
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     search_title_btn = types.KeyboardButton('/search_title')
#     search_isbn_btn = types.KeyboardButton('/search_isbn')
#     search_author_btn = types.KeyboardButton('/search_author')
#     keyboard.add(search_title_btn, search_isbn_btn, search_author_btn)
#     bot.send_message(chat_id, "Choose an option to search:", reply_markup=keyboard)
#
# # Start the bot
# bot.polling()


# import telebot
# from telebot import types
# import json
#
# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot('7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s')
#
# # Flag to ensure only one instance of the bot is running
# running = True
# states = {}
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
#     keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
#     bot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     channel_link = "https://t.me/MillatUmidi_library"
#     join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
#                    f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
#                    f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
#     bot.send_message(message.chat.id, join_message)
#     start_menu(message.chat.id)
#
# @bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
# def mu_library_message(message):
#     with open("photo_2024-05-13_20-24-25.jpg", "rb") as image_file:
#         bot.send_photo(message.chat.id, image_file.read())
#     mu_library_options(message)
#
# def mu_library_options(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     register_button = types.KeyboardButton("✅ REGISTER 📝")
#     books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
#     books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
#     back_button = types.KeyboardButton("Back ↩️")
#     keyboard.add(register_button, books_mu_library, books_mu_faculty, back_button)
#     bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University", reply_markup=keyboard)
#
# # Load book data from JSON
# def load_books_data():
#     with open('books.json', 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#     return data['books']
#
# # Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
# @bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
# def books_in_mu_library(message):
#     keyboard = types.InlineKeyboardMarkup()
#     search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
#     search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
#     search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
#     keyboard.add(search_title, search_author, search_isbn)
#     bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)
#
# # Callback query handler for initiating book search
# @bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
# def search_by(call):
#     states[call.message.chat.id] = "searching"
#     field = call.data.split('_')[-1]
#     if field == 'title':
#         bot.send_message(call.message.chat.id, "Please enter the title of the book:")
#     elif field == 'author':
#         bot.send_message(call.message.chat.id, "Please enter the author of the book:")
#     elif field == 'isbn':
#         bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")
#
# def search_book(message):
#     user_input = message.text.lower()
#     results = load_books_data()
#     if results:
#         for book in results:
#             if book["title"].lower() == user_input or book['isbn'] == user_input or book["author"].lower() == user_input:
#                 book_info = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 if 'image' in book:
#                     try:
#                         with open(book['image'], 'rb') as image_file:
#                             bot.send_photo(message.chat.id, image_file, caption=book_info)
#                     except Exception as e:
#                         print(f"Error sending photo: {e}")
#                 else:
#                     bot.send_message(message.chat.id, book_info)
#                 return
#     bot.reply_to(message.chat.id, "No books found matching your query.")
#
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if states.get(message.chat.id) == "searching":
#         search_book(message)
#         states[message.chat.id] = None
#     else:
#         bot.send_message(message.chat.id, "Please choose option first.")


# def search_book(message):
#     user_input = message.lower()
#     results = load_books_data()
#     if results:
#         found_books = False
#         for book in results:
#             if book["title"].lower() == user_input or book['isbn'] == user_input or book["author"].lower() == user_input:
#                 book_info = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 return book_info
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if states.get(message.chat.id) == "searching":
#         book_info = search_book(message.text)
#         if book_info:
#             bot.send_message(message.chat.id, book_info)
#         else:
#             bot.reply_to(message.chat.id, "No books found matching your query.")
#         states[message.chat.id] = None
#     else:
#         bot.send_message(message.chat.id, "Please choose option first.")

# bot.polling()


import telebot
from telebot import types
import json

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7083059842:AAGnA5bCEy8kew8jUCOI71V-uY3VK6TpV1s')

# Flag to ensure only one instance of the bot is running
running = True
states = {}


def start_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
    world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
    amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
    channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
    keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
    bot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start_message(message):
    channel_link = "https://t.me/MillatUmidi_library"
    join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
                   f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
                   f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
    bot.send_message(message.chat.id, join_message)
    start_menu(message.chat.id)


@bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
def mu_library_message(message):
    with open("photo_2024-05-13_20-24-25.jpg", "rb") as image_file:
        bot.send_photo(message.chat.id, image_file.read())
    mu_library_options(message)


def mu_library_options(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    register_button = types.KeyboardButton("✅ REGISTER 📝")
    books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
    books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
    back_button = types.KeyboardButton("Back ↩️")
    keyboard.add(register_button, books_mu_library, books_mu_faculty, back_button)
    bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University",
                     reply_markup=keyboard)


# Load book data from JSON
def load_books_data():
    with open('books.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data['books']


# Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
@bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
def books_in_mu_library(message):
    keyboard = types.InlineKeyboardMarkup()
    search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
    search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
    search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
    keyboard.add(search_title, search_author, search_isbn)
    bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)


# Callback query handler for initiating book search
@bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
def search_by(call):
    states[call.message.chat.id] = "searching"
    field = call.data.split('_')[-1]
    if field == 'title':
        bot.send_message(call.message.chat.id, "Please enter the title of the book:")
    elif field == 'author':
        bot.send_message(call.message.chat.id, "Please enter the author of the book:")
    elif field == 'isbn':
        bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")


def search_book(message):
    user_input = message.text.lower()
    results = load_books_data()
    if results:
        for book in results:
            if book["title"].lower() == user_input or book['isbn'] == user_input or book["author"].lower() == user_input:
                book_info = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
                if 'image' in book:
                    try:
                        with open(book['image'], 'rb') as image_file:
                            bot.send_photo(message.chat.id, image_file.read(), caption=book_info)
                    except Exception as e:
                        print(f"Error sending photo: {e}")
                else:
                    bot.send_message(message.chat.id, book_info)
                return
    bot.reply_to(message.chat.id, "No books found matching your query.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if states.get(message.chat.id) == "searching":
        search_book(message)
        states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, "Please choose option first.")


bot.polling()




# import telebot
# from telebot import types
# import json
#
# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot('7031144721:AAEUW58qenrejdeEfxiHLnFYSHhZ1aPehaU')
#
# # Flag to ensure only one instance of the bot is running
# running = True
# states = {}
#
#
# def start_menu(chat_id):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     mu_library_button = types.KeyboardButton('MU_LIBRARY 🏢')
#     world_book_button = types.KeyboardButton('WORLD_BOOKS 🌍')
#     amazon_books_button = types.KeyboardButton('AMAZON_BOOKS 📚')
#     channel_books_button = types.KeyboardButton('BOOK CHANNELS 📲')
#     keyboard.add(mu_library_button, world_book_button, amazon_books_button, channel_books_button)
#     bot.send_message(chat_id, "Choose one of the options below:", reply_markup=keyboard)
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     channel_link = "https://t.me/MillatUmidi_library"
#     join_message = f"ASSALOMU ALAYKUM\n\nWELCOME TO OUR BOT👋,\n\n✅ THIS BOT HELPS YOU SEARCHING  BOOKS YOU WANT 📚\n" \
#                    f"\n✅ YOU CAN SEARCH BOOKS FOR BOOKS OF MILLAT UMIDI UNIVERSITY 🏢 \nAND ALL THE BOOKS IN THE WORLD 🌍 !" \
#                    f"\n\nOUR CHANEL LINK 👇, PLEASE JOIN❗️\n{channel_link}\n"
#     bot.send_message(message.chat.id, join_message)
#     start_menu(message.chat.id)
#
#
# @bot.message_handler(func=lambda message: message.text == "MU_LIBRARY 🏢")
# def mu_library_message(message):
#     with open("photo_2024-05-13_20-24-25.jpg", "rb") as image_file:
#         bot.send_photo(message.chat.id, image_file.read())
#     mu_library_options(message)
#
#
# def mu_library_options(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     register_button = types.KeyboardButton("✅ REGISTER 📝")
#     books_mu_library = types.KeyboardButton("✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
#     books_mu_faculty = types.KeyboardButton("✅ BOOKS FOR MU FACULTIES 🗂")
#     back_button = types.KeyboardButton("Back ↩️")
#     keyboard.add(register_button, books_mu_library, books_mu_faculty, back_button)
#     bot.send_message(message.chat.id, "Hello, We are happy🥰 with your choice,\n 🤗Welcome to MILLAT UMIDI University",
#                      reply_markup=keyboard)
#
#
# # Load book data from JSON
# def load_books_data():
#     with open('books.json', 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#     return data['books']
#
#
# # Function to handle the "✅ AVAILABLE BOOKS IN MU LIBRARY 📚" button
# @bot.message_handler(func=lambda message: message.text == "✅ AVAILABLE BOOKS IN MU LIBRARY 📚")
# def books_in_mu_library(message):
#     keyboard = types.InlineKeyboardMarkup()
#     search_title = types.InlineKeyboardButton('📙 TITLE', callback_data='search_by_title')
#     search_author = types.InlineKeyboardButton('📝👤 AUTHOR', callback_data='search_by_author')
#     search_isbn = types.InlineKeyboardButton(' 🔢 ISBN', callback_data='search_by_isbn')
#     keyboard.add(search_title, search_author, search_isbn)
#     bot.send_message(message.chat.id, "Choose how you want to search for books:", reply_markup=keyboard)
#
#
# # Callback query handler for initiating book search
# @bot.callback_query_handler(func=lambda call: call.data.startswith('search_by_'))
# def search_by(call):
#     states[call.message.chat.id] = "searching"
#     field = call.data.split('_')[-1]
#     if field == 'title':
#         bot.send_message(call.message.chat.id, "Please enter the title of the book:")
#     elif field == 'author':
#         bot.send_message(call.message.chat.id, "Please enter the author of the book:")
#     elif field == 'isbn':
#         bot.send_message(call.message.chat.id, "Please enter the ISBN of the book:")
#
#
# def search_book(message):
#     user_input = message.text.lower()
#     results = load_books_data()
#     if results:
#         for book in results:
#             if book["title"].lower() == user_input or book['isbn'] == user_input or book["author"].lower() == user_input:
#                 book_info = f"Title: {book['title']}\nISBN: {book['isbn']}\nAuthor: {book['author']}\nPages: {book['pages']}\nColumn: {book['column']}\nShelf: {book['shelf']}"
#                 if 'image' in book:
#                     try:
#                         with open(book['image'], 'rb') as image_file:
#                             bot.send_photo(message.chat.id, image_file, caption=book_info)
#                     except Exception as e:
#                         print(f"Error sending photo: {e}")
#                 else:
#                     bot.send_message(message.chat.id, book_info)
#                 return
#     bot.reply_to(message.chat.id, "No books found matching your query.")
#
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if states.get(message.chat.id) == "searching":
#         search_book(message)
#         states[message.chat.id] = None
#     else:
#         bot.send_message(message.chat.id, "Please choose option first.")
#
#
# bot.polling()

