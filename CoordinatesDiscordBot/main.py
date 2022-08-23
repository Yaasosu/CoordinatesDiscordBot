import nextcord
from nextcord.ext import commands #Import Library | Загружаем библиотеки
from nextcord.ui import Button,View

client = commands.Bot()
token = "" #Your token | Твой токен

#Code for Over | Код для вычисления по оверу
class over(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("Calculator | Калькулятор")  #X Coordinate | Кордината X
        self.X_Coordinate = nextcord.ui.TextInput(
            label="Enter X coordinates | Х кординаты",
            placeholder="Enter X coordinates | X кординаты",
            min_length=2,
            max_length=100,
        )
        self.add_item(self.X_Coordinate)

        self.Z_Coordinate = nextcord.ui.TextInput( #Z Coordinate | Кордината Z
            label="Enter Z coordinates | З кординаты",
            placeholder="Enter Z coordinates | З кординаты",
            min_length=2,
            max_length=100,
        )
        self.add_item(self.Z_Coordinate)

    async def callback(self, interaction: nextcord.Interaction): #Algorithm and text output | Алгоритм, и вывод текста
        a = float(self.Z_Coordinate.value)
        b = float(self.X_Coordinate.value)
        a_2 = a * 8
        b_2 = b * 8
        embed = nextcord.Embed(
            title="Over spawn coordinates | Кординаты спавна по Over",
            colour=nextcord.Colour.green()

        )
        embed.add_field(name='X Coordinates | X кординаты', value=b_2, inline=True)
        embed.add_field(name='Z Coordinates | З кординаты', value=a_2, inline=True)
        await interaction.send(embed=embed)


@client.slash_command( #output text through "/" | Вызов с помощью "/"
    name="nether",
    description="Write Your coordinate | Напишите свои кординаты",
)
async def send(interaction: nextcord.Interaction):
    modal = nether()
    await interaction.response.send_modal(modal)


#code from Nether | Код для вычисления по незеру

class nether(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("calculator") #X Coordinate | Кордината X

        self.X_Coordinate = nextcord.ui.TextInput(
            label="Enter X coordinates | X кординаты",
            placeholder="Enter X coordinates | Х кординаты",
            min_length=2,
            max_length=100,
        )
        self.add_item(self.X_Coordinate)

        self.Z_Coordinate = nextcord.ui.TextInput( #Z Coordinate | Кордината Z
            label="Enter Z coordinates | З кординаты",
            placeholder="Enter Z coordinates | З кординаты",
            min_length=2,
            max_length=100,
        )
        self.add_item(self.Z_Coordinate)

    async def callback(self, interaction: nextcord.Interaction): #Algorithm and text output | Алгоритм, и вывод текста
        a = float(self.Z_Coordinate.value)
        b = float(self.X_Coordinate.value)
        a_2 = a / 8
        b_2 = b / 8
        embed = nextcord.Embed(
            title="Nether spawn coordinates | Кординаты спавна по Nether",
            colour=nextcord.Colour.red()

        )
        embed.add_field(name='X Coordinates | Х кординаты', value=b_2, inline=True)
        embed.add_field(name='Z Coordinates | З кординаты', value=a_2, inline=True)
        await interaction.send(embed=embed)

@client.slash_command(#output text through "/" | Вызов с помощью "/"
    name="over",
    description="Write Your coordinate | Напишите свои кординаты",
)
async def send(interaction: nextcord.Interaction):
    modal = over()
    await interaction.response.send_modal(modal)

@client.slash_command( #output text through "/" | Вызов с помощью "/"
    name="help",
    description="Help menu | Хелп меню",
)
async def test(ctx): #button for message | Кнопка под сообщение
    button = Button(label="Continue ", style=nextcord.ButtonStyle.red)
    button1 = Button(label="Продолжить ", style=nextcord.ButtonStyle.blurple)

    async def English_HelpMenu(interaction):
        button = Button(label='Test "/over" ', style=nextcord.ButtonStyle.green)
        button1 = Button(label='Test "/nether" ', style=nextcord.ButtonStyle.red)

        async def Over_Menu2(interaction):
            await interaction.response.send_modal(modal=over())

        button.callback = Over_Menu2

        async def Nether_Menu2(interaction):
            await interaction.response.send_modal(modal=nether())

        button1.callback = Nether_Menu2

        view = View()
        view.add_item(button)
        view.add_item(button1)
        embed = nextcord.Embed(title="🛠 And here is all the information you need",color=nextcord.Colour.yellow(), type="rich")
        embed.add_field(name="1.Nether", value='How to use "/nether" ? I will give an example when you are in Over_World and you need to find out where and at what coordinates your portal will spawn in Nether_World.', inline=True)
        embed.add_field(name="2.Over", value='How to use "/over" ? I will give an example when you are in Nether_World and you need to find out where and at what coordinates your portal will be spawned in Over_World.', inline=True)
        embed.add_field(name="3.WARNING⚠", value='Be aware that the coordinates may be inaccurate. And they will be wrong by 1-10 blocks.', inline=True)
        embed.add_field(name="4.Additionally!",value='Below this message there are buttons, by clicking on them you can test the bot!',inline=True)
        await ctx.send(embed=embed, view=view)

    button.callback = English_HelpMenu

    async def Russian_HelpMenu(interaction):
        button = Button(label='Тест "/over" ', style=nextcord.ButtonStyle.green)
        button1 = Button(label='Тест "/nether" ', style=nextcord.ButtonStyle.red)

        async def Over_Menu2(interaction):
            await interaction.response.send_modal(modal=over())

        button.callback = Over_Menu2

        async def Nether_Menu2(interaction):
            await interaction.response.send_modal(modal=nether())

        button1.callback = Nether_Menu2

        view = View()
        view.add_item(button)
        view.add_item(button1)
        embed = nextcord.Embed(title="🛠 А вот и вся необходимая информация", color=nextcord.Colour.yellow(),type="rich")
        embed.add_field(name="1.Nether",value='Как использовать "/Nether" ? Я приведу пример, когда вы находитесь в Over_World и вам нужно узнать, где и по каким координатам спавнится ваш портал в Nether_World.',inline=True)
        embed.add_field(name="2.Over",value='Как использовать «/Over»? Я приведу пример, когда вы находитесь в Nether_World и вам нужно узнать, где и по каким координатам будет спавниться ваш портал в OverWorld.',inline=True)
        embed.add_field(name="3.Важно⚠",value='Имейте в виду, что координаты могут быть неточными. И они будут ошибаться на 1-10 блоков.',inline=True)
        embed.add_field(name="4.Дополнительно!",value='Ниже этого сообщения есть кнопки, нажав на них вы можете протестировать бота!',inline=True)

        await ctx.send(embed=embed, view=view)

    button1.callback = Russian_HelpMenu

    view = View()
    view.add_item(button)
    view.add_item(button1)
    embed = nextcord.Embed(title="🇺🇸",description='Hi, this is a help menu. Choose the language that is more convenient for you.',color=nextcord.Colour.yellow(), type="rich")
    embed.add_field(name="🇷🇺", value='Привет, это хелп-меню. Выбери тот язык который тебе удобнее.', inline=True)
    await ctx.send(embed=embed, view=view)

client.run(token)