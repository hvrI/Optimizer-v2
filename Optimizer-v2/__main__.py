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

        # SYSTEM MENU
        self.menu = Menu(self.app)
        self.system_menu(self.menu)
        self.app.config(menu=self.menu)

        # LOG TEXTBOX
        self.log_textBox = Text(self, state='disabled', height=23, width=273)
        self.vsb = Scrollbar(self, orient="vertical", command=self.log_textBox.yview)
        self.log_textBox.configure(yscrollcommand=self.vsb.set)
        self.log_textBox.place(x=30, y=10)
        self.vsb.pack(side="right", fill="y")

        # Services
        self.button_services_checker = Button(self, text="Services Checker", height=2, width=20, command=self.check_service)
        self.button_services_checker.place(x=30, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Services", height=2, width=20, command=self.untweak_service_handler)
        self.button_untweak_service_handler.place(x=30, y=455)
        self.button_tweak_all_services = Button(self, text="All Services", height=2, width=20, command=self.tweak_all_services)
        self.button_tweak_all_services.place(x=30, y=510)
        # Windows Settings
        self.button_tweak_all_services = Button(self, text="Windows Settings Checker", height=2, width=20, command=self.check_windows_settings)
        self.button_tweak_all_services.place(x=200, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Windows Settings", height=2, width=20, command=self.untweak_windows_settings_handler)
        self.button_untweak_service_handler.place(x=200, y=455)
        self.button_tweak_all_services = Button(self, text="All Windows Settings", height=2, width=20, command=self.tweak_all_windows_settings)
        self.button_tweak_all_services.place(x=200, y=510)
        # Antivirus
        self.button_tweak_all_services = Button(self, text="Antivirus Checker", height=2, width=20, command=self.check_antivirus)
        self.button_tweak_all_services.place(x=370, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Antivirus", height=2, width=20, command=self.untweak_antivirus_handler)
        self.button_untweak_service_handler.place(x=370, y=455)
        self.button_tweak_all_services = Button(self, text="Disable Antivirus", height=2, width=20, command=self.disable_antivirus)
        self.button_tweak_all_services.place(x=370, y=510)
        # Network
        self.button_tweak_all_services = Button(self, text="Network Checker", height=2, width=20, command=self.check_network)
        self.button_tweak_all_services.place(x=540, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Network", height=2, width=20, command=self.untweak_network_handler)
        self.button_untweak_service_handler.place(x=540, y=455)
        self.button_tweak_all_services = Button(self, text="All Network", height=2, width=20, command=self.tweak_all_network)
        self.button_tweak_all_services.place(x=540, y=510)
        # Performance
        self.button_tweak_all_services = Button(self, text="Performance Checker", height=2, width=20, command=self.check_performance)
        self.button_tweak_all_services.place(x=710, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Performance", height=2, width=20, command=self.untweak_performance_handler)
        self.button_untweak_service_handler.place(x=710, y=455)
        self.button_tweak_all_services = Button(self, text="All Performance", height=2, width=20, command=self.tweak_all_performance)
        self.button_tweak_all_services.place(x=710, y=510)
        # Debloat
        self.button_tweak_all_services = Button(self, text="Bloat Checker", height=2, width=20, command=self.check_debloat)
        self.button_tweak_all_services.place(x=880, y=400)
        self.button_untweak_service_handler = Button(self, text="Update Bloatware", height=2, width=20, command=self.untweak_debloat_handler)
        self.button_untweak_service_handler.place(x=880, y=455)
        self.button_tweak_all_services = Button(self, text="All Debloat", height=2, width=20, command=self.tweak_all_debloat)
        self.button_tweak_all_services.place(x=880, y=510)


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
    #   MENU
    #

    def system_menu(self, menu: Menu):
        # Menus
        system_menu = Menu(menu, tearoff=0)
        path_not_found_menu = Menu(menu, tearoff=0)

        # Add System Menu to Bar (System Menu -> Main Menu Bar)
        menu.add_cascade(label="System", menu=system_menu)
        menu.add_separator()

        # Add Path_Not_Found_Menu to System Menu (path_not_found_menu -> System Menu)
        system_menu.add_cascade(label="Path Not Found", menu=path_not_found_menu)

        # path_not_found_menu commands                                                                                          
        path_not_found_menu.add_command(label="Services", command=self.services_path_not_found)
        path_not_found_menu.add_command(label="Antivirus", command=self.antivirus_path_not_found)
        path_not_found_menu.add_command(label="Windows Settings", command=self.windows_settings_path_not_found)

        # clear_log command
        menu.add_command(label="Clear", command=self.clear_logs)

        return
    
    #
    #   MENU FUNCTION
    #

    @deco
    def services_path_not_found(self):
        for path in self.op.path_not_found_services:
            self.log_textBox.insert("end", path + "\n")
    
    @deco
    def antivirus_path_not_found(self):
        for path in self.op.path_not_found_antivirus:
            self.log_textBox.insert("end", path + "\n")

    @deco
    def windows_settings_path_not_found(self):
        for path in self.op.path_not_found_windows_settings:
            self.log_textBox.insert("end", path + "\n")

    @deco
    def clear_logs(self):
        return self.log_textBox.delete("1.0", END)

    
    #
    #   SERVICES FUNCTIONS
    #   CHECKER | HANDLER | TWEAKER
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
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "services")
            if result[-1]:
                final_log += f"{keyName}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
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
    #   CLEAR LOG FILEs, TEMPORARY FILES, JUNKS FUNCTIONS
    #




    #
    #   DISABLE ANTIVIRUS
    #

    @deco
    def check_antivirus(self):
        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False) / (Complete Registry Path, False)
        results = self.op.antivirus_checker() 
        Disabled_log = ""
        Error_log = ""
        Enable_log = ""
        
        for result in results:
            if result[-1]:
                Disabled_log += f"{result[0]} - {result[1]} : {result[2]}" + "\n"
            elif not result[-1] and len(result) != 2:
                Enable_log += f"{result[0]} : {result[1]} =/= {result[2]}" + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Antivirus Disabled Registry(s)\n" + self.equal_signs + Disabled_log + self.equal_signs + 
                     "Antivirus Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Antivirus Enabled Registry(s)\n" + self.equal_signs + Enable_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    @deco
    def untweak_antivirus_handler(self):
        results = self.op.latest_untweak_antivirus
        final_log = "Updating Antivirus Registry(s)\n" + self.equal_signs

        if not results:
            return self.log_textBox.insert("end", "Unable to locate any enabled antivirus registry(s).\n")
        
        for result in results:
            original_value = result[-1]
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "antivirus")
            if result[-1]:
                final_log += f"{result[0]} - {result[1]}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                final_log += f"ERROR: {result[0]}\n"
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()

    @deco
    def disable_antivirus(self):
        results = self.op.antivirus_disabler()
        Disabled_log = ""
        Error_log = ""
        Cmd_log = ""
        
        for result in results:
            if result[-1] not in [True, False]:
                Cmd_log += f"{result[-1]}: {result[0]}" + "\n"
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
    
    #
    #   WINDOWS SETTINGS (PRIVACY & QOL & TELEMENTRY CMD)
    #   CHECKER | HANDLER | TWEAKER
    #
    
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
    
    @deco
    def untweak_windows_settings_handler(self):
        results = self.op.latest_untweak_windows_settings
        final_log = "Updating Untweaked Windows Settings Registry(s)\n" + self.equal_signs

        if not results:
            return self.log_textBox.insert("end", "Unable to locate any untweak windows settings registry(s).\n")
        
        for result in results:
            original_value = result[-1]
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "windows_settings")
            if result[-1]:
                final_log += f"{result[0]} - {result[1]}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                final_log += f"ERROR: {result[0]}\n"
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()
    
    @deco
    def tweak_all_windows_settings(self):
        results = self.op.all_windows_settings_tweak()
        Tweak_log = ""
        Error_log = ""
        Cmd_log = ""
        
        for result in results:
            if result[-1] not in [True, False]:
                Cmd_log += f"{result[-1]}: {result[0]}" + "\n"
                continue

            if result[-1]:
                Tweak_log += result[0] + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Tweak Windows Settings Registry(s)\n" + self.equal_signs + Tweak_log + self.equal_signs + 
                     "Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Command(s) Executed\n" + Cmd_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    #
    #   NETWORK
    #   CHECKER | HANDLER | TWEAKER
    #

    @deco
    def check_network(self):
        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False) / (Complete Registry Path, False)
        results = self.op.network_checker()
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


        final_log = ("Tweaked Network Registry(s)\n" + self.equal_signs + Tweaked_log + self.equal_signs + 
                     "Network Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Untweak Network Registry(s)\n" + self.equal_signs + Untweak_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    

    @deco
    def untweak_network_handler(self):
        results = self.op.latest_untweak_network
        final_log = "Updating Untweaked Network Registry(s)\n" + self.equal_signs

        if not results:
            return self.log_textBox.insert("end", "Unable to locate any untweak network registry(s).\n")
        
        for result in results:
            original_value = result[-1]
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "network")
            if result[-1]:
                final_log += f"{result[0]} - {result[1]}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                final_log += f"ERROR: {result[0]}\n"
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()
        
    @deco
    def tweak_all_network(self):
        results = self.op.all_network_tweak()
        Tweak_log = ""
        Error_log = ""
        
        for result in results:
            if result[-1]:
                Tweak_log += result[0] + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Tweak Network Registry(s)\n" + self.equal_signs + Tweak_log + self.equal_signs + 
                     "Network Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    #
    # PERFORMANCE
    # CHECKER | HANDLER | TWEAKER
    # 

    @deco
    def check_performance(self):
        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False) / (Complete Registry Path, False)
        results = self.op.performance_checker() 
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


        final_log = ("Tweaked Performance Registry(s)\n" + self.equal_signs + Tweaked_log + self.equal_signs + 
                     "Performance Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Untweak Performance Registry(s)\n" + self.equal_signs + Untweak_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    @deco
    def untweak_performance_handler(self):
        results = self.op.latest_untweak_performance
        final_log = "Updating Untweaked Performance Registry(s)\n" + self.equal_signs
        self.op.delete_registry(r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People\not new")
        if not results:
            return self.log_textBox.insert("end", "Unable to locate any untweak performance registry(s).\n")
        
        for result in results:
            original_value = result[-1]
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "performance")
            if result[-1]:
                final_log += f"{result[0]} - {result[1]}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                final_log += f"ERROR: {result[0]}\n"
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()
    
    @deco
    def tweak_all_performance(self):
        results = self.op.all_performance_tweak()
        Tweak_log = ""
        Error_log = ""
        Cmd_log = ""
        
        for result in results:
            if result[-1] not in [True, False]:
                Cmd_log += f"{result[-1]}: {result[0]}" + "\n"
                continue

            if result[-1]:
                Tweak_log += result[0] + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Tweak performance Registry(s)\n" + self.equal_signs + Tweak_log + self.equal_signs + 
                     "Performance Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Command(s) Executed\n" + Cmd_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    
    #
    #   DEBLOAT
    #   CHECKER | HANDLER | TWEAKER
    #
    
    @deco
    def check_debloat(self):
        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False) / (Complete Registry Path, False)
        results = self.op.debloat_checker()
        Debloated_log = ""
        Error_log = ""
        Bloat_log = ""
        Bloatkey_log = ""
        
        for result in results:
            if result[-1]:
                if result[1] == "BLOATKEY":
                    Bloatkey_log += f"{result[0]}" + "\n"
                    continue
                Debloated_log += f"{result[0]} - {result[1]} : {result[2]}" + "\n"
            elif not result[-1] and len(result) != 2:
                if result[1] == "BLOATKEY":
                    Bloatkey_log += f"{result[0]}" + "\n"
                    continue
                Bloat_log += f"{result[0]} : {result[1]} =/= {result[2]}" + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Debloated Registry(s)\n" + self.equal_signs + Debloated_log + self.equal_signs + 
                     "Bloat Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs + "Bloated Registry(s)\n" + self.equal_signs + Bloat_log + self.equal_signs +
                    "Bloat Keys Registry(s)\n" + self.equal_signs + Bloatkey_log + self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    

    @deco
    def untweak_debloat_handler(self):
        results = self.op.latest_untweak_debloat
        final_log = "Updating Bloat Registry(s)\n" + self.equal_signs

        if not results:
            return self.log_textBox.insert("end", "Unable to locate any bloat registry(s).\n")
        
        for result in results:
            original_value = result[-1]
            # (Complete Registry Path, Key Name, Key Value, True) or (Complete Registry Path, False)
            result = self.op.add_change_registry(result[0], result[1], "debloat")
            if result[-1]:
                final_log += f"{result[0]} - {result[1]}: {original_value} => {result[2]}\n" # (path, ('Start', 'Reg_DWORD', '3'), '2')
            else:
                final_log += f"ERROR: {result[0]}\n"
        else:
            self.op.log.finished_tweaks()
            self.log_textBox.insert("end", final_log + self.equal_signs)
            return results.clear()
        
    @deco
    def tweak_all_debloat(self):
        results = self.op.all_debloat_tweak()
        Tweak_log = ""
        Error_log = ""
        
        for result in results:
            if result[-1]:
                Tweak_log += result[0] + "\n"
            else:
                Error_log += result[0] + "\n"


        final_log = ("Debloated or Deleted Registry(s)\n" + self.equal_signs + Tweak_log + self.equal_signs + 
                     "Bloat Registry Path(s) Not Found or Inaccessible\n" + self.equal_signs + Error_log + 
                    self.equal_signs)
        self.op.log.finished_tweaks()
        return self.log_textBox.insert("end", final_log)
    

if __name__ == "__main__":
    app = Tk()
    frame = GUI(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()
