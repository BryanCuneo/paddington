from pathlib import Path

import discord


class CozyCrew(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.yt_url = "https://www.youtube.com/channel/UCzeQN6qxZwyydWPOrR51YTQ"

    _cozy_crew_group = discord.SlashCommandGroup("cozy", "Cozy Crew")

    @_cozy_crew_group.command(description="About the Paddington bot")
    async def paddington(self, ctx):
        """Show information about this bot."""
        print("/cozy paddington: Showing info about Paddington")
        embed = discord.Embed(
            title="Paddington",
            description="A Discord bot for the BearCozy Crew community.",
        )

        embed.add_field(
            name="Features",
            value="Hero search for Awaken Chaos Era:\n * /ace hero\n\nBuffs, debuffs, etc:\n * /ace buffs\n * /ace debuffs\n\nRoll some dice:\n * /roll 6\n * /roll 3d8\n\nCozy Crew Commands:\n * /yt - BearCozy's YouTube channel",
            inline=False,
        )

        embed.add_field(
            name="GitHub Repository",
            value="[Paddington](https://github.com/BryanCuneo/paddington)",
        )
        embed.add_field(
            name="Built With",
            value="[DBot](https://github.com/BryanCuneo/dbot)\n[pyumilove](https://github.com/BryanCuneo/pyumilove)",
        )
        embed.add_field(
            name="License",
            value="[AGPLv3+](https://www.gnu.org/licenses/agpl-3.0.en.html)",
        )
        embed.add_field(
            name="Problem?",
            value="Contact your Discord server administrator or [submit an issue](https://github.com/BryanCuneo/paddington/issues)",
            inline=False,
        )

        await ctx.respond(embed=embed)

    @_cozy_crew_group.command(description="BearCozy Crew YouTube channel")
    async def yt(self, ctx):
        print("/cozy yt - " + self.yt_url)
        await ctx.respond(self.yt_url)


def setup(bot):
    bot.add_cog(CozyCrew(bot))
