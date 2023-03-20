import re
import winreg

import wmi


def get_registry_value(header_key: winreg.HKEYType, registry_path: str, name: str) -> str:
    """
    Gets a value from registry by provided parameters

    :param header_key: HKEY enum
    :param registry_path: Registry path, such as Control Panel\Mouse
    :param name: Name of the value
    :return: value data
    """
    try:
        print(registry_path)
        registry_key = winreg.OpenKey(header_key, registry_path, 0,
                                      winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


def get_wmi_value(wmi_query: str, regex: str) -> str:
    """
    Gets a value from wmi by provided query, then match on regex

    :param wmi_query: the WMI query string
    :param regex: a pattern on which to match return value
    :return: value data
    """
    output = list()
    c = wmi.WMI()
    for inspected_value in c.query(wmi_query):
        output.append(re.findall(regex, str(inspected_value)))

    return output


class Collector:
    def collect(self):
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def header(self) -> str:
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def __repr__(self):
        return f"Collector[{self.header()}]"
