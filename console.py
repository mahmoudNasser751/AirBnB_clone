#!/usr/bin/env python3

import re
import cmd
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.

    It sub-classes Python's `cmd.Cmd` class which provides a simple framework
    for writing line-oriented command interpreters.
    """

    prompt = "(hbnb) "
    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """Override default `empty line + return` behaviour.
        """
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
