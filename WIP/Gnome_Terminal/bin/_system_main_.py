import sys, os, random, subprocess, time, bin._system_ui_

class g_system(object):
    
    def __init__(self, file:str, dev:bool=False) -> None:
        """Main terminal architecture. Build constructure to begin.
        \nRequires; *file: str* = __file__
        \nNot Requried; *dev: bool* = toggles dev features, can also be toggled with switch_dev()"""
        self.emojis_goodbye = ["👋", "💤", "😴", "😭"]
        self.main_process = True
        self.devMode = dev
        self.header = "| Gnome Terminal™, (Python 3.8.4) |\n"
        self.system_clear(1)
        self.user = os.getlogin()
        self.active_session = file
    def system_clear(self,caller:int) -> bool:
        """Clears the terminal."""
        if sys.platform == "win32": os.system("cls")
        elif sys.platform == "linux" or sys.platform == "darwin": os.system("clear")
        else: return False
        if caller > 0: print(self.header)
        return True
    def display(self,data:str) -> bool:
        """Used to display stored variables.\n
        Currently partially broken"""
        spaces: list = []
        for i in range(len(data)):
            if data[i] == " ":
                spaces.append(i)
        new_d: list = data.split(" ")
        if self.devMode: print("\"Dev ->\" " + new_d)
        for i in range(len(new_d)):
            if i == 0: continue
            temp = "\""
            if new_d[i].startswith("\""): new_d[i] += "\""
            elif new_d[i].endswith("\""):
                new_d.insert()
                for k in range(len(new_d[i])):
                    temp += new_d[i][k]
                self.exe("print(str({0}), end=\"\", flush=True)".format(temp))
                continue
            self.exe("print(str({0}), end=\"\", flush=True)".format(new_d[i]))
        print("")
    def exe(self,comm:str) -> None:
        """Executes commands as system, used to run code during runtime.
        \nStoring variables is currently broken"""
        print("exec(\"{0}\")".format(comm))
        exec(comm)
    def switch_dev(self) -> bool:
        """Used to switch devmode on and off"""
        
        self.devMode = not self.devMode
        print("Developer Settings [ON]" if self.devMode else "Developer Settings [OFF]")
        return self.devMode
    def leave(self,caller:int,abort:bool) -> None:
        if not abort:
            calls = {0: "\033[F{0} ? leave                                ".format(self.user),1: "\u001b[999D{0} ? leave         ".format(os.getlogin())}
            print(calls.get(caller))

        print("Bye Bye! " + self.emojis_goodbye[random.randint(0, len(self.emojis_goodbye))-1])
        if not abort: quit()
        else: return
    def restarter(self) -> None:
        print("\033[F{0} ? restart                                ".format(self.user))

        # print("Bye Bye! " + self.emojis_goodbye[random.randint(0, len(self.emojis_goodbye))-1])
        self.leave(0,True)
        time.sleep(0.6)
        self.main_process = False
        subprocess.call(sys.executable + ' "' + os.path.realpath(self.active_session) + '"')
        quit()
    def display_ui(self) -> None:
        """Displays the terminal's UI.
        \nNot required, but recommended."""
        self.ui = bin._system_ui_.sys_ui._drawui_(self)