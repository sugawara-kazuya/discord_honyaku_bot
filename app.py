# インストールした discord.py を読み込む
import discord
from googletrans import Translator
#from translate import Translator

# 自分のBotのアクセストークンに置き換えてください
env_1 = os.getenv('TOKENID')
TOKEN = env_1

# 送りたいチャンネル指定
env_2 = os.getenv('SENDCHANNELID')
SEND_CHANNELID = env_2
# メッセージを取りたいチャンネル指定
env_3 = os.getenv('CHACHCHANELID')
CHACH_CHANELID = env_3
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
