Description
---------------

This plugin allows you to jump between Python's classes in active view.



Using this tool
---------------

To use this plugin you have to go to your Sublime Text 3 Packages directory
and clone this repository

```
git clone git@github.com:KarolJagodzinski/sublime_classjumper.git
```

then you have to configure key bindings in your settings
**Preferences -> Key Bindings** and add following

```
[
    { "keys": [<keys>], "command": "class_jumper", "args": {"jump_to": "up"} },
    { "keys": [<keys>], "command": "class_jumper", "args": {"jump_to": "down"} }
]
```

where `<keys>` should be changed to proper key bindings i.e.
```
[
    { "keys": ["super+control+c+up"], "command": "class_jumper", "args": {"jump_to": "up"} },
    { "keys": ["super+control+c+down"], "command": "class_jumper", "args": {"jump_to": "down"} }
]
```
