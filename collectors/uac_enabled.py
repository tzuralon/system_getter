from abc import ABC

import winreg

from collectors.base import Collector, get_registry_value


class UacEnabled(Collector, ABC):
    def collect(self) -> bool:
        """
        Collector which collects either UAC is enabled on this host
        Using HKEY_LOCAL_MACHINE > Software > Microsoft > Windows > Current Version > Policies > System > EnableLUA == 1
        :return: True/False
        """
        return 1 == get_registry_value(winreg.HKEY_LOCAL_MACHINE,
                                              r"Software\Microsoft\Windows\CurrentVersion\Policies\System",
                                              "EnableLUA")

    def header(self) -> str:
        return 'Is UAC Enabled'
