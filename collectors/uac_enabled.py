from abc import ABC

import winreg

from collectors.base import Collector


class UacEnabled(Collector, ABC):
    def get_registry_value(self, header_key: winreg.HKEYType, registry_path: str, name: str) -> str:
        """

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

    def collect(self) -> bool:
        """
        Collector which collects either UAC is enabled on this host
        Using HKEY_LOCAL_MACHINE > Software > Microsoft > Windows > Current Version > Policies > System > EnableLUA == 1
        :return: True/False
        """
        return 1 == self.get_registry_value(winreg.HKEY_LOCAL_MACHINE,
                                              r"Software\Microsoft\Windows\CurrentVersion\Policies\System",
                                              "EnableLUA")

    def header(self) -> str:
        return 'Is UAC Enabled'
