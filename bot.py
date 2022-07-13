from tkinter import ON
import discord,asyncio,requests,json #導入模組
from discord.ext import commands

with open('config.json',mode='r') as file: #開啟config.json
    data=json.load(file)
PREFIX=data['prefix']
READYMSG=data['readymsg']
URL=data['url']
TOKEN=data['token']

bot=commands.Bot(command_prefix=PREFIX,help_command=None)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="地震Bot使用方法", description=f"{PREFIX}help | 傳送這則沒意義的訊息\n{PREFIX}setq | 創建名為`🛑地震速報`的頻道(會傳送地震訊息)",color=discord.Colour.random()) 
    await ctx.send(embed=embed)

@bot.command()
async def setq(ctx):
    channel=await ctx.guild.create_text_channel('🛑地震速報',category=ctx.channel.category)
    await channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send(f'已創建{channel.mention},請不要更改頻道名稱')
    embed=discord.Embed(title="地震速報", description=f"如果台灣發生區域性有感地震\n會及時發布在此頻道",color=discord.Colour.random())
    await channel.send(embed=embed)

@bot.event #事件
async def on_ready(): #當啟動時
    print(f'>>{bot.user}上線<<') #顯示{bot.user}上線,讓你知道成功啟動+
    #開啟時測試地震訊息
    if READYMSG == 'on': #如果設置為開啟
        for guild in bot.guilds:
                for channel in guild.channels:
                    if channel.name == "🛑地震速報": 
                        #偵測地震資訊
                        data = requests.get(URL) #開啟API
                        data_json = data.json()
                        eq = data_json['records']['earthquake'] #轉換成json格式
                        for i in eq:
                            content = i['reportContent'] #content=地震內容
                            picture=i['reportImageURI'] #picture=地震資訊圖片
                        embed=discord.Embed(title="地震訊息測試",description=f'{content}',color=discord.Colour.random())
                        embed.set_image(url=picture)
                        await channel.send(embed=embed)
    else:
        pass
    while True: #重複執行
        #偵測'60秒前'的資訊,做比對
        data = requests.get(URL) #開啟API
        data_json = data.json()
        eq = data_json['records']['earthquake'] #轉換成json格式
        for i in eq:
            lcontent = i['reportContent'] #lcontent=地震內容
        await asyncio.sleep(60) #等待60秒
        #偵測地震資訊
        data = requests.get(URL) #開啟API
        data_json = data.json()
        eq = data_json['records']['earthquake'] #轉換成json格式
        for i in eq:
            content = i['reportContent'] #content=地震內容
            picture=i['reportImageURI'] #picture=地震資訊圖片
        if str(lcontent)==str(content): #如果60秒前和60秒後的內容相同
            pass #不做任何事,繼續重複執行
        else: #否則(60秒前和60秒後的內容不相同,代表地震內容有更新,代表有更新的地震)
            for guild in bot.guilds: #設guild為bot在的所有群組
                for channel in guild.channels: #設channel為guild的所有頻道
                    if channel.name == "🛑地震速報": #如果這些頻道的名字為'🛑地震速報'
                        embed=discord.Embed(title="地震owo!",description=f'{content}',color=discord.Colour.random())
                        embed.set_image(url=picture)
                        await channel.send(embed=embed) #傳送地震訊息

bot.run(TOKEN)