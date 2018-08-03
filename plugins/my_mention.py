from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@respond_to('メンション')
def mention_func(message):
	message.reply('私にメンションをとっても何もないよ')

@listen_to('リッスン')
def listen_func(message):
	message.send('誰だね？')
	message.reply('君か')

@respond_to('かっこいい')
def cool_func(message):
	message.react('+1')
