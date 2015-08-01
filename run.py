from bot import app
from telegram import Bot
from plugin import Plugin

if __name__ == "__main__":
    commands = [instance.name for plugin,instance in Plugin.plugins.items() if instance.command]
    print commands
    bot = Bot(app.config.get('TOKEN'))
    bot.setWebhook(app.config.get('WEBHOOK'))
    app.run(debug=True, port=80, host="0.0.0.0")

