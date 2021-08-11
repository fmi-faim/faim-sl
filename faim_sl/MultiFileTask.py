import sciluigi as sl
import luigi

from os.path import split, splitext, join

from tifffile import imread, imsave


class MultiFileTask(sl.Task):
    in_data = None

    target_dir = luigi.Parameter(description='Target directory.')
    suffix = luigi.Parameter(description='File suffix.')

    file_map = None

    def out_file(self):
        self.prepare_inputs()
        self.file_map = {}
        out_batch = {}
        for in_path in self.in_data().keys():
            _, name = split(in_path)
            filename, ext = splitext(name)
            out_path = join(self.target_dir, filename + '{}.tif'.format(self.suffix))
            out_batch[out_path] = sl.TargetInfo(self, path=out_path)
            self.file_map[in_path] = out_path

        return out_batch

    def run(self):
        self.prepare()
        save_fun = self.get_save_function()
        for path, target_info in self.in_data().items():
            # if not target_info.target.exists():
            img = imread(target_info.path)
            img = self.run_computation(img)
            target_file = self.file_map[path]
            save_fun(target_file, img)

    def prepare_inputs(self):
        pass

    def prepare(self):
        pass

    def get_save_function(self):
        return imsave

    def run_computation(self, img):
        return self.compute(img)

    @staticmethod
    def compute(self, img):
        return img
