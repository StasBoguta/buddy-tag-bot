"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import re
import json
import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from taro import TARO_SET
import time

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5588729871:AAE_3Y1i4w321rWaLj9f_83myMlFhbV9wHQ'
# API_TOKEN = '1698570040:AAGvmUeVtpTKw18dn-VlTUAXDT04vWp-uhI'
# CHATS_SET = [-1001785608646]

f = open('tags.json', encoding="utf8")
TAG_SET = json.load(f)
f.close()

NUDES_TIMES = {}
NUDES_DUPLICATE = {}
BEER_TIMES = {}
BEER_DUPLICATE = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

regex = r"[\s]*@[^\s]+[\s]*"


async def get_all_tag():
    tag_arr = []
    for speciality in TAG_SET.values():
        for people in speciality.values():
            tag_arr = tag_arr + people
    return tag_arr


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
@картадня - карта дня
@піво - піво
@нюдси - тегає одного Бадді, який повиннен тобі кинути нюдси\n
@all - задудосити всіх бадді\n
ФІ
@фі - фішники
@кн @іпз @пм @кб - по спеціальностях\n
ФЕН
@фен - весь ФЕН
@фінанси @маркетинг @менеджмент @економіка - по спеціальностях\n
ФПвН
@фпвн - весь ФПвН
@право  - по спеціальностях\n
ФСНСТ
@фснст - весь ФСНСТ
@психологія @соціологія @соцроб @міжнар @піар @політологія - по спеціальностях\n
ФПрН
@фпрн - весь ФПрН
@хімія @фізика @екологія @біологія - по спеціальностях\n
ФГН
@фгн - фесь ФГН
@германська @українська @філософія @культурологія @історія - по спеціальностях
    """
    await bot.send_message(message.chat.id, text, parse_mode='Markdown')

# VOTE_SET = {}
# keyboard = InlineKeyboardMarkup()
# keyboard.add(InlineKeyboardButton(text="👉👌", callback_data="fuck_user"),
#              InlineKeyboardButton(text="👰‍♀️👰‍♂️", callback_data="merry_user"),
#              InlineKeyboardButton(text="💀", callback_data="kill_user"))
# keyboard.add(InlineKeyboardButton(text="Закінчити голосування", callback_data="vote_end"))

# @dp.message_handler(regexp='@голосування')
# async def nudes(message: types.Message):
#     # if message.chat.id not in CHATS_SET:
#     #     return
#     matches = re.finditer(regex, message.text, re.MULTILINE)
#     tags = []
#     for match in matches:
#         tag = match.group().strip()
#         if tag != "@голосування":
#             tags.append(match.group().strip())
#     if len(tags) != 0:
#         msg = await message.answer(f"Шо ти хочеш зробити з {tags[0]}", reply_markup=keyboard)
#         VOTE_SET[msg["message_id"]] = {"tag": tags[0]}


# @dp.callback_query_handler()
# async def process_callback(callback_query: types.CallbackQuery):
#     data = callback_query.data
#     chat_id = callback_query["message"]["chat"]["id"]
#     message_id = callback_query["message"]["message_id"]
#     user_id = callback_query["from"]["id"]
#     try:
#         if data == "fuck_user":
#             VOTE_SET[message_id][user_id] = "fuck"
#             await bot.answer_callback_query(callback_query.id, text='Ось і нема трусів', show_alert=True)
#             await bot.edit_message_text(
#                 f"Шо ти хочеш зробити з {VOTE_SET[message_id]['tag']}.\nПроголосувало {len(VOTE_SET[message_id])-1}",
#                 chat_id=chat_id,
#                 message_id=message_id, reply_markup=keyboard)
#         elif data == "merry_user":
#             VOTE_SET[message_id][user_id] = "merry"
#             await bot.answer_callback_query(callback_query.id, text='Маєш файний смак', show_alert=True)
#             await bot.edit_message_text(
#                 f"Шо ти хочеш зробити з {VOTE_SET[message_id]['tag']}.\nПроголосувало {len(VOTE_SET[message_id])-1}",
#                 chat_id=chat_id,
#                 message_id=message_id, reply_markup=keyboard)
#         elif data == "kill_user":
#             VOTE_SET[message_id][user_id] = "kill"
#             await bot.answer_callback_query(callback_query.id, text='Якшо шо я тобі допоможу труп закопать', show_alert=True)
#             await bot.edit_message_text(
#                 f"Шо ти хочеш зробити з {VOTE_SET[message_id]['tag']}.\nПроголосувало {len(VOTE_SET[message_id])-1}", chat_id=chat_id,
#                 message_id=message_id, reply_markup=keyboard)
#         else:
#             fuck_counter = 0
#             merry_counter = 0
#             kill_counter = 0
#             for value in VOTE_SET[message_id].values():
#                 if value == "fuck":
#                     fuck_counter = fuck_counter + 1
#                 elif value == "merry":
#                     merry_counter = merry_counter + 1
#                 elif value == "kill":
#                     kill_counter = kill_counter + 1
#             await bot.edit_message_text(f"{VOTE_SET[message_id]['tag']} ось результати:\nВбивають тебе - {kill_counter} людей\nОдружуються на тобі - {merry_counter} людей\nЇбуть тебе - {fuck_counter} людей", chat_id, message_id)
#             VOTE_SET.pop(message_id)
#     except:
#         pass

@dp.message_handler(regexp='@піво')
async def nudes(message: types.Message):
    # if message.chat.id not in CHATS_SET:
    #     return
    check = await check_id(message, BEER_TIMES, BEER_DUPLICATE)
    if not check:
        if not BEER_DUPLICATE[message.from_id]:
            await message.reply("Іди трезвій! Потім повернешся за пивом!")
        BEER_DUPLICATE[message.from_id] = True
    else:
        tag_arr = await get_all_tag()
        men = random.choice(tag_arr)
        action = random.uniform(0, 1)
        if action <= 0.1:
            await message.reply(f"Ти торчиш бочку горючого напою для {men}")
        elif action <= 0.5:
            await message.reply(f"Тобі {men} торчить літру алкоголю")
        else:
            await message.reply(f"Ви з {men} повинні сходити на піво")


# @dp.message_handler(regexp='@картадня')
# async def taro(message: types.Message):
#     taro_id = random.choice(TARO_SET)
#     await message.reply_sticker(taro_id)


async def check_id(message: types.Message, array, checker):
    if message.from_id not in array.keys():
        checker[message.from_id] = False
        array[message.from_id] = time.time()
        return True
    delta = time.time() - array[message.from_id]
    if delta > 21600:
        checker[message.from_id] = False
        return True
    return False


@dp.message_handler(regexp='@нюдси')
async def nudes(message: types.Message):
    check = await check_id(message, NUDES_TIMES, NUDES_DUPLICATE)
    if not check:
        if not NUDES_DUPLICATE[message.from_id]:
            await message.reply("Багато нюдсів просити погано! Май совість! Попроси пізніше")
        NUDES_DUPLICATE[message.from_id] = True
    else:
        tag_arr = await get_all_tag()
        men = random.choice(tag_arr)
        action = random.uniform(0, 1)
        if action <= 0.05:
            await message.reply("Шось ти дуже хорні. Піди понизь хорніградус")
        elif action <= 0.2:
            await message.reply("А всьо, а тепер ти винен нюдси. Кидай свої!!!")
        else:
            await message.reply(f'Тобі повинен кинути нюдси {men}')


@dp.message_handler(regexp='@')
async def tag_users(message: types.Message):
    txt = message.text
    matches = re.finditer(regex, txt, re.MULTILINE)
    tags = set()
    for match in matches:
        tags.add(match.group().strip())
    for tag in tags:
        tags_arr = []
        if tag != "@all":
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
            tags_arr = await get_all_tag()

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

# @dp.message_handler(regexp='(С|с)екс')
# async def all_message(message: types.Message):
#     await message.reply('Якщо секс, то краще жосткій')
#     await message.reply_sticker('CAACAgIAAxkBAAEFT-Vi1m6y9EU-pfcgaVLYfR5e2Da21gAClQ8AAvhcsEiIoYxQTB4dgykE')
#


@dp.message_handler(regexp='цьом')
async def all_message(message: types.Message):
    await message.reply('Цьом!')


# @dp.message_handler(regexp='(М|м)а(ма|тір|ть|мчик|зер)')
# async def all_message(message: types.Message):
#     messages = [
#         'Я дуже люблю твою маму','Мать то хорошо, особливо твоя','Ну не мамкай',
#         'А ти знаєш де я сьогодні був?'
#     ]
#     await message.reply(random.choice(messages))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
