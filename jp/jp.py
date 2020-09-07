import typing
import datetime
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel
from core.paginator import EmbedPaginatorSession

from .resources.join import JoinResource

class Jp(commands.Cog):
    """Get join position of a member in your server"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["joinp"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def joinposition(self, ctx, *, member: typing.Union[discord.Member, str] = None):
        """Get the join position of a member."""

        embed = JoinResource(ctx, member).join_embed()
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Jp(bot))