class Collector:
    def collect(self) -> str:
        raise NotImplementedError("Virtual method, please use an inheriting method")

    def header(self) -> str:
        raise NotImplementedError("Virtual method, please use an inheriting method")