class Collector:
    def collect(self):
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def header(self) -> str:
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def __repr__(self):
        return f"Collector[{self.header()}]"