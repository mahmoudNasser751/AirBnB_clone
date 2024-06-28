#!/usr/bin/env python3

import re
import cmd
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    
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
        """Do nothing on empty input (just pressing ENTER)"""
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()