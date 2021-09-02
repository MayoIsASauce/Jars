class sys_ui(object):
    @staticmethod
    def _drawui_(self):
        while True:
            try: 
                u = input("{0} ? ".format(self.user))

                u_buffer = u.split(" ")
                if u_buffer[0].lower() == "clear": 
                    try: self.system_clear(int(u_buffer[1]))
                    except IndexError: self.system_clear(1)
                elif u_buffer[0].lower().startswith("display"): self.display(data=u)
                elif u_buffer[0].lower() == "leave": self.leave(0, False)
                elif u_buffer[0].lower() == "dev": self.switch_dev()
                elif u_buffer[0].lower() == "r" or u.lower().replace(" ", "") == "restart": self.restarter()
                else: self.exe(u)

            except Exception as e:
                print(e.args[0])

            except KeyboardInterrupt:
                if self.main_process: self.leave(1, False)
                else: quit()
                break