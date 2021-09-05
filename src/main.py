
from aiocron        import crontab
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

    import platform
    os = eval(platform.system())()

    print(f"Starting @onsoim.bot from {platform.system()}")
    bot = commands.Bot(command_prefix='!')

    import json
    with open('res/channel.json') as f: channel_id = json.load(f)[os.mode]

    # @crontab('* * * * *')
    @bot.command()
    async def ping(ctx = False):
        ctx = ctx if ctx else bot.get_channel(channel_id['test'])
        await ctx.send("pong")

    import config
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
