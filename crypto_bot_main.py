# -*- coding: utf-8 -*-

import config
import telebot
import requests
import datetime
import time

bot = telebot.TeleBot(config.token)

all_tokens = []


def log(message):
    """ Logging users messages """

    print('<------------------------------------->')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(f'Message by - {message.from_user.first_name} {message.from_user.last_name}\n {message.text}')


def get_all_tokens():
    """
    Gets list of tokens from Binance https://www.binance.com/fapi/v1/ticker/24hr
    :return: list all_tokens
    """
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
    """ After 'start' func sends welcome message """
    log(message)

    bot.send_message(message.chat.id,
                     "🕺 Let's check how much ₿ or Ripple is worth right now 📈 Or maybe you want to see the cost of TOP🔟 coins. It`s easy.\n"
                     "\nJust tap on the commands: \n"
                     "/top10 - check TOP10 price crypto by Binance\n"
                     "/btc - check BTC price by Binance\n"
                     "/xrp - check Ripple price by Binance\n"
                     "/eth - check Ethereum price by Binance")


@bot.message_handler(commands=['btc'])
def price_btc(message):
    """ Sends current price of BTC by Binance """
    log(message)
    get_all_tokens()

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    for token in all_tokens:
        if 'BTCUSDT' in token['symbol']:
            last_price = '1 BTC = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['xrp'])
def price_xrp(message):
    """ Sends current price of XRP by Binance """
    log(message)
    get_all_tokens()

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    for token in all_tokens:
        if 'XRPUSDT' in token['symbol']:
            last_price = '1 XRP = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['eth'])
def price_eth(message):
    """ Sends current price of ETH by Binance """
    log(message)
    get_all_tokens()

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    for token in all_tokens:
        if 'ETHUSDT' in token['symbol']:
            last_price = '1 ETH = ' + ' ' + token['price'] + ' ' + 'usdt'
            bot.send_message(message.chat.id, last_price)
            all_tokens.clear()


@bot.message_handler(commands=['top10'])
def price_top10(message):
    """ Sends current price of TOP10 coins by Binance """

    log(message)
    get_all_tokens()

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

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
    # bot running
    bot.infinity_polling()
