#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone project.

    This class provides a command-line interface to manage AirBnB objects.
    """

    prompt = "(hbnb) "

    # Dictionary of available classes
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def emptyline(self):
        """
        Do nothing when empty line + ENTER is pressed.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it and print the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print string representation of an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Print string representation of all instances or a class.
        Usage: all [class name]
        """
        objects = storage.all()
        result = []

        if not arg:
            for obj in objects.values():
                result.append(str(obj))
        else:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return

            for key, obj in objects.items():
                if key.startswith(arg + "."):
                    result.append(str(obj))

        print(result)

    def do_update(self, arg):
        """
        Update an instance based on class name and id.
        Usage: update <class name> <id> <attr name> "<attr value>"
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                if attr_type == int:
                    attr_value = int(attr_value)
                elif attr_type == float:
                    attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
