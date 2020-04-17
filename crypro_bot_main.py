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


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "🕺 Let's check how much ₿ or Ripple is worth right now 📈 Or maybe you want to see the cost of TOP🔟 coins. It`s easy.\n"
                     "\nJust tap on the commands: \n"
                     "/top10 - check TOP10 price crypto by Binance\n"
                     "/btc - check BTC price by Binance\n"
                     "/xrp - check Ripple price by Binance\n"
                     "/eth - check Ethereum price by Binance")


@bot.message_handler(commands=['btc'])
def price_btc(message):
    get_all_tokens()

    for token in all_tokens:
        if 'BTCUSDT' in token['symbol']:
            last_price = '1 BTC = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['xrp'])
def price_xrp(message):
    get_all_tokens()

    for token in all_tokens:
        if 'XRPUSDT' in token['symbol']:
            last_price = '1 XRP = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['eth'])
def price_eth(message):
    get_all_tokens()

    for token in all_tokens:
        if 'ETHUSDT' in token['symbol']:
            last_price = '1 ETH = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['top10'])
def price_top10(message):
    get_all_tokens()

    bot.send_message(message.chat.id, f"1{all_tokens[0]['symbol'].split('USDT')[0]}  = {all_tokens[0]['price']} usdt\n"
                                      f"1{all_tokens[1]['symbol'].split('USDT')[0]}  = {all_tokens[1]['price']} usdt\n"
                                      f"1{all_tokens[2]['symbol'].split('USDT')[0]}  = {all_tokens[2]['price']} usdt\n"
                                      f"1{all_tokens[3]['symbol'].split('USDT')[0]}  = {all_tokens[3]['price']} usdt\n"
                                      f"1{all_tokens[4]['symbol'].split('USDT')[0]}  = {all_tokens[4]['price']} usdt\n"
                                      f"1{all_tokens[5]['symbol'].split('USDT')[0]}  = {all_tokens[5]['price']} usdt\n"
                                      f"1{all_tokens[6]['symbol'].split('USDT')[0]}  = {all_tokens[6]['price']} usdt\n"
                                      f"1{all_tokens[7]['symbol'].split('USDT')[0]}  = {all_tokens[7]['price']} usdt\n"
                                      f"1{all_tokens[8]['symbol'].split('USDT')[0]}  = {all_tokens[8]['price']} usdt\n"
                                      f"1{all_tokens[9]['symbol'].split('USDT')[0]}  = {all_tokens[9]['price']} usdt\n"
                                      f"\nCrypto to the moon 🚀")


if __name__ == '__main__':
    bot.infinity_polling()
