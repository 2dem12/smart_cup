# нужные библиотеки:
# pip install pyTelegramBotAPI
# pip install googletrans==4.0.0rc1
#
# ссылка на телеграмм бота:
# https://t.me/smart_cup_bot


import telebot
from googletrans import Translator
from telebot import types

que_t1 = ['Enter weapons.', "Who do you dislike the most", "What is your boy friend name???", 'The most cozy place.',
          'How old are you??', 'What kind of gift do you want for the new year???',
          'Write something to get your story.']
que_t2 = ['The coolest feature/technology.', "The best person.", 'What are you most afraid of???',
          'Write something to get your story.']
status = 0
ans_t1 = []
ans_t2 = []
textr = ''
i = 0
translator = Translator()
bot = telebot.TeleBot('6136107778:AAFGCd8fnSaz_LfklhiKuIjbh1JM27dpThs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    hero = types.KeyboardButton('Hero of the tribe')
    car = types.KeyboardButton('Programmer in a sports car')
    markup.add(hero, car)
    bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.first_name} \nЯ бот, который напишет вам вашу '
                                      f'новую историю.', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_user(message):
    global status, ans_t1, ans_t2, textr, i

    if message.text == 'Hero of the tribe':
        status = 1
        ans_t1 = []
        i = 0
        bot.send_message(message.chat.id, 'Enter the race')

    if message.text == 'Programmer in a sports car':
        status = -1
        ans_t1 = []
        i = 0
        bot.send_message(message.chat.id, 'If you were the owner of the company, what would it be called???')

    if len(ans_t1) == 7 and status == 1:
        textr = ''

        textr = f"""A long time ago, a great battle took place in the world where {ans_t1[0]} lived.
{ans_t1[0].capitalize()} were well armed {ans_t1[1]}. Their goal was the same -
to protect their lands and wealth from {ans_t1[2]}.

In one of the battles, {ans_t1[0]} was heavily attacked, and {ans_t1[3].title()} ended up
behind enemy lines. He was forced to hide {ans_t1[4]} where he discovered
a magical amulet that could predict the future. {ans_t1[3].title()} decided
to put on an amulet to figure out how to get him out of {ans_t1[4]}.

The amulet lit up and showed the {ans_t1[5]} paths. {ans_t1[3].title()} chose the most
difficult path that led him to the leader of the enemies. With the help
his {ans_t1[1]}, {ans_t1[3].title()} defeated {ans_t1[2]} and saved his comrades.

After the war, {ans_t1[3].title()} returned to his homeland and was rewarded
{ans_t1[6]}. Later, {ans_t1[3].title()} became a great leader of his
country and helped everyone who needed his help."""

        bot.send_message(message.chat.id, textr)
        status = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tr = types.KeyboardButton('Translate this text')
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        markup.add(hero, car, tr)
        bot.send_message(message.chat.id, 'Who will your next story be about???', reply_markup=markup)

    if len(ans_t2) == 4 and status == -1:
        textr = ''

        textr = f"""There were the fastest and most luxurious cars in the world, but
only one company created the real sports cars of the future -
"{ans_t2[0]}". These beautiful machines were capable of reaching the speed
of light and had the most innovative technologies, including {ans_t2[1]}.

One day, racers who owned "{ans_t2[0]}"
of different models gathered on the track. Among them were the racer {ans_t2[2].title()}, who was
a programmer who graduated from IFTIS and tried to implement into the car
his latest development, but for some reason it didn't work out and there was an error that he couldn't figure out.

He asked many people who know English, but no one could translate the text that occurs when an error occurs. 
Before the race, he met a girl, Alina, who had excellent knowledge of foreign languages. She helped {ans_t2[2].title()} 
translate an error that no one could understand. 
Fortunately, in a few hours, the rider managed to fix an annoying mistake.

The race started and "{ans_t2[0]}" raced along the track, leaving a whirlwind behind them
of fire and smoke. The racer {ans_t2[2].title()} felt how his car reacted
to his every move. He enjoyed the speed and adrenaline
until he heard the voice of his car, which warned him about
{ans_t2[3]}.

He was forced to slow down, and at that moment another rider
rushed past him, but his "{ans_t2[0]}" began to lose speed due to
{ans_t2[3]}. The driver {ans_t2[2].title()} decided to take advantage of the situation to
finish first and win the race.

"{ans_t2[0].capitalize()}" continued to compete on the track, creating a real
the show is for all viewers, and the racer {ans_t2[2].title()} continued to improve their
cars to stay on top of the sports world."""

        bot.send_message(message.chat.id, textr)
        status = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tr = types.KeyboardButton('Translate this text')
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        markup.add(hero, car, tr)
        bot.send_message(message.chat.id, 'Who will your next story be about???', reply_markup=markup)

    if message.text is not None and status == 1 and message.text != 'Hero of the tribe' and message.text != 'Programmer in a sports car':
        ans_t1.append(message.text)
        bot.send_message(message.chat.id, que_t1[i])
        i += 1

    if message.text is not None and status == -1 and message.text != 'Programmer in a sports car' and message.text != 'Hero of the tribe':
        ans_t2.append(message.text)
        bot.send_message(message.chat.id, que_t2[i])
        i += 1

    if message.text == 'Translate this text' and status == 0 and message.text is not None:
        trans = translator.translate(textr, src='en', dest='ru')
        bot.send_message(message.chat.id, trans.text)


bot.polling(none_stop=True)
