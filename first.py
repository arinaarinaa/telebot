import telebot 
from telebot import types
token = '5807759820:AAFkAWVAg8C-Nyss_rlyykHgD9B5A0KdFQ8'


bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start']) #декаратор - любая команда
#бота так создается. После этого нужна функция 
def start_message(message):
    bot.send_message(message.chat.id, 'Начинаем план <b>скам</b>', parse_mode='HTML') #чат айди - айди чата
    #Если вывести туда цифры, то приходить сообщение будет только одному чату этому
    bot.send_message(message.chat.id, 'Нажми на /button, если хочешь увидеть весь функционал')
    
    user_first_name = str(message.chat.first_name)
    bot.send_message(message.chat.id, f'Оп, оп, {user_first_name} здесь')



@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #markup - клавиатура, ресайз - размер кнопки 
    item1 = types.KeyboardButton('Кнопулька')# вот это сама кнопка, здесь их
    #может быть много(названия пропиши также)
    item2 = types.KeyboardButton('Конец')
    item3 = types.KeyboardButton('Депрессивные мемы')
    item4 = types.KeyboardButton('Контент')
    markup.add(item1, item2, item3, item4) #Добавляем к клаве 
    bot.send_message(message.chat.id, 'Выберите, что нужно', reply_markup=markup)

    

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Кнопулька':
        bot.send_message(message.chat.id, 'Ну вот ты и нажал на кнопульку, молодец')
        bot.send_message(message.chat.id, 'Займи себя чем-нибудь..')
    if message.text == 'Конец':
        bot.send_message(message.chat.id, 'Заскамили мамонта')
        bot.send_photo(message.chat.id, 'https://sun9-north.userapi.com/sun9-79/s/v1/ig2/WerYF-wsF9cRJK3vrr3Fn-dRiOB4ral1ydsTNIMB2Wm8sbY35OtNOmTr7ocIAFugyEvcExTfkx6ouYtOVqblhsVx.jpg?size=1280x972&quality=95&type=album')

    if message.text == 'Депрессивные мемы':
        audio = open(r'C:/Users/днс/OneDrive/Рабочий стол/jj/Голос 001_sd.m4a', 'rb')
        bot.send_audio(message.chat.id, audio)
        bot.send_message(message.chat.id,'<a href="https://www.youtube.com/watch?v=aKOwUMHncZs&t=250s">Стендап Саши Малого</a>',parse_mode="HTML")
    
    if message.text == 'Контент':
        inner_knopki = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text = 'Есть вечный мульт',url = 'https://www.youtube.com/watch?v=x0guCN44rhs&t=22s')
        but2 = types.InlineKeyboardButton(text = 'просто неплохой клип',url = 'https://www.youtube.com/watch?v=0HDdjwpPM3Y&list=RD0HDdjwpPM3Y&start_radio=1')
        inner_knopki.add(but1, but2)
        bot.send_message(message.chat.id, 'Контент', reply_markup=inner_knopki)
        bot.send_message(message.chat.id, 'Что-то еще может быть?')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Ты что-то хотел?")
 
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Привет")
 
# @bot.message_handler(commands=['videos'])
# def search_videos(message):
#     msg = bot.send_message(message.chat.id, "Введите текст, который вы хотите найти в YouTube")
#     bot.register_next_step_handler(msg, search)
 
# @bot.message_handler(commands=['channel'])
# def search_channel(message):
#     msg = bot.send_message(message.chat.id, "Введите YouTube канал")
#     bot.register_next_step_handler(msg, search_from_channel)
 
 
 
# @bot.message_handler(content_types=['text'])
# def text(message):
#     bot.send_message(message.chat.id, "Ты что-то хотел?")
 
# def search_from_channel(message):
#     bot.send_message(message.chat.id, "Начинаю поиск")
#     driver.get(message.text + "/videos")
#     videos = driver.find_elements_by_id("video-title")
#     for i in range(len(videos)):
#         bot.send_message(message.chat.id, videos[i].get_attribute('href'))
#         if i == 10:
#             break
 
# def search(message):
#     bot.send_message(message.chat.id, "Начинаю поиск")
#     video_href = "https://www.youtube.com/results?search_query=" + message.text
#     driver.get(video_href)
#     sleep(2)
#     videos = driver.find_element_by_id("video-title")
#     for i in range(len(videos)):
#         bot.send_message(message.chat.id, videos[i].get_attribute('href'))
#         if i == 10:
#             break
 
bot.infinity_polling()