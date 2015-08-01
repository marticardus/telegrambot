from bot import token
from telegram import Bot

class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        cls.name = name

        if not hasattr(cls, 'plugins'):
            cls.plugins = {}
        else:
            # Called when a plugin class is imported
            cls.register_plugin(cls)

    def register_plugin(cls, plugin):
        instance = plugin()
        cls.plugins[cls.name] = instance

class Plugin(object):
    __metaclass__ = PluginMount

    command = True
    onMessage = False

    def __init__(self):
        #self.bot = Bot(token=current_app.config['TOKEN'])
        self.bot = Bot(token=token)
