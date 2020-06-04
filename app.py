import json
import feedparser
from time import sleep
from functools import wraps
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler


def get_config():
    with open("config/config.json", "r") as read_file:
        config = json.load(read_file)
        return config


updater = Updater(get_config()["telegram_token"], use_context=True)


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        chat_id = get_config()["admin_chat_id"][0]
        if user_id != chat_id:
            updater.bot.send_message(chat_id=chat_id, text=f'Unauthorized access denied for {user_id}')
        return func(update, context, *args, **kwargs)
    return wrapped


class UpworkFeed:
    def __init__(self):
        self.entries_list = []

    def parsed_feed(self, url):
        while True:
            sleep(5)
            parsed_feed = feedparser.parse(url)
            if parsed_feed.status == 200:
                return parsed_feed

    def new_posts(self, url):
        if len(self.entries_list) != 0:
            new_parsed_data = self.parsed_feed(url)
            new_entries_list = [v for k, v in new_parsed_data.items() if k == 'entries']
            new_jobs = []

            for t in new_entries_list[0]:
                if t['link'] not in [t['link'] for t in self.entries_list[0]]:
                    new_jobs.append(t)
            self.entries_list = new_entries_list
            return reversed(new_jobs)
        else:
            parsed_data = self.parsed_feed(url)
            self.entries_list = [v for k, v in parsed_data.items() if k == 'entries']
            return reversed(self.entries_list[0])

    def format_msg(self, msg_list):
        formated_msgs = []
        for msg in msg_list:
            soup = BeautifulSoup((msg['summary']), features="html.parser")
            description = soup.get_text().replace('Budget', '\n\nBudget').replace('Skills:', '\n\nSkills:\n').replace('Posted On:', '\nPosted On:').replace('Category:', '\n\nCategory:').replace('Country:', '\nCountry:').replace('click to apply', msg['link'])
            if len(description) >= 4096:
                formated_msgs.append(f"{msg['title']}\n\ndescription is too long, to see full version please visit the web site...")
            else:
                formated_msgs.append(f"{msg['title']}\n\n{description}")
        return formated_msgs


@restricted
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello\n\nto start type /feed name\n\nfor example /feed main')


@restricted
def get_feed(update, context):
    if len(" ".join(context.args)) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id,text='To start type /feed name')
    feed_name = context.args[0]
    if feed_name not in [k for k in get_config().keys()]:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Type correct feed name!')

    feed = UpworkFeed()
    while True:
        try:
            sleep(20)
            new_msg = feed.format_msg(feed.new_posts(get_config()[feed_name]))
            for msg in new_msg:
                sleep(5)
                context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
        except Exception as e:
            updater.bot.send_message(chat_id=get_config()["admin_chat_id"][0], text=str(e))


def main():
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("feed", get_feed))

    updater.start_polling()
    # updater.idle()


if __name__ == "__main__":
    main()
