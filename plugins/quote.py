from plugin import Plugin

class quote(Plugin):
    def exe(self, request):
        print request
        self.bot.sendMessage(chat_id=request['chat']['id'], text='kk')
