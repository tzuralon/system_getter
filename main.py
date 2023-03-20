import time
from pathlib import Path

import json
import win32con
import win32api

import requests

from collectors.laptop_or_desktop import LaptopOrDesktop
from collectors.os_version import OsVersion
from collectors.processes import Processes
from collectors.timezone import Timezone
from collectors.uac_enabled import UacEnabled
from collectors.windows_product_id import WindowsProductId


class Main:
    def __init__(self):
        # The collectors list is implemented here
        self.collectors = list([LaptopOrDesktop(),
                                Processes(),
                                Timezone(),
                                UacEnabled(),
                                OsVersion(),
                                WindowsProductId()])
        self.collectables = dict()

        self.output_file_path = Path(r"C:\windows\temp\telem.txt")
        self.url_to_broadcast = "https://localhost:8080"

    def collect_all_collectables(self):
        """
        This method will run all of the collectors in series

        :return: 0 on success
        """
        for collector in self.collectors:
            self.collectables[collector.header()] = collector.collect()

        return 0

    def save_output_to_file(self):
        """
        Manages the telemetry file save

        :return: None
        """
        # Create parent dir if neccessary
        if not self.output_file_path.parent.exists():
            self.output_file_path.parent.mkdir(parents=True)

        # Hidden file cannot be rewritten, let's unhide it
        if self.output_file_path.exists():
            win32api.SetFileAttributes(str(self.output_file_path), win32con.FILE_ATTRIBUTE_NORMAL)

        # Dump the file as json
        self.output_file_path.write_text(json.dumps(self.collectables))

        # Hide the file
        win32api.SetFileAttributes(str(self.output_file_path), win32con.FILE_ATTRIBUTE_HIDDEN)

        return 0

    def broadcast_to_url(self):
        """
        Tries to post the json into the url
        :return: 0 on success, 1 on failure
        """
        try:
            requests.post(self.url_to_broadcast, json=json.dumps(self.collectables))
            return 0
        except requests.exceptions.ConnectionError:
            return 1


if __name__ == '__main__':
    main = Main()

    main.collect_all_collectables()
    main.save_output_to_file()
    while 0 != main.broadcast_to_url():
        print(f"Failed to connect to {main.url_to_broadcast}, sleeping for 30sec")
        time.sleep(30)
