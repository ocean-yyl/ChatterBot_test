# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 16:05
# software: PyCharm
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Charlie', read_only=True)

trainer = ListTrainer(chatbot)
conversation = [
	"Hello",
	"Hi there!",
	"How are you doing?",
	"I'm doing great.",
	"That is good to hear",
	"Thank you.",
	"You're welcome."
]
trainer.train(conversation)

while True:
	request = str(input("User: "))
	if request == 'stop':
		break
	response = chatbot.get_response(request)
	print('Bot: ' + str(response))
