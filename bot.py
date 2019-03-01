from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename = 'bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
              update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)




def planets(bot, update):
    begin = 'Напишите название одной из этих планет: Mercury, Mars, Venus, Jupiter, Saturn, Uranus, Neptune, чтобы узнать, в каком созвездии она сегодня находится: '
    logging.info(begin)
    update.message.reply_text(begin)


date = datetime.datetime.now()

planet = {
    'Mercury': ephem.constellation(ephem.Mercury(date)),
    'Mars': ephem.constellation(ephem.Mars(date)),
    'Venus': ephem.constellation(ephem.Venus(date)),
    'Jupiter': ephem.constellation(ephem.Jupiter(date)),
    'Saturn': ephem.constellation(ephem.Saturn(date)),
    'Uranus': ephem.constellation(ephem.Uranus(date)),
    'Neptune': ephem.constellation(ephem.Neptune(date)),
}

def constellation(bot, update):

    name = update.message.text
    answer = 'Планета находится в созвездии {}'.format(planet[name])

    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
              update.message.chat.id, update.message.text)
    update.message.reply_text(answer)



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))


    dp.add_handler(MessageHandler(Filters.text, constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()
    
main()