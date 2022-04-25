import os

class Monkey(object):
    def __init__(self, file):
        self._cached_stamp = 0
        self.filename = file
        self.run = False

    def look_monkey(self):
        try:
            stamp = os.stat(self.filename).st_mtime
            if stamp != self._cached_stamp:
                self._cached_stamp = stamp
                self.run = True
            else:
                self.run = False
        except:
            pass