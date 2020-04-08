# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 19:30
# software: PyCharm
"""
Logic Adapters
Logic adapters determine the logic for how ChatterBot selects a response to a given input statement.
逻辑适配器确定ChatterBot如何选择对给定输入语句的响应的逻辑。

It is possible to enter any number of logic adapters for your bot to use.
If multiple adapters are used, then the bot will return
the response with the highest calculated confidence value.
If multiple adapters return the same confidence,
then the adapter that is entered into the list first will take priority.
可以输入任意数量的逻辑适配器供您的机器人使用。
如果使用了多个适配器，则漫游器将以计算出的最高置信度值返回响应。
如果多个适配器返回相同的置信度，则首先输入列表的适配器将具有优先权。
"""
# import chatterbot
# from chatterbot import ChatBot
# chatbot = ChatBot(
# 	"My ChatterBot",
# 	logic_adapters=[
# 		"chatterbot.logic.BestMatch"
# 	]
# )

"""
Common logic adapter attributes通用逻辑适配器属性
Each logic adapter inherits the following attributes and methods.
每个逻辑适配器都继承以下属性和方法。
[chatterbot.logic.LogicAdapter]  This is an abstract class that 
represents the interface that all logic adapters should implement.
"""
"""
Best Match Adapter
A logic adapter that returns a response based on known responses to 
the closest matches to the input statement.
The BestMatch logic adapter selects a response based on the best known match to a given statement.
"""

# Setting parameters
# chatbot = ChatBot(
# 	"My ChatterBot",
# 	logic_adapters=[
# 		{
# 			"import_path": "chatterbot.logic.BestMatch",
# 			"statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",# 可以是路径，也可以是类
# 			"response_selection_method": "chatterbot.response_selection.get_first_response"
# 		}
# 	]
# )




# Specific response example
# Create a new instance of a ChatBot
# from chatterbot import ChatBot
# bot = ChatBot(
# 	'Exact Response Example Bot',
# 	storage_adapter='chatterbot.storage.SQLStorageAdapter',
# 	logic_adapters=[
# 		{
# 			'import_path': 'chatterbot.logic.BestMatch'
# 		},
# 		{
# 			'import_path': 'chatterbot.logic.SpecificResponseAdapter',
# 			'input_text': 'Help me!',
# 			'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
# 		}
# 	]
# )
#
# # Get a response given the specific input
# response = bot.get_response('Help me!')
# print(response)

"""
# Low confidence response example
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
	'Example Bot',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		{
			'import_path': 'chatterbot.logic.BestMatch',
			'default_response': 'I am sorry, but I do not understand.',
			'maximum_similarity_threshold': 0.50
		}
	]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few responses
trainer.train([
	'How can I help you?',
	'I want to create a chat bot',
	'Have you read the documentation?',
	'No, I have not',
	'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)
"""