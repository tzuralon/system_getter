from abc import ABC

import platform

from collectors.base import Collector


class OsVersion(Collector, ABC):
    def collect(self) -> str:
        """
        Collector which collects OS Version
        :return: OS Version
        """
        return platform.platform()

    def header(self) -> str:
        return 'OS Version'
