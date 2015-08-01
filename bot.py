# -*- coding: utf-8 -*-
import os, json

from flask import Flask, request
app = Flask(__name__)
app.config.from_object('config.Config')
token = app.config.get('TOKEN')

import plugins
from plugin import Plugin
print Plugin.plugins

@app.route('/', methods=['POST'])
def telegramWebHook():
    data = request.json['message']
    print json.dumps(data, indent=2)
    chat = data['chat']['id']
    if data['text'][0] == '/':
        try:
            command, args = data['text'].split(None, 1)
        except:
            command = data['text']
            args = None

        command = command[1:].lower()
        print command
        if command in Plugin.plugins:
            Plugin.plugins[command].exe(data)
    else:
        for plugin, instance in Plugin.plugins.items():
            if instance.onMessage:
                instance.exe(data)
    return ""
