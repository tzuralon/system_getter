from pathlib import Path

import json
import win32con, win32api

from collectors.laptop_or_desktop import LaptopOrDesktop
from collectors.timezone import Timezone
from collectors.uac_enabled import UacEnabled


class Main:
    def __init__(self):
        self.collectors = list([LaptopOrDesktop(),
                                Timezone(),
                                UacEnabled()])
        self.collectables = dict()

        self.output_file_path = Path(r"C:\windows\temp\telem.txt")

    def collect_all_collectables(self):
        for collector in self.collectors:
            self.collectables[collector.header()] = collector.collect()

    def save_output_to_file(self):
        """
        Manages the telemetry save

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

        #Hide the file
        win32api.SetFileAttributes(str(self.output_file_path), win32con.FILE_ATTRIBUTE_HIDDEN)

    def debug(self):
        print(self.collectors)
        print(self.collectables)


if __name__ == '__main__':
    main = Main()

    main.collect_all_collectables()
    main.save_output_to_file()
    main.debug()
