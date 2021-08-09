import luigi

class BatchTargetInfo(luigi.Target):
    task = None
    batch = None

    def __init__(self, task, batch):
        self.task = task
        self.batch = batch

    def exists(self):
        exists = False
        for target in self.batch.values():
            exists = exists and target.exists()

        return exists
