import os

class ChangeDir:
    def __init__(self, dir):
        self.file = dir

    def __enter__(self):
        os.chdir(self.file)

    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir('../')

with ChangeDir('dir1'):
    print(os.listdir())

