#киборд перенесен под сообщение
#добавлен стандартный ответ на сообщение
#добавлены гиперссылки
#эдит/удаление каждого предыдущего сообщения
#

'''
Добавить:
- ограничение в 20 сообщений в минуту
'''
import telebot
from telebot import types
import config
import requests
import aiogram
import sqlite3
import time

print('in progress...')
token = '6270601894:AAGlQdXXw6m_zZp_63hCys2MnZpFiY8JgAg'
bot = telebot.TeleBot(token)

run = False

news = """У нас есть сенсационная новость, вскоре состоится несравненная тусовка. 
Не требует лишних слов, дата уже определена - 6 мая в 17.00 начало, так что не теряй время и закажи билеты по самым доступным ценам уже сегодня. 
Твоя уникальная возможность круто провести время ждет тебя! 👇🏽
"""        

tusovka = """Мы нескромно говорим о себе как о небольшой, однако, умелой команде, готовой совершать творческие подвиги и преодолевать любые препятствия на пути к успеху. SD CLUB является новичком на тусовочной сцене, однако наша целеустремленность и профессионализм дают нам уверенность в нашем бескомпромиссном качестве. Нашего клуба нет равных, потому что мы продвигаемся по новому формату, который не имеет границ и готов предоставить нашим клиентам качество и отзывчивость всех наших работников без исключения!"""

free1 = """Хочешь попасть в списки FREE и получить уникальный шанс на три VIP проходки? Тогда внимательно читай условия! 
- Необходимо быть ПОДПИСАНЫМ на """ 
free2 = """ и сделать репост поста о ближайшей тусовке в свои сторис, поставив отметку нас! 
- Также не забудь сделать репост записи на свою стену и поставить лайк на пост ближайшего EVENT в ВК. 
- 💥 - Среди выполнивших условия мы разыграем три VIP проходки, так что не упусти свой шанс. Выполни условия - и ты уже участвуешь! 
Приходи на тусовку 6 мая и получай FREE вход до 18.00! После 18.00 вход будет стоить всего от 200 рублей. Готов к незабываемому вечеру? Тогда присоединяйся к нам уже сегодня! 💥❤️"""

scene = """Откройте для себя настоящее зрелище с доступом на сцену! С билетом "SD GRIM" вы получаете ключи от гримёрки и сцены. А теперь самое главное - вы получаете вездеход на вечеринке! Ощутите себя знаменитостью и пройдите сквозь толпу с уверенностью и стилем. Сделайте свой визит на вечеринку незабываемым с доступом на сцену. Для того чтобы его получить, напиши в поддержку в разделе «Помощь», мы обязательно ответим тебе!"""

ticks1 = "Получи промокод на скидку!\t" 
ticks2 = "\tи напиши «ХОЧУ ПРОМОКОД». Мы обязательно ответим и вышлем тебе код. Обрати внимание, что скидки действуют не на каждый "

metgret = """Билет Meet Great - это личная встреча с артистом. Купить его можно связавшись с нами в разделе "помощь". Узнать подробнее про этот билет можно там же"""

helpa = """Для связи с организаторами👇🏽
1. https://vk.com/smbat_777
2. https://vk.com/dimapetruska"""

@bot.message_handler(commands=['start'])
def start_message(message):

    # keybord
    markup = types.InlineKeyboardMarkup(row_width = 2)
    
    item1 = types.InlineKeyboardButton("Ближайшие events", callback_data = '1')
    item2 = types.InlineKeyboardButton("Узнать о тусовке", callback_data = '2')
    item3 = types.InlineKeyboardButton("Хочу бесплатную проходку", callback_data = '3')
    item4 = types.InlineKeyboardButton("Хочу выйти на сцену(в гримерку)", callback_data = '4')
    item5 = types.InlineKeyboardButton("Ссылка на покупку билетов", callback_data = '5')
    item6 = types.InlineKeyboardButton("Meet Great (личная встреча с артистом)", callback_data = '6')
    item7 = types.InlineKeyboardButton("Помощь", callback_data = '7')
    
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, text = news + "<a href='https://moscow.qtickets.events/68360-spacex-x-sd-clubshow-blockkid-secret-guests-6-maya-14'>🎫 Купить билет</a>".format(message.from_user, bot.get_me()),parse_mode='html')
    
    msg_st = bot.send_message(message.chat.id, text = "{0.first_name}, тебя приветствует организация SD, мы проводим лучшие EVENTS для тебя!\nВыбирай, что хотел 😃 / 👇🏽".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    
@bot.message_handler(content_types=['text'])
def answer(message):
    if True:
        msg_ans = bot.send_message(message.chat.id, 'Пока что я не умею отвечать на сообщения. Если у Вас есть вопрос, пожалуйста, перейдите в раздел "Помощь"')
        time.sleep(5)
        bot.delete_message(msg_ans.chat.id, msg_ans.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width = 2)
            
            item1 = types.InlineKeyboardButton("Ближайшие events", callback_data = '1')
            item2 = types.InlineKeyboardButton("Узнать о тусовке", callback_data = '2')
            item3 = types.InlineKeyboardButton("Хочу бесплатную проходку", callback_data = '3')
            item4 = types.InlineKeyboardButton("Хочу выйти на сцену(в гримерку)", callback_data = '4')
            item5 = types.InlineKeyboardButton("Ссылка на покупку билетов", callback_data = '5')
            item6 = types.InlineKeyboardButton("Meet Great (личная встреча с артистом)", callback_data = '6')
            item7 = types.InlineKeyboardButton("Помощь", callback_data = '7')
        
            markup.add(item1, item2, item3, item4, item5, item6, item7)
            if call.data == '1':
            
                msg = "Ближайшие\t" + "<b>EVENTS</b>" + "\tможешь посмотреть в наших социальных сетях 👇🏽\n" + "<a href='https://instagram.com/sd.moscow?igshid=YmMyMTA2M2Y='>Instagram</a>" + '\n' + "<a href='https://t.me/SamDaimond'>Telegram</a>" + '\n' + "<a href='https://vk.com/samdiamond_sdclub'>VK</a>".format(call.message.from_user, bot.get_me())

            elif call.data == '2':
            
                msg = tusovka

            elif call.data == '3':
            
                msg = free1 + "<a href='https://vk.com/samdiamond_sdclub'>наше сообщество в VK</a>" + free2.format(call.message.from_user, bot.get_me())

            elif call.data == '4':
            
                msg = scene                 
                
            elif call.data == '5':
            
                msg = ticks1 + "<a href='https://vk.com/samdiamond_sdclub'>Подпишись на наше сообщество в VK</a>" + ticks2 + "<b>EVENT</b>" + "!".format(call.message.from_user, bot.get_me())
                
            elif call.data == '6':
            
                msg = metgret
                
            elif call.data == '7':
            
                msg = helpa
            
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = msg, parse_mode='html', reply_markup = markup)
            
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
