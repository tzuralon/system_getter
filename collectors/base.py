import re
import winreg
from typing import List

import wmi


def get_registry_value(header_key: winreg.HKEYType, registry_path: str, name: str) -> str:
    """
    Gets a value from registry by provided parameters, if failed, return None

    :param header_key: HKEY enum
    :param registry_path: Registry path, such as Control Panel\Mouse
    :param name: Name of the value
    :return: value data
    """
    try:
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


def get_wmi_values(wmi_query: str, regexs: List[str]) -> List[str]:
    """
    Gets a value from wmi by provided query, then match on multiple regexs

    :param wmi_query: the WMI query string
    :param regexs: a list of pattern on which to match return value
    :return: value data list
    """
    output = list()
    c = wmi.WMI()
    for inspected_value in c.query(wmi_query):
        per_value_output = list()
        for regex in regexs:
            per_value_output.append(re.findall(regex, str(inspected_value)))
        output.append(per_value_output)

    return output


class Collector:
    """
    Base class for Collector
    """
    def collect(self):
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def header(self) -> str:
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def __repr__(self):
        return f"Collector[{self.header()}]"
