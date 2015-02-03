# fork of ChainOfCommand
# github.com/jisaacks/ChainOfCommand

import sublime
import sublime_plugin

class OrigamiSplitRightCommand(sublime_plugin.WindowCommand):
    def run(self, commands):
        window = self.window
        for command in commands:
            command_name = command[0]
            command_args = command[1:]
            window.run_command(command_name, *command_args)

class OrigamiDestroyRightCommand(sublime_plugin.WindowCommand):
    def run(self, commands):
        window = self.window
        for command in commands:
            command_name = command[0]
            command_args = command[1:]
            window.run_command(command_name, *command_args)