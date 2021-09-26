
from aiocron        import crontab
from discord.ext    import commands

import discord


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

    @crontab('0 * * * *')
    async def every_hour(ctx = False):
        # gss_notice_update
        ctx = ctx if ctx else bot.get_channel(channel_id['gss-notice'])

        from command.scraper.GSSWatchdog import GSS

        new = GSS().get_new()
        for m in new['top_notices'] + new['notices']:
            embed = discord.Embed(
                title   = m['Title'],
                url     = m['href']
            )
            embed.set_author(name = m['Writer'])

            await ctx.send(embed=embed)

        # 0x3F_update
        ctx = ctx if ctx else bot.get_channel(channel_id['0x3f'])

        from command.scraper.x3F import x3F

        msg = ""
        news = x3F().get_new()
        for n in news:
            msg += f'{n}\n{news[n]}\n'
        await ctx.send(msg)

    # @crontab('* * * * *')
    @bot.command()
    async def ping(ctx = False):
        ctx = ctx if ctx else bot.get_channel(channel_id['test'])
        await ctx.send("pong")

    @bot.command()
    async def x3F(ctx, *args):
        from command.x3F import x3F
        await ctx.send(x3F().commands(args))

    import util.config
    bot.run(util.config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
