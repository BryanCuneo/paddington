"""A small Discord bot framework."""
from pathlib import Path

import discord
from dbot_utilities import load_config


class Dbot(discord.Bot):
    _startup_message = """+--------------------------------------------------------+
| Welcome to Dbot - A plugin-based Discord bot framework |
| <https://github.com/BryanCuneo/dbot>                   |
|                                                        |
| Copyright 2018-2023 Bryan Cuneo                        |
| https://www.gnu.org/licenses/agpl-3.0.en.html          |
+--------------------------------------------------------+"""
    _ready_message = """
Logged in as: {0}
User ID: {0.id}
"""

    def __init__(self, plugins_dir):
        super().__init__()
        print(self._startup_message)

        print("Loading plugins from", plugins_dir)
        for plugin in Path(plugins_dir).iterdir():
            if plugin.stem != "__pycache__":
                print("*", plugin.stem)
                self.load_extension("plugins." + plugin.stem)

    # When the bot is fully initialized
    async def on_ready(self):
        print(Dbot._ready_message.format(self.user))


def main():
    bot = Dbot(config["plugins_dir"])
    bot.run(config["discord_access_token"])


if __name__ == "__main__":
    config = load_config()
    main()
