"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import re
import json
import random


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5588729871:AAE_3Y1i4w321rWaLj9f_83myMlFhbV9wHQ'
# API_TOKEN = '1698570040:AAGvmUeVtpTKw18dn-VlTUAXDT04vWp-uhI'
CHATS_SET = [-1001785608646]

f = open('tags.json', encoding="utf8")
TAG_SET = json.load(f)
f.close()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

regex = r"[\s]*@[^\s]+[\s]*"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await bot.send_message(message.chat.id, "Add me to the Buddy group!!\nThat's all that I want!")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    text = """Вечір в хату!\nЯкщо хочеш задовбати бадді теганієм, то я тобі допоможу!\n
Шо дєлать:\n1. В мене є набір тегів, які ти можеш написати в чат. Щоб перевірити доступні теги напиши /helpm\n
2. Пишеш в чат, наприклад @fi і тобі тегне всіх фішників. Також є теги окремо по спеціальності.\n\nХутчіш затегівай людей! Цьом!
    """
    await bot.send_message(message.chat.id, text, parse_mode='Markdown')


@dp.message_handler(commands=['helpm'])
async def send_more_help(message: types.Message):
    text = """
*Доступні команди для дудоса Бадді 2022*\n
@нюдси - тегає одного Бадді, який повиннен тобі кинути нюдси\n
@all - задудосити всіх бадді\n
ФІ
@фі - фішники
@кн @іпз @пм - по спеціальностях\n
ФЕН
@фен - весь ФЕН
@фінанси @маркетинг @менеджмент @економіка - по спеціальностях\n
ФПвН
@фпвн - весь ФПвН
@право @публічне  - по спеціальностях\n
ФСНСТ
@фснст - весь ФСНСТ
@психологія @соціологія @соцроб @міжнар @громадське @політологія - по спеціальностях\n
ФПрН
@фпрн - весь ФПрН
@хімія @фізика @екологія @біологія - по спеціальностях\n
ФГН
@фгн - фесь ФГН
@германська @українська @філософія @культурологія @історія - по спеціальностях
    """
    await bot.send_message(message.chat.id, text, parse_mode='Markdown')


@dp.message_handler(regexp='@')
async def tag_users(message: types.Message):
    if message.chat.id not in CHATS_SET:
        return
    txt = message.text
    matches = re.finditer(regex, txt, re.MULTILINE)
    tags = set()
    for match in matches:
        tags.add(match.group().strip())
    for tag in tags:
        tags_arr = []
        if tag == "@нюдси":
            tag_arr = []
            for speciality in TAG_SET.values():
                for people in speciality.values():
                    tag_arr = tag_arr + people
            index = random.randint(0, len(tag_arr))
            men = tag_arr[index]
            await message.reply(f'Тобі повинен кинути нюдси {men}')
        elif tag != "@all":
            if tag in list(TAG_SET.keys()):
                for tag_set in TAG_SET[tag].values():
                    tags_arr = tags_arr + tag_set
            else:
                speciality_all = {}
                for speciality in TAG_SET.values():
                    speciality_all.update(speciality)
                if tag in speciality_all.keys():
                    tags_arr = tags_arr + speciality_all[tag]
        else:
            for speciality in TAG_SET.values():
                for people in speciality.values():
                    tags_arr = tags_arr + people

        if len(tags_arr) != 0:
            if len(tags_arr) > 5:
                tags_len = len(tags_arr)
                iteration = 0
                while iteration < tags_len:
                    left = iteration
                    right = tags_len + 1 if left + 5 > tags_len + 1 else left + 5
                    iteration = iteration + 5
                    tags_slice = tags_arr[left:right]
                    reply_text = "\n".join(tags_slice)
                    await message.reply(f'Люди за тегом {tag}:\n{reply_text}')
            else:
                reply_text = "\n".join(tags_arr)
                await message.reply(f'Люди за тегом {tag}:\n{reply_text}')


@dp.message_handler(regexp='^Стас Богута')
async def creator_reply(message: types.Message):
    await message.reply(f'Абонен не може прийняти ваш виклик, або знаходиться поза мережею. Виклик абонента @stasboguta')


@dp.message_handler(regexp='(П|п)іздєц|єбанутся')
async def pizdec_reply(message: types.Message):
    await message.reply_sticker('CAACAgIAAxkBAAEFT8Zi1llLBedXn3TXXMDebZQeIMEyMQACXBIAAiRhqUtZjwhZKLtMhCkE')


@dp.message_handler(regexp='(К|к)апібалицький|(Б|б)алицький|(К|к)оординатор (Б|б)адді')
async def pizdec_reply(message: types.Message):
    await message.reply_sticker('CAACAgIAAxkBAAEFT8pi1lqDBJ2zWAYqU6KjtWm1wnKNvQACRxIAApn9uEhCchH2JItcEikE')


@dp.message_handler(regexp='(Т|т)ернопіль')
async def pizdec_reply(message: types.Message):
    await message.reply_sticker('CAACAgQAAxkBAAEFT8hi1lpj3UTgMOhL8cECZY-AYc66_AACewADzMbLEbHdXkGD-IiFKQQ')


@dp.message_handler(regexp="(А|а)ліна (К|к)руп('|`|')яник|(С|с)аша (Т|т)емч|(Т|т)емч")
async def pizdec_reply(message: types.Message):
    await message.reply('🔪🔪🔪🔪🔪')


@dp.message_handler(regexp='ніхуя собі')
async def all_message(message: types.Message):
    await message.reply_sticker('CAACAgIAAxkBAAEFT8xi1lucgRpIW2DF0uvltzzrOIzGkAACJBIAAnHAqUs-5_J9etWXeCkE')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
