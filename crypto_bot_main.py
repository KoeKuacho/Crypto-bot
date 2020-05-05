# -*- coding: utf-8 -*-

import config
import telebot
import requests
import datetime
import time

bot = telebot.TeleBot(config.token)


def log(message):
    """ Logging users messages """
    print('<------------------------------------->')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(f'Message by - {message.from_user.first_name} {message.from_user.last_name}\n {message.text}')


@bot.message_handler(commands=['start'])
def welcome(message):
    """ After 'start' func sends welcome message """
    log(message)

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJNWF6eCSYDgIXlUPr1U5_ca406t5FVAAL7BQAClvoSBZdb7eV44WgWGAQ')
    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(2)

    bot.send_message(message.chat.id,
                     "🕺 Let's check how much ₿ or Ripple is worth right now 📈 Or maybe you want to see the cost of TOP7 coins. It`s easy.\n"
                     "\nJust tap on the commands: \n"
                     "/top7 - check TOP7 price crypto by Binance\n"
                     "/btc - check BTC price by Binance\n"
                     "/xrp - check Ripple price by Binance\n"
                     "/eth - check Ethereum price by Binance\n"
                     "/info - bot info")


# https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT sample link for request

@bot.message_handler(commands=['btc'])
def price_btc(message):
    """ Sends current price of BTC by Binance """
    log(message)

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url).json()
    coin_name = response['symbol'].split('USDT')[1]
    price = float(response['price'])
    price_coin = f'1BTC = {coin_name} {price} usdt'

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    bot.send_message(message.chat.id, price_coin)


@bot.message_handler(commands=['xrp'])
def price_xrp(message):
    """ Sends current price of XRP by Binance """
    log(message)

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT'
    response = requests.get(url).json()
    coin_name = response['symbol'].split('USDT')[1]
    price = float(response['price'])
    price_coin = f'1XRP = {coin_name} {price} usdt'

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    bot.send_message(message.chat.id, price_coin)


@bot.message_handler(commands=['eth'])
def price_eth(message):
    """ Sends current price of ETH by Binance """
    log(message)

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    response = requests.get(url).json()
    coin_name = response['symbol'].split('USDT')[1]
    price = float(response['price'])
    price_coin = f'1ETH = {coin_name} {price} usdt'

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(1)

    bot.send_message(message.chat.id, price_coin)


@bot.message_handler(commands=['top7'])
def price_top10(message):
    """ Sends current price of TOP7 coins by Binance """

    log(message)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJNzF6fRPCRXTiwrXw9gHPqAAFWacOGLAACEAYAApb6EgWKFCUqPYiR0BgE')

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(0.1)

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url).json()
    btc_name = response['symbol'].split('USDT')[1]
    price_b_j = float(response['price'])
    btc_price = f'1BTC = {btc_name} {price_b_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT'
    response = requests.get(url).json()
    xrp_name = response['symbol'].split('USDT')[1]
    price_x_j = float(response['price'])
    xrp_price = f'1XRP = {xrp_name} {price_x_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    response = requests.get(url).json()
    eth_name = response['symbol'].split('USDT')[1]
    price_e_j = float(response['price'])
    eth_price = f'1ETH = {eth_name} {price_e_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BCHUSDT'
    response = requests.get(url).json()
    bch_name = response['symbol'].split('USDT')[1]
    price_bc_j = float(response['price'])
    bch_price = f'1BCH = {bch_name} {price_bc_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT'
    response = requests.get(url).json()
    ltc_name = response['symbol'].split('USDT')[1]
    price_l_j = float(response['price'])
    ltc_price = f'1LTC = {ltc_name} {price_l_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT'
    response = requests.get(url).json()
    bnb_name = response['symbol'].split('USDT')[1]
    price_bn_j = float(response['price'])
    bnb_price = f'1BNB = {bnb_name} {price_bn_j} usdt'

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=EOSUSDT'
    response = requests.get(url).json()
    eos_name = response['symbol'].split('USDT')[1]
    price_e_j = float(response['price'])
    eos_price = f'1EOS = {eos_name} {price_e_j} usdt'

    bot.send_message(message.chat.id,
                     f'{btc_price}\n{xrp_price}\n{eth_price}\n{bch_price}\n{ltc_price}\n{bnb_price}\n{eos_price}'
                     f'\n\nCrypto to the moon 🚀')

@bot.message_handler(commands=['info'])
def info(message):
    """ Sends information about the author  """
    log(message)

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJd-F6w1wOGXu4SoRi3pBgo7Yelzx86AAImBgAClvoSBT54uAwflqC1GQQ')

    bot.send_chat_action(message.chat.id, action='typing')
    time.sleep(0.2)

    bot.send_message(message.chat.id, f'Hey 🖐 I`m so glad you wanna know more about the project. '
                                          f'I hope the bot performed everything perfectly 🤖 '
                                          f'\nI will be happy for a cup of coffee for me ☕')

    bot.send_message(message.chat.id, f'💰 BTC:')
    bot.send_message(message.chat.id, f'1B549zLRXJQd31gcVFbZZRqyqfeTzNnx33')

    bot.send_message(message.chat.id, f'💰 ETH:')
    bot.send_message(message.chat.id, f'0x08beDB512392e4Ea5A8080d61F68BEc6bc959188')

    bot.send_message(message.chat.id, f'💰 XRP:')
    bot.send_message(message.chat.id, f'raq6g4UbK455dBARweSQFDhMSDRwV5FaDE')


if __name__ == '__main__':
    # bot running
    bot.infinity_polling()
