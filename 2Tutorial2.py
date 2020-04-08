# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 18:20
# software: PyCharm
"""
Specifying logic adapters 指定逻辑适配器
The logic_adapters parameter is a list of logic adapters.
In ChatterBot, a logic adapter is a class that takes an
input statement and returns a response to that statement.

您可以选择使用任意数量的逻辑适配器。
在此示例中，我们将使用两个逻辑适配器。当输入语句要求时，
TimeLogicAdapter返回当前时间。
MathematicalEvaluation适配器解决了使用基本运算的数学问题
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

while True:
	try:
		bot_input = bot.get_response(input("Inputs:"))
		print("Norman:",bot_input)
	except(KeyboardInterrupt, EOFError, SystemExit):
		break