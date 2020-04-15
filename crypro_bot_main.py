# -*- coding: utf-8 -*-

import config
import telebot
import requests

bot = telebot.TeleBot(config.token)

# 'https://www.binance.com/fapi/v1/ticker/24hr'

all_tokens = []


def get_all_tokens():
    url = 'https://www.binance.com/fapi/v1/ticker/24hr'
    response = requests.get(url).json()
    for all_s in response:
        token = {
            'symbol': all_s['symbol'],
            'price': all_s['lastPrice']
        }
        if token not in all_tokens:
            all_tokens.append(token)
    return all_tokens


@bot.message_handler(commands=['btc'])
def price_btc(message):
    get_all_tokens()

    for token in all_tokens:
        if 'BTCUSDT' in token['symbol']:
            last_price = token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['xrp'])
def price_btc(message):
    get_all_tokens()

    for token in all_tokens:
        if 'XRPUSDT' in token['symbol']:
            last_price = token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['eth'])
def price_btc(message):
    get_all_tokens()

    for token in all_tokens:
        if 'ETHUSDT' in token['symbol']:
            last_price = token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['top10'])
def price_btc(message):
    get_all_tokens()
    print(all_tokens[0:11])

    bot.send_message(message.chat.id, f"{all_tokens[0]['symbol'].split('USDT')[0]}  {all_tokens[0]['price']} usdt\n"
                                      f"{all_tokens[1]['symbol'].split('USDT')[0]}  {all_tokens[1]['price']} usdt\n"
                                      f"{all_tokens[2]['symbol'].split('USDT')[0]}  {all_tokens[2]['price']} usdt\n"
                                      f"{all_tokens[3]['symbol'].split('USDT')[0]}  {all_tokens[3]['price']} usdt\n"
                                      f"{all_tokens[4]['symbol'].split('USDT')[0]}  {all_tokens[4]['price']} usdt\n"
                                      f"{all_tokens[5]['symbol'].split('USDT')[0]}  {all_tokens[5]['price']} usdt\n"
                                      f"{all_tokens[6]['symbol'].split('USDT')[0]}  {all_tokens[6]['price']} usdt\n"
                                      f"{all_tokens[7]['symbol'].split('USDT')[0]}  {all_tokens[7]['price']} usdt\n"
                                      f"{all_tokens[8]['symbol'].split('USDT')[0]}  {all_tokens[8]['price']} usdt\n"
                                      f"{all_tokens[9]['symbol'].split('USDT')[0]}  {all_tokens[9]['price']} usdt\n")


if __name__ == '__main__':
    bot.infinity_polling()
