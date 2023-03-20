from abc import ABC

import wmi
import re

from collectors.base import Collector, get_wmi_value

chassis_types_dict = dict({1: 'Other',
                           2: 'Unknown',
                           3: 'Desktop',
                           4: 'Low Profile Desktop',
                           5: 'Pizza Box',
                           6: 'Mini Tower',
                           7: 'Tower',
                           8: 'Portable',
                           9: 'Laptop',
                           10: 'Notebook',
                           11: 'Hand Held',
                           12: 'Docking Station',
                           13: 'All in One',
                           14: 'Sub Notebook',
                           15: 'Space-Saving',
                           16: 'Lunch Box',
                           17: 'Main System Chassis',
                           18: 'Expansion Chassis',
                           19: 'SubChassis',
                           20: 'Bus Expansion Chassis',
                           21: 'Peripheral Chassis',
                           22: 'Storage Chassis',
                           23: 'Rack Mount Chassis',
                           24: 'Sealed-Case PC',
                           30: 'Tablet',
                           31: 'Convertible',
                           32: 'Detachable'})


class LaptopOrDesktop(Collector, ABC):
    def collect(self) -> str:
        """
        Collector which collects Laptop / Desktop
        :return: 'Laptop / Desktop / Unknown'
        """

        """
        Return is in format:
        instance of Win32_SystemEnclosure
        {
            ChassisTypes = {10};
            Tag = "System Enclosure 0";
        };
        """
        chassis_types = get_wmi_value("SELECT ChassisTypes FROM Win32_SystemEnclosure", r"ChassisTypes = {(\d+)}")
        for chassis_type in chassis_types:
            if 0 == len(chassis_type):  # If none returned - return Unknown type
                return 'Unknown'
            chassis_type_int = int(chassis_type[0])  # Assume we have a single instance
            if 1 <= chassis_type_int <= 2:
                return 'Unknown'
            elif 3 <= chassis_type_int <= 7:
                return 'Desktop'
            elif 8 <= chassis_type_int:
                return 'Laptop'
            return 'Unknown'

    def header(self) -> str:
        return 'Laptop or Desktop'