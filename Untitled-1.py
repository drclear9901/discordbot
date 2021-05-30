# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz
from discord import message

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("정상적으로 실행되었습니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("개발중"))

@client.event
async def on_message(message):
    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(828047125337604136)
            embed = discord.Embed(title="**새벽길드 공지사항**", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            await channel.send (embed=embed)
            await message.author.send("*[ BOT 알림 ]* | 등록 완료 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODQ4NTI3NjY2NDI4MTE2OTky.YLN6-A.vk16kXev6c9GVTwnqd2hjN6rUt8')