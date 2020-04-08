# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-08 18:20
# software: PyCharm
"""
Setting the storage adapter 设置存储适配器
ChatterBot带有内置的适配器类，使它可以连接到不同类型的数据库。
在本教程中，我们将使用SQLStorageAdapter允许聊天机器人连接到SQL数据库。
默认情况下，此适配器将创建一个SQLite数据库。

SQLStorageAdapter是ChatterBot的默认适配器。
如果未在构造函数中指定适配器，则将自动使用SQLStorageAdapter适配器。
"""
from chatterbot import ChatBot

bot = ChatBot(
	'Norman',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',# 配置存储适配器
	database_uri='sqlite:///mydb.sqlite3' # 存储路径
)