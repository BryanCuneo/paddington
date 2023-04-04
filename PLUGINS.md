# Plugins
Plugins provide functionality to your bot via [Extensions](https://docs.pycord.dev/en/stable/ext/commands/extensions.html) and [Cogs](https://docs.pycord.dev/en/stable/ext/commands/cogs.html) that are loaded automatically at runtime. You can find a collection of plugins that I have written over at [dbot-plugins](https://github.com/BryanCuneo/dbot-plugins).

## Single-file
A self-contained extension file. [dice_roller.py](/plugins/dice_roller.py) is a very basic single-file plugin that registers a simple command.

## Multi-file
If you wish to spread your plugin across multiple files, you can do so via subfolders within your plugins directory like so:

```
dbot/
├─ plugins/
│  ├─ multi_file_plugin/
│  │  ├─ __init__.py
│  │  ├─ do_stuff.py
|  |  ├─ config.toml
```

Check out the [recurring message scheduler](/plugins/recurring_messages) for an example of a multi-file plugin.

`__init__.py` is the required entry point for multi-file plugins.

## Creating a plugin
Using [create_plugin.py](/create_plugin.py) you can generate plugin templates.

<details>

  <summary>Multi-file plugins</summary>

  ```
  $> python .\create_plugin.py "Test Plugin"

  Building new plugin - Test Plugin
  ------------------------------------------
  Folder name: test_plugin
  Class name: TestPlugin
  Acronym: tp
  Creating base directory: plugins\test_plugin... Done
  Creating files... Done

  Success
  $>
  ```
</details>

<details>

  <summary>Single-file plugins</summary>

  ```
  $> python .\create_plugin.py -s "Test Plugin"

  Building new plugin - Test Plugin
  ------------------------------------------
  Folder name: test_plugin
  Class name: TestPlugin
  Acronym: tp
  Creating plugin file plugins\test_plugin.py... Done

  Success
  $>
  ```
</details>
