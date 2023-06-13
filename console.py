#!/usr/bin/python3
"""This is a console interpreter for the first AirBnB project"""
import cmd
import sys
import os
import models
import shlex
from models.base_model import BaseModel
from models.models import model_classes
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg.split(" ")[0] not in model_classes.keys():
            print("** class doesn't exist **")
        elif " " not in arg:
            print("** instance id missing **")
        elif arg.replace(" ", ".") not in models.storage.all():
            print("** no instance found **")
        else:
            models.storage.remove(arg.replace(" ", "."))

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
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = models.storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg not in model_classes.keys() and arg != "":
            print("** class doesn't exist **")
        else:
            print(models.storage.all())

    def do_update(self, arg):
        """Updates an instacne based on the class name and id by
        adding or updating attributes"""
        a = shlex.split(arg)
        if len(a) == 0:
            print("** class name missing **")
        elif a[0] not in model_classes.keys():
            print("** class doesn't exist **")
        elif len(a) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(a) < 3:
            print("** attribute name missing **")
        elif len(a) < 4:
            print("** value missing **")
        else:
            k = "{}.{}".format(a[0], a[1])
            models.storage.update(models.storage.all()[k], a[2], a[3])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
