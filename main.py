from collectors.laptop_or_desktop import LaptopOrDesktop
from collectors.timezone import Timezone
from collectors.uac_enabled import UacEnabled


class Main:
    def __init__(self):
        self.collectors = list([LaptopOrDesktop(),
                                Timezone(),
                                UacEnabled()])
        self.collectables = dict()

    def collect_all_collectables(self):
        for collector in self.collectors:
            self.collectables[collector.header()] = collector.collect()

    def debug(self):
        print(self.collectors)
        print(self.collectables)


if __name__ == '__main__':
    main = Main()

    main.collect_all_collectables()
    main.debug()
