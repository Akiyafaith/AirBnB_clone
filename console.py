#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    define a command interpreter for the program
    the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        return True
    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    def help_quit(self):
        """
        Display help message for the quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help message for the EOF command.
        """
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
