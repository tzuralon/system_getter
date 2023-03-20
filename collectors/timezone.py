from abc import ABC

import time

from collectors.base import Collector


class Timezone(Collector, ABC):
    def collect(self) -> str:
        """
        Collector which collects Timezone
        If there are 2 timezones (one for DST and for non-DST, it will take the relevant one according to daylight conf
        :return: Timezone string ('IST', 'IDT')
        """
        return time.tzname[time.daylight]

    def header(self) -> str:
        return 'Timezone'
