"""Create the filestructure for a new plugin"""
import argparse
import sys
from pathlib import Path

from dbot_utilities import load_config

# Used for the __init__.py file in a multi-file plugin
init_file_content = """from pathlib import Path

import discord

from dbot_utilities import load_config


class {0}(discord.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    _{1}_group = discord.SlashCommandGroup("{2}", "{3}")

    @_{1}_group.command(description="{3} commands")
    async def test(self, ctx):
        await ctx.respond(self.config["plugin_name"])

def setup(bot):
    config = load_config(Path(__file__).parent.joinpath("config.toml"))
    bot.add_cog({0}(bot, config))
"""

# Used for the config.toml file in a multi-file plugin
config_file_content = """plugin_name = "{0}"
"""

# Used for the plugin_name.py file in a single-file plugin
main_file_content = """from pathlib import Path

import discord


class {0}(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    _{1}_group = discord.SlashCommandGroup("{2}", "{3}")

    @_{1}_group.command(description="{3} commands")
    async def test(self, ctx):
        await ctx.respond("{3}")

def setup(bot):
    bot.add_cog({0}(bot))
"""


def get_cli_args():
    """Parse command live arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pluginname",
        help="Create a new plugin folder with an __init__.py and config.toml.",
        type=str,
    )
    parser.add_argument(
        "--singlefile",
        "-s",
        help="Create a single-file plugin instead.",
        action="store_true",
    )

    return parser.parse_args()


def format_name(plugin_name):
    """Format a plugin name into a class name, folder name, and acronym. Example:
    Plugin name: Test Plugin Project
    Class name: TestPluginProject
    Folder name: test_plugin_project
    Acronym: tpp
    """
    clean_name = (
        "".join(char for char in plugin_name if (char.isalnum() or char in "_- "))
        .replace("_", " ")
        .replace("-", " ")
        .lower()
    )

    # Folder name with underscores as word delimeter
    folder_name = clean_name.replace(" ", "_")
    # CamelCase class name
    split_name = clean_name.split()
    class_name = "".join(word.capitalize() for word in split_name)
    # Lowercase acronym
    acronym = "".join([word[0] for word in split_name])

    print(
        "Folder name: {0}\nClass name: {1}\nAcronym: {2}".format(
            folder_name, class_name, acronym
        )
    )
    return folder_name, class_name, acronym


def create_plugin(plugin_name):
    folder_name, class_name, acronym = format_name(plugin_name)
    folder_path = Path(config["plugins_dir"], folder_name)
    try:
        print("Creating base directory: {0}...".format(folder_path), end="")
        folder_path.mkdir(parents=True, exist_ok=False)
        print(" Done")
    except FileNotFoundError:
        print(" Error: Directory already exists. Exiting.")
        exit

    print("Creating files...", end="")
    # Create an __init__.py file
    init_filepath = Path(folder_path, "__init__.py")
    with open(init_filepath, "x") as f:
        f.write(init_file_content.format(class_name, folder_name, acronym, plugin_name))

    # Create an empty config file
    config_filepath = Path(folder_path, "config.toml")
    with open(config_filepath, "x") as f:
        f.write(config_file_content.format(plugin_name))


def create_single_file_plugin(plugin_name):
    """Create a plugin file. No dedicated folder, no config, just a main python file."""
    folder_name, class_name, acronym = format_name(plugin_name)
    plugin_path = Path(config["plugins_dir"], folder_name + ".py")
    try:
        print("Creating plugin file {0}...".format(plugin_path), end="")
        with open(plugin_path, "x") as f:
            f.write(
                main_file_content.format(class_name, folder_name, acronym, plugin_name)
            )
    except FileExistsError:
        print(" Error: File already exists. Exiting.")
        exit


def main():
    """Generate a skeleton folder structure for a new plugin."""
    plugin_name = args.pluginname
    print("\nBuilding new plugin -", plugin_name)
    print("-" * (31 + len(plugin_name)))

    # If --singlefile or -s provided as a commandline argument, only create a single python file
    # Otherwise, create a dedicated folder for the plugin, an __init__.py, and a config.toml
    if args.singlefile:
        create_single_file_plugin(plugin_name)
    else:
        create_plugin(plugin_name)
    print(" Done\n\nSuccess")


if __name__ == "__main__":
    args = get_cli_args()
    config = load_config()
    main()
