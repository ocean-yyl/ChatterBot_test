# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 19:07
# software: PyCharm
"""
Preprocessors 预处理
ChatterBot’s preprocessors are simple functions that
modify the input statement that a chat bot receives
before the statement gets processed by the logic adaper.
ChatterBot的预处理器是简单的函数，可在逻辑适配器对语句进行处理之前，修改聊天机器人收到的输入语句。
"""
from chatterbot import ChatBot
chatbot = ChatBot(
	'Bob the Bot',
	preprocessors=[
		'chatterbot.preprocessors.clean_whitespace'
	]
)


"""Creating new preprocessors"""

