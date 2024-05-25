from termcolor import *
from clear_screen import clear_screen

class ErrorReturn():
    def __init__(self, command):
        self.command = command
    def CommandNotFoundError(self):
        cprint(f"Error:Type -> CommandNotFoundError\n\t{self.command} not in The End command", "red")
    def TValueError(self):
        cprint(f"Error:Type -> ValueError\n\t>!<number>!<", "red")
    def ErrorCommand(self):
        cprint(f"Error:Type -> ErrorCommand\nTarget:\n\tmap", "red")
    def CommandLost(self):
        cprint(f"Error:Type -> CommandLost\n\t>!{self.command} <target> <number>!<", "red")
    def TEOFError(self):
        cprint("Error:Type -> EOFError Ctrl-Z not use", "red")
class Terminal():
    def __init__(self):
        self.Fcommand = ["see"]
    def excute_command(self,user ,map) -> any:
        clear_screen()
        while True:
            try:
                self.command = input(">>>")
                error_return = ErrorReturn(self.command)
                if self.command.split()[0] == self.Fcommand[0]:
                    self.see(user, map, error_return)
                elif self.command == "exit":
                    break
                else:
                    error_return.CommandNotFoundError()
            except EOFError:
                error_return.TEOFError()
            except KeyboardInterrupt:
                break
            except IndexError:
                error_return.CommandNotFoundError()
    def see(self, user, map, error_return) -> any:
        try:
            if self.command.split()[1] == "map":
                try:
                    max = int(self.command.split()[2])
                    if max >= 0:
                        for j in range(max):
                            for i in range(max):
                                if map.map[user.x + i][user.y + j]:
                                    print(map.map[user.x + i][user.y + j].id, end=", ")
                                else:
                                    print("None", end=", ")
                        print("\n")
                    else:
                        for j in range(max):
                            for i in range(max):
                                if map.map[user.x + i][user.y + j]:
                                    print(map.map[user.x + i][user.y + j].id, end=", ")
                                else:
                                    print("None", end=", ")
                        print("\n")
                except IndexError:
                    pass
                except ValueError:
                    error_return.TValueError()
            else:
                error_return.ErrorCommand()
        except IndexError:
            error_return.CommandLost()
        del error_return, user, map