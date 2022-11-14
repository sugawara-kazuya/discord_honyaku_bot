# インストールした discord.py を読み込む
import discord
from googletrans import Translator
#from translate import Translator

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTAyODk0NzY1NTMxOTEwOTY4Mw.GfsWpc.9QXo2s1prq697UMAO8RJXal2scrh4DHl196VS0'

# 送りたいチャンネル指定
SEND_CHANNELID = 1035112058653528114
# メッセージを取りたいチャンネル指定
CHACH_CHANELID = 1037722976935739402
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())
translator = Translator()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # botの発言には反応しない
    if message.author.bot:
        return
    if message.channel.id == CHACH_CHANELID:
        if not message.author.bot:
            lang = translator.detect(message.content).lang
            channel = client.get_channel(SEND_CHANNELID)
            if lang == "en":
                trans_text = translator.translate(message.content, src = lang, dest = "ja").text
                await channel.send(trans_text)
            elif lang == "ja":
                trans_text = translator.translate(message.content, src = lang, dest = "en").text
                await channel.send(trans_text)
            elif lang == "vi":
                trans_text = translator.translate(message.content, src = lang, dest = "ja").text
                await channel.send(trans_text)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)