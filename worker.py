from telethon import TelegramClient, sync, tl
import time
import random

api_id = 2646470
api_hash = '764c4e3babfd216ec38f564b542f2e0a'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

while True:
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        a1 = 'просмотры' in dialog.title.lower()
        a2 = 'views' in dialog.title.lower()
        a3 = 'posts' in dialog.title.lower()
        a4 = 'tgfast 🚀|work' in dialog.title.lower()
        a5 = 'реклама pr teleg bot' in dialog.title.lower()
        a6 = 'pixibot работа' in dialog.title.lower()
        if a1 or a2 or a3 or a4 or a5 or a6:
            print(dialog.title)
            target = dialog
            messages = client.get_messages(target, limit=30)
            for message in messages:
                if message.reply_markup is not None:
                    button = message.reply_markup.rows[0].buttons[0]
                    if type(button) == tl.types.KeyboardButtonCallback:
                        resp = client(tl.functions.messages.GetBotCallbackAnswerRequest(
                            target,
                            message.id,
                            data=button.data
                        ))
                        time.sleep(3)
    time.sleep(random.randint(350, 500))
