from collectors.laptop_or_desktop import LaptopOrDesktop


class Main:
    def __init__(self):
        self.collectors = list([LaptopOrDesktop()])
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
