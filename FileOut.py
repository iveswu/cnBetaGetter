# coding=utf8
__author__ = 'ives'

class FileOut(object):

    def __init__(self, stdout):
        self.buffer = []
        self.stdout = stdout
        self.file = open("log.txt", "a")

    def write(self, args):

        self.file.write(args)
        self.file.flush()
        self.stdout.write(args)
        self.stdout.flush()

