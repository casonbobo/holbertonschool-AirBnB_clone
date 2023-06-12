#!/usr/bin/python3
"""This is a console interpreter for the first AirBnB project"""
import cmd
import sys
import os
import models
from models.base_model import BaseModel
from models.models import model_classes


class HBNBCommand(cmd.Cmd):
    """Console interpreter that will do all of the back-end commands"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a class"""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg not in model_classes.keys():
            print("** class doesn't exist **")
        else:
            my_model = model_classes[arg]()
            my_model.save()
            print(my_model.id)

    def do_greet(self, args):
        """Greet the user"""
        print("Hello, {}!".format(args))

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Goodbye!")
        sys.exit()

    def do_EOF(self, args):
        """Quit command to exit the program"""
        print("Goodbye!")
        sys.exit()  

    def emptyline(self):
        """Override the default behavior of an empty line"""
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in model_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print ("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = models.storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
