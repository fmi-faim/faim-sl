import luigi


class IntListParameter(luigi.Parameter):
    def parse(self, arguments):
        return [int(s) for s in arguments.split(' ')]


class SliceParameter(luigi.Parameter):
    def parse(self, arguments):
        return slice(*[int(s) for s in arguments.split(':')])

