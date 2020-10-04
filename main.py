import platform
import subprocess

class App():
    def __init__(self):
        self.commands = {
            "2": "arp",
            "3": "exit"
        }
        # this breaks down if user is on windows but using something like
        # git bash, cygwin
        if platform.platform() == "Windows":
            self.commands["1"] = "ipconfig"
        else:
            self.commands["1"] = "ifconfig"
        
    def run(self):
        while True:
            try:
                print("Welcome to pynetworkutils, please select a command to run")
                print("---------------------------------------------------------")
                print("1. " + self.commands["1"])
                print("2. " + self.commands["2"])
                print("3. " + self.commands["3"])
                user_input = input()
                if user_input in self.commands:
                    # if user wants to exit
                    if user_input == "3":
                        break
                    else:
                        try:
                            flag = "-a"
                            process = subprocess.Popen(
                                [self.commands[user_input], flag], 
                                universal_newlines=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE
                            )
                            stdout, stderr = process.communicate()
                            if stderr:
                                raise Exception(stderr)
                            print(stdout)
                        except Exception as e:
                            print(e)
                else:
                    raise Exception("Unsupported command, please enter a command from the list of commands")
            except Exception as e:
                print(e)
                



if __name__ == "main":
    app = App()
    app.run()