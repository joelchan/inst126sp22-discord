""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn (https://krypt0n.co.uk)
Description:
This is a template to create your own discord bot in python.

Version: 4.1
"""

from tokenize import String
from exceptions import *
from typing import TypeVar, Callable
import json
import os
import platform
from pydoc import describe
import random
import sys
from Classes.errortype import errors

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

import helpers.checks as checks

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class General(commands.Cog, name="general-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="botinfo",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def botinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the bot.
        :param context: The context in which the command has been executed.
        """
        embed = disnake.Embed(
            description="Used [Krypton's](https://krypt0n.co.uk) template",
            color=0x9C84EF
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="INST126 Dev Team",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Slash Commands) or {config['prefix']} for normal commands",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.command(
        name="serverinfo",
        description="Get some useful (or not) information about the server.",
    )
    @checks.not_blacklisted()
    async def serverinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the server.
        :param context: The context in which the command has been executed.
        """
        roles = [role.name for role in context.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)

        embed = disnake.Embed(
            title="**Server Name:**",
            description=f"{context.guild}",
            color=0x9C84EF
        )
        embed.set_thumbnail(
            url=context.guild.icon.url
        )
        embed.add_field(
            name="Server ID",
            value=context.guild.id
        )
        embed.add_field(
            name="Member Count",
            value=context.guild.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{len(context.guild.channels)}"
        )
        embed.add_field(
            name=f"Roles ({len(context.guild.roles)})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {context.guild.created_at}"
        )
        await context.send(embed=embed)

    @commands.command(
        name="ping",
        description="Check if the bot is alive.",
    )
    @checks.not_blacklisted()
    async def ping(self, context: Context) -> None:
        """
        Check if the bot is alive.
        :param context: The context in which the command has been executed.
        """
        embed = disnake.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0x9C84EF
        )
        await context.send(embed=embed)

    @commands.command(
        name="invite",
        description="Get the invite link of the bot to be able to invite it.",
    )
    @checks.not_blacklisted()
    async def invite(self, context: Context) -> None:
        """
        Get the invite link of the bot to be able to invite it.
        :param context: The context in which the command has been executed.
        """
        embed = disnake.Embed(
            description=f"Invite me by clicking [here](https://discordapp.com/oauth2/authorize?&client_id={config['application_id']}&scope=bot+applications.commands&permissions={config['permissions']}).",
            color=0xD75BF4
        )
        try:
            # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except disnake.Forbidden:
            await context.send(embed=embed)

    @commands.command(
        name="server",
        description="Get the invite link of the discord server of the bot for some support.",
    )
    @checks.not_blacklisted()
    async def server(self, context: Context) -> None:
        """
        Get the invite link of the discord server of the bot for some support.
        :param context: The context in which the command has been executed.
        """
        embed = disnake.Embed(
            description=f"Join the support server for the bot by clicking [here](https://discord.gg/mTBrXyWxAF).",
            color=0xD75BF4
        )
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except disnake.Forbidden:
            await context.send(embed=embed)

    @commands.command(
        name="error",
        description="Tell the bot about an error you are encountering and it'll try to help"
    )
    @checks.not_blacklisted()
    async def error_help(self, context: Context) -> None:

        # Respond once error command is triggered
        await context.send(f'Hey {context.author.name}, what error are you encountering? Or Type help to get list of errors')

        should_listen = True
        while should_listen:

            # Wait for a message from the user who triggered the bot for 60 seconds
            msg = await context.bot.wait_for("message", check=lambda message: message.author == context.author, timeout=60.0)
            embed = disnake.Embed()
            
             # This is where we'll handle all the logic for determining what the user needs help with
            if msg.content.lower() == "help":  # Show a list of all errors the user can get help with
                embed.title = "**List of Errors:**"
                embed.description = f"\n".join("**{}**".format(k.name) for k in errors)
                embed.set_footer(text="Just type any of these errors and I'll help")
                embed.color = 0x9C84EF

            elif msg.content.lower() in list(map(lambda error: error.name.lower(), errors)):
                should_listen = False
                chosen_error = list(filter(lambda error: error.name.lower() == msg.content.lower(), errors))[0]
                embed.title = chosen_error.name
                embed.description = chosen_error.description
                if chosen_error.image:
                    embed.add_field(name="Example:", value="Check it out!", inline=False)
                    embed.set_image(file=disnake.File(chosen_error.image))
            else:
                embed.title = "**Hmmmmmm**"
                embed.description = "That doesn't appear to be an error. Type help to get list of errors"

            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
