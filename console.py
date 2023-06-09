#!/usr/bin/python3
"""This is a console interpreter for the first AirBnB project"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Console interpreter that will do all of the back-end commands"""
    intro = "Welcome to MyCmdInterpreter! Type 'help' to see the available commands."
    prompt = "(hbnb) "

    def do_greet(self, args):
        """Greet the user"""
        print("Hello, {}!".format(args))

    def do_quit(self, args):
        """Exits"""
        print("Goodbye!")
        sys.exit()

    def do_EOF(self, args):
        """Exits"""
        print("Goodbye!")
        sys.exit()  

    def emptyline(self):
        """Override the default behavior of an empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
