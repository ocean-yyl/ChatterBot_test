# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 19:07
# software: PyCharm
"""
Setting the training class
ChatterBot comes with training classes built in, or you can create your own if needed.
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Training Example')
trainer = ListTrainer(chatbot)

trainer.train([
	"Hi there!",
	"Hello",
])

trainer.train([
	"Greetings!",
	"Hello",
])

"""
Training with corpus data
ChatterBot comes with a corpus data and utility module that 
makes it easy to quickly train your bot to communicate. 
To do so, simply specify the corpus data modules you want to use.

"""
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
	"chatterbot.corpus.english"
)


"""It is also possible to import individual subsets of ChatterBot’s corpus at once."""
trainer.train(
	"chatterbot.corpus.english.greetings",
	"chatterbot.corpus.english.conversations"
)

"""
You can also specify file paths to corpus files or directories
 of corpus files when calling the train method.
"""
trainer.train(
	"./data/greetings_corpus/custom.corpus.json",
	"./data/my_corpus/"
)


"""
Training with the Ubuntu dialog corpus
This training class will handle the process of downloading the compressed corpus file 
and extracting it. 
If the file has already been downloaded, it will not be downloaded again. 
If the file is already extracted, it will not be extracted again.
"""
from chatterbot.trainers import UbuntuCorpusTrainer
trainer = UbuntuCorpusTrainer(chatbot)
trainer.train()


"""Creating a new training class"""