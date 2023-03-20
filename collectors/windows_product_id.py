from abc import ABC

from collectors.base import Collector, get_wmi_value


class WindowsProductId(Collector, ABC):
    def collect(self) -> str:
        """
        Collector which collects Windows Product ID
        :return: Windows product ID
        """
        output = get_wmi_value("SELECT OA3xOriginalProductKey FROM softwareLicensingService",
                             r'OA3xOriginalProductKey = "(.*)"')
        if 0 < len(output) and 0 < len(output[0]):
            return output[0][0]

        return "Unknown"

    def header(self) -> str:
        return 'Windows Product ID'
