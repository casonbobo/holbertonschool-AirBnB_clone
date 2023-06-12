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
            print ("** instance id missing **")
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
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_objs = self.storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3].strip('"')
        if attr_name in ["id", "created_at", "updated_at"]:
            return
        obj = all_objs[instance_key]
        setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
        self.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
