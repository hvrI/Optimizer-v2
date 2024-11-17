import time

from tkinter import *
from tkinter import messagebox
from optimise import *



class GUI(Frame):
    def __init__(self, app):
        Frame.__init__(self)

        self.equal_signs = "=================================================\n"

        # GUI SETTINGS
        self.app = app
        self.app.title("Optimiser 1.1.0")
        self.app.geometry("1075x575")

        self.op = Name()

        # LOG TEXTBOX
        self.log_textBox = Text(self, state='disabled', height=23, width=273)
        self.vsb = Scrollbar(self, orient="vertical", command=self.log_textBox.yview)
        self.log_textBox.configure(yscrollcommand=self.vsb.set)
        self.log_textBox.place(x=30, y=10)
        self.vsb.pack(side="right", fill="y")

        # BUTTONS
        self.button_clear_logs = Button(self, text="Clear Logs", height=2, width=20, command=self.clear_logs)
        self.button_clear_logs.place(x=710, y=455)
        self.button_services_checker = Button(self, text="Services Checker", height=2, width=20, command=self.check_service)
        self.button_services_checker.place(x=30, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Untweak Services", height=2, width=20, command=self.untweak_service_handler)
        self.button_untweak_service_handler.place(x=30, y=455)
        self.button_tweak_all_services = Button(self, text="Tweak All Services", height=2, width=20, command=self.tweak_all_services)
        self.button_tweak_all_services.place(x=30, y=510)
        self.button_tweak_all_services = Button(self, text="Disable Antivirus", height=2, width=20, command=self.disable_antivirus)
        self.button_tweak_all_services.place(x=370, y=400)
        self.button_tweak_all_services = Button(self, text="Windows Settings Checker", height=2, width=20, command=self.check_windows_settings)
        self.button_tweak_all_services.place(x=200, y=400)


    def deco(func):
        """
        In order to write/change text in Textbox that's disabled,
        This wrapper changes textbox back to normal for text writing/editing purposes,
        then changing back to disable as before.
        """
        def inner(self):
            self.log_textBox.configure(state='normal')
            func(self)
            self.log_textBox.see("end")
            self.log_textBox.configure(state='disabled')
        return inner
    
    #
    # CLEAR LOG TEXTBOX FUNCTION
    #

    @deco
    def clear_logs(self):
        return self.log_textBox.delete("1.0", END)
    
    #
    #   SERVICES FUNCTIONS
    #

    @deco
    def check_service(self):
        results = self.op.service_checker()
        clean_log = ""
        error_log = ""
        untweak_log = ""

        for result in results:
            if result[1] not in [0, 1]:
                untweak_log += f"{result[0]} : Current Value: {result[1]} | Value: {result[2]}\n"
            elif result[1] == 0:
                clean_log += f"{result[0]}\n"
            else:
                error_log += f"{result[0]}\n"

        final_log = ("Tweaked Services\n" + self.equal_signs + clean_log + self.equal_signs + 
                     "Services Not Found or Inaccessible\n" + self.equal_signs + error_log + 
                    self.equal_signs + "Services Not Tweaked\n" + self.equal_signs + untweak_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)

    
    @deco
    def untweak_service_handler(self):
        results = self.op.latest_untweak_services
        final_log = "Updating Untweaked Services\n" + self.equal_signs

        if not results:
            return self.log_textBox.insert("end", "Please Run Services Checker before Using this Command. Unless All Tweaks for Services have been Applied.\n")
        
        for result in results:
            keyName = self.op.name_of_registry_key(result[0])
            original_value = result[-1]
            # REGISTRY ADD CHANGE FUNCTION HERE
            result = self.op.add_change_registry(result[0], result[1])
            if result[-1]:
                final_log += f"{keyName}: *{original_value}* => *{result[2]}*\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                self.log_textBox.insert("end", f"ERROR: {keyName}\n")
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()
        

    @deco
    def tweak_all_services(self):
        results = self.op.all_services_tweak() # Generator (Key_Name, True/False)
        tweaked_log = ""
        error_log = ""
        
        for result in results:
            if result[-1]:
                tweaked_log += result[0] + "\n"
            else:
                error_log += result[0] + "\n"


        final_log = ("Tweaked Services\n" + self.equal_signs + tweaked_log + self.equal_signs + 
                     "Services Not Found or Inaccessible\n" + self.equal_signs + error_log + 
                    self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    

    #
    # CLEAR LOG FILEs, TEMPORARY FILES, JUNKS FUNCTIONS
    #




    #
    # DISABLE ANTIVIRUS
    #

    @deco
    def disable_antivirus(self):
        results = self.op.antivirus_disabler()
        Disabled_log = ""
        Error_log = ""
        Cmd_log = ""
        
        for result in results:
            print(result[-1])
            if result[-1] is 0:
                Cmd_log += f"SUCCESS: {result[0]}" + "\n"
                continue
            elif result[-1] is 1:
                Cmd_log += f"FAILED: {result[0]}" + "\n"
                continue

            if result[-1]:
                Disabled_log += result[0] + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Disabled Antivirus Registry(s)\n" + self.equal_signs + Disabled_log + self.equal_signs + 
                     "Antivirus Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Command(s) Executed\n" + Cmd_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    @deco
    def check_windows_settings(self):
        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False) / (Complete Registry Path, False)
        results = self.op.windows_settings_checker() 
        Tweaked_log = ""
        Error_log = ""
        Untweak_log = ""
        
        for result in results:
            if result[-1]:
                Tweaked_log += f"{result[0]} - {result[1]} : {result[2]}" + "\n"
            elif not result[-1] and len(result) != 2:
                Untweak_log += f"{result[0]} : {result[1]} =/= {result[2]}" + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Tweaked Windows Settings Registry(s)\n" + self.equal_signs + Tweaked_log + self.equal_signs + 
                     "Windows Settings Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Untweak Windows Settings Registry(s)\n" + self.equal_signs + Untweak_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)

    

if __name__ == "__main__":
    app = Tk()
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()
