
from discord.ext    import commands


class Darwin:
    def __init__(self):
        self.mode   = 'debug'

class Linux:
    def __init__(self):
        self.mode   = 'release'

class Windows:
    def __init__(self):
        self.mode   = 'debug'


def main():

    print("Starting @onsoim.bot")
    bot = commands.Bot(command_prefix='!')

    import platform
    os = eval(platform.system())()

    import json
    with open('res/channel.json') as f: channel_id = json.load(f)[os.mode]

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    import config
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
