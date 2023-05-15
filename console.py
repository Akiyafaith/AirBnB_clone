#!/usr/bin/python3
"""import the command interpreter module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    define a command interpreter for the program
    the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    
    def do_create(self, arg):
        """"Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
    else:
        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        obj_list =  []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] in storage.classes:
            for key in storage.all():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(storage.all()[key]))
        else:
            print("** class doesn't exist **")

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
        if key in storage.all():
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
            
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
