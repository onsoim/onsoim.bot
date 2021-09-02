
from discord.ext    import commands


def main():

    print("Starting @onsoim.bot")
    bot = commands.Bot(command_prefix='!')

    import json
    with open('res/channel.json') as f: channel_id = json.load(f)['debug']

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    import config
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
