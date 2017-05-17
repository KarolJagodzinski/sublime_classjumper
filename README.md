Description
---------------

This plugin allows you to jump between Python's classes and methods in active view.


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
    { "keys": [<keys>], "command": "class_jumper", "args": {"direction": "up, "jump_to": "class"} },
    { "keys": [<keys>], "command": "class_jumper", "args": {"direction": "down, "jump_to": "class"} }
    { "keys": [<keys>], "command": "class_jumper", "args": {"direction": "up, "jump_to": "method"} },
    { "keys": [<keys>], "command": "class_jumper", "args": {"direction": "down, "jump_to": "method"} }
]
```

where `<keys>` should be changed to proper key bindings i.e.
```
[
    { "keys": ["super+home"], "command": "class_jumper", "args": {"direction": "up, "jump_to": "class"}},
    { "keys": ["super+end"], "command": "class_jumper", "args": {"direction": "down, "jump_to": "class"}},
    { "keys": ["super+pageup"], "command": "class_jumper", "args": {"direction": "up, "jump_to": "method"}},
    { "keys": ["super+pagedown"], "command": "class_jumper", "args": {"direction": "down, "jump_to": "method"}}
]
```
