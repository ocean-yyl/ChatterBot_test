# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 18:20
# software: PyCharm
"""
Training your chat bot  训练您的聊天机器人
You can run the training process multiple times.
You can also run the train command on a number of different example dialogs(对话).
"""
from chatterbot import ChatBot

bot = ChatBot(
	'Norman',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database_uri='sqlite:///database.sqlite3',
	logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
		'chatterbot.logic.TimeLogicAdapter'
	],
)

#######关键代码#########
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
	'How are you?',
	'I am good.',
	'That is good to hear.',
	'Thank you',
	'You are welcome.',
])
#######关键代码#########
while True:
	try:
		bot_input = bot.get_response(input("Inputs:"))
		print("Norman:",bot_input)
	except(KeyboardInterrupt, EOFError, SystemExit):
		break