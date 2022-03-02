from config import bot_token
import requests
from core.dbmanager import get_meaning

def run_command(text, chat_id, message_id):

    definition = get_meaning(text, '*', json_out=False)
    # out = definition.__repr__()
    text = dict2telegram(definition)
    out = text

    if len(out) == 0:
        out = """این واژه پیدا نشد!"""

    # make a message to send to telegram
    message = {
        # chat id should be id of the one who had requested
        "chat_id":chat_id,
        # text is command output in monospace format
        "text":out,
        # set parse mode to markdown so that text can be in monospace
        "parse_mode":"HTML",
    }

    # send the message
    a = requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', data=message)



def dict2telegram(dictext):
    text = ""

    for entry in dictext:
        # print(entry)
        text += f"""
🔆<b>{entry['dict_name']}</b>
        """
        for res in entry['result']:
            text += f"""
🍊<i>{res['word']}</i>
            """
            text += f"""
{res['definition']}
            """
    return text