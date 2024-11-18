import os
import shutil
import winreg
import contextlib
import subprocess

from optimise.script.services import *
from optimise.script.AntiVirus import *
from optimise.script.logging import *
from optimise.script.windows_settings import *
from optimise.script.debloat import *

REGISTRY_HKEY = {
    "HKLM" : winreg.HKEY_LOCAL_MACHINE,
    "HKCU" : winreg.HKEY_CURRENT_USER,
    "HKCR" : winreg.HKEY_CLASSES_ROOT,
    "HKU" : winreg.HKEY_USERS,
}

REGISTRY_DATATYPE = {
    "Reg_DWORD" : winreg.REG_DWORD,
    "Reg_SZ" : winreg.REG_SZ,
    "Reg_NONE" : winreg.REG_NONE,
    "Reg_MULTI_SZ": winreg.REG_MULTI_SZ,
    "Reg_BINARY" : winreg.REG_BINARY,
}

REGISTRY_DATATYPE_REPRESENTATION = {
    "Reg_NONE" : 0,
    "Reg_SZ" : 1,
    "Reg_EXPAND_SZ" : 2,
    "Reg_BINARY" : 3,
    "Reg_DWORD" : 4,
    "Reg_MULTI_SZ": 7,
    "Reg_QWORD" : 11,
}

class Name():

    def __init__(self):

        # LOGGING MODULE STARTUP
        self.log = Log()
        
        # SERVICES
        self.latest_untweak_services = []
        self.path_not_found_services = []

        # ANTIVIRUS
        self.path_not_found_antivirus = []

        # WINDOWS SETTINGS
        self.latest_untweak_windows_settings = []
        self.path_not_found_windows_settings = []        


    def name_of_registry_key(self, path: str):
        """
        Return Registry Path's KeyName
        ETC:
        HKLM\\SOFTWARE\\Policies\\Microsoft\\Edge
        = Edge
        """
        return path.split('\\')[-1]

    #
    # REGISTRY FUNCTION
    #

    def add_change_registry(self, path: str, values: tuple, path_not_found: list=[]):
        """
        Only Add/Change one at a time, unsupported for multiple keys per path
        ETC:
        path HKLM\\SYSTEM\\CurrentControlSet\\Services\\IKEEXT
        value ("Start", "Reg_DWORD", "3")
        RETURN (Complete Registry Path, Key Name, Key Value, True/False)
        """
        with winreg.ConnectRegistry(None, REGISTRY_HKEY.get(path.split("\\")[0])) as hkey:
            try:
                with winreg.OpenKey(hkey, path[path.index("\\")+1:], 0, winreg.KEY_ALL_ACCESS) as rkey:
                    value_name, value_type, value = values
                    if value_type not in ["Reg_SZ", "Reg_MULTI_SZ"] and value.isnumeric:
                        winreg.SetValueEx(rkey, value_name, 0, REGISTRY_DATATYPE.get(value_type), int(value))
                    else:
                        winreg.SetValueEx(rkey, value_name, 0, REGISTRY_DATATYPE.get(value_type), value)

                    # Check if any changes made
                    for i in range(winreg.QueryInfoKey(rkey)[1]):
                        if value_name in winreg.EnumValue(rkey, i) and REGISTRY_DATATYPE_REPRESENTATION.get(value_type) == winreg.EnumValue(rkey, i)[2]:
                            # winreg.EnumValue(rkey, i) return ('MenuShowDelay', '200', 1)
                            if str(winreg.EnumValue(rkey, i)[1]) == value:
                                self.log.registry_key_changed(f"Path: \"{path}\" - \"{value_name}\" - Value changed to \"{winreg.EnumValue(rkey, i)[1]}\"")
                                return (path, value_name, value, True)
                            else:
                                # Log Registry Key Not Changed
                                self.log.registry_key_not_changed(f"Path: \"{path}\" - \"{value_name}\" - Current Value: \"{winreg.EnumValue(rkey, i)[1]}\" | Changing Value: \"{value}\"")
                                return (path, value_name, value, False)
                    else:
                        self.log.registry_key_not_found(path, value)
                        return (path, False)
            
            except (FileNotFoundError):
                self.log.registry_path_not_found(f"Path Not Found: \"{path}\"")
                path_not_found.append(path)
                return (path, False)
            except (OSError, PermissionError, Exception) as Error:
                self.log.unexpected_error(Error)
                return (path, False)
            
    def create_registry_subkey(self, path: str):
        """
        Create Registry Subkey Path
        ETC:
        path HKLM\\SYSTEM\\CurrentControlSet\\Services\\IKEEXT
        RETURN True/False
        """
        with winreg.ConnectRegistry(None, REGISTRY_HKEY.get(path.split("\\")[0])) as hkey:
            try:
                winreg.CreateKeyEx(hkey, path[path.index("\\")+1:], 0, winreg.KEY_ALL_ACCESS)
            except (OSError, Exception) as Error:
                self.log.unexpected_error(Error)
                return False
            else:
                return True

    
    #
    # SERVICES OPTIMIZATION
    # CHECKER | TWEAKER
    #

    def service_checker(self):
        """
        Check any changes made to services.
        Could be changed by Windows Update etc.
        Wouldn't make any changes instantly, just to give a view on what services changed.
        """
        self.latest_untweak_services = []
        self.path_not_found_services = []

        for path, values in serviceReg.items():
            keyName = self.name_of_registry_key(path)
            with winreg.ConnectRegistry(None, REGISTRY_HKEY.get(path.split("\\")[0])) as hkey:
                try:
                    with winreg.OpenKey(hkey, path[path.index("\\")+1:], 0, winreg.KEY_ALL_ACCESS) as rkey:
                        # Looping through all the registry keys in the subkey
                        for i in range(winreg.QueryInfoKey(rkey)[1]):
                            if "Start" in winreg.EnumValue(rkey, i):
                                original_value = str(winreg.EnumValue(rkey, i)[1])
                                tweaked_value = values[0][2]
                                if original_value != tweaked_value:
                                    self.latest_untweak_services.append((path, values[0], original_value)) # (path, ('Start', 'Reg_DWORD', '3'), '2')
                                    yield (keyName, original_value, tweaked_value)
                                    break
                                else:
                                    yield (keyName, 0)
                                    break
                except (FileNotFoundError):
                    self.log.registry_path_not_found(f"Path Not Found: \"{path}\"")
                    self.path_not_found_services.append(path)
                    yield (keyName, 1)
                except (OSError, PermissionError, Exception) as Error:
                    self.log.unexpected_error(Error)
                    yield (keyName, 1)
        else:
            self.log.added_latest_untweaks(self.latest_untweak_services)
            return self.latest_untweak_services
        
            
    def all_services_tweak(self):
        """
        Tweak all services to either manual or disabled
        """
        self.path_not_found_services = []

        for path, values in serviceReg.items():
            for value_name, value_type, value in values:
                result = self.add_change_registry(path, (value_name, value_type, value), self.path_not_found_services) # (Complete Registry Path, Key Name, Key Value, True/False)
                yield (self.name_of_registry_key(path), result[-1])

    
    #
    # ANTIVIRUS DISABLER
    # DISABLER
    #

    def antivirus_disabler(self):
        """
        Disable All Windows Built-In Antivirus
        """
        self.path_not_found_antivirus = []

        for path, values in AntivirusReg.items():
            for value_name, value_type, value in values:
                result = self.add_change_registry(path, (value_name, value_type, value), self.path_not_found_antivirus) # (Complete Registry Path, Key Name, Key Value, True) / (Complete Registry Path, False)
                if result[-1]:
                    yield (f"{result[0]} - {result[1]}", result[-1])
                else:
                    yield (f"{result[0]}", result[-1])

        for cmd in AntivirusCMD:
            result = os.system(cmd + " >nul 2>&1")
            if result == 0:
                yield (cmd, "SUCCESS")
            else:
                yield (cmd, "FAILED")

    

    #
    # GENERAL WINDOWS OPTIMIZATION
    # CHECKER | TWEAKER
    #

    def windows_settings_checker(self):

        self.latest_untweak_windows_settings = []
        self.path_not_found_windows_settings = []

        for path, values in privacyQolReg.items():
            with winreg.ConnectRegistry(None, REGISTRY_HKEY.get(path.split("\\")[0])) as hkey:
                keyName = self.name_of_registry_key(path)
                try:
                    with winreg.OpenKey(hkey, path[path.index("\\")+1:], 0, winreg.KEY_ALL_ACCESS) as rkey:
                    # Looping through all the registry keys in the subkey
                        for value_name, value_type, value in values:
                            for i in range(winreg.QueryInfoKey(rkey)[1]):
                                retrieve_value = winreg.EnumValue(rkey, i) # (value_name, value_data, data_type)
                                if value_name == retrieve_value[0] and REGISTRY_DATATYPE_REPRESENTATION.get(value_type) == retrieve_value[2]:
                                    if value == str(retrieve_value[1]):
                                        # (Complete Registry Path, Value_Name, Value, True) / (Complete Registry Path - Value_Name, Current_Value, Value, False)
                                        yield (path, value_name, str(retrieve_value[1]), True)
                                        break
                                    else:
                                        # (path, ('Start', 'Reg_DWORD', '3'), '2')
                                        self.latest_untweak_windows_settings.append((path, (value_name, value_type, value), str(retrieve_value[1])))
                                        yield (f"{path} - {retrieve_value[0]}", str(retrieve_value[1]), value, False)
                                        break
                                
                except (FileNotFoundError):
                    self.log.registry_path_not_found(f"Path Not Found: \"{path}\"")
                    self.path_not_found_windows_settings.append(path)
                    yield (path, False)
                except (OSError, PermissionError, Exception) as Error:
                    self.log.unexpected_error(Error)
                    yield (path, False)
        else:
            self.log.added_latest_untweaks(self.latest_untweak_windows_settings)

        return
    
    def all_windows_settings_tweak(self):
        self.path_not_found_windows_settings = []
        
        for path, values in privacyQolReg.items():
            for value_name, value_type, value in values:
                result = self.add_change_registry(path, (value_name, value_type, value), self.path_not_found_windows_settings)
                # (Complete Registry Path, Key Name, Key Value, True) / (Complete Registry Path, False)
                if result[-1]:
                    yield (f"{result[0]} - {result[1]}", result[-1])
                else:
                    yield (f"{result[0]}", result[-1])

        for cmd in TelementryCMD:
            result = os.system(cmd + " >nul 2>&1")
            if result == 0:
                yield (cmd, "SUCCESS")
            else:
                yield (cmd, "FAILED")
