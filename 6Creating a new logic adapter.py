# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 20:19
# software: PyCharm
from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

	def __init__(self, chatbot, **kwargs):
		super().__init__(chatbot, **kwargs)

	def can_process(self, statement):
		return True

	def process(self, input_statement, additional_response_selection_parameters):
		import random

		# Randomly select a confidence between 0 and 1
		confidence = random.uniform(0, 1)

		# For this example, we will just return the input as output
		selected_statement = input_statement
		selected_statement.confidence = confidence

		return selected_statement

"""
If you create your own logic adapter 
you will need to have it in a separate file from your chat bot. 
Your directory setup should look something like the following:
──--project_directory
	├── cool_chatbot.py
	└── cool_adapter.py
Then you should be able to specify the following when you initialize your chat bot.
ChatBot(
    # ...
    logic_adapters=[
        {
            'import_path': 'cool_adapter.MyLogicAdapter'
        }
    ]
)
"""