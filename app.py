"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import re
import json


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5588729871:AAE_3Y1i4w321rWaLj9f_83myMlFhbV9wHQ'
CHATS_SET = [-1001785608646]

f = open('tags.json')
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
@all - задудосити всіх бадді\n
ФІ
@fi - фішники
@kn @ipz @pm - по спеціальностях\n
ФЕН
@fen - весь ФЕН
@finance @marketing @management @economics - по спеціальностях\n
ФПвН
@fpvn - весь ФПвН
@pravo @public  - по спеціальностях\n
ФСНСТ
@fsnst - весь ФСНСТ
@psycho @socio @socrob @miznar @gromada @polyt - по спеціальностях\n
ФПрН
@fprn - весь ФПрН
@chemist @physics @eco @bio - по спеціальностях\n
ФГН
@fgn - фесь ФГН
@german @ukr @philos @kult @history - по спеціальностях
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
