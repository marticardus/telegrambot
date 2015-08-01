from plugin import Plugin
import json, os

class trigger(Plugin):
    command = False
    onMessage = True

    def load_triggers(self):
        with open(os.path.join(os.path.dirname(__file__), 'trigger.json'), 'r') as fp:
            self.triggers = json.load(fp)

    def exe(self, request):
        self.load_triggers()
        for k, v in self.triggers.items():
            if k in request['text']:
                self.bot.sendMessage(chat_id=request['chat']['id'], text=v)
