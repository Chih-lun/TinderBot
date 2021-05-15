from tinderbot import Tinderbot

username = input('Enter your user name: ')
password = input('Enter your password: ')

tinderbot = Tinderbot()
tinderbot.login(username,password)
tinderbot.auto_like()