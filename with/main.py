import os
os.chdir("with")

# one way to work with files
f = open('sample.txt', 'w')
f.write("Lorem ipsum dolor sit amet consectetur adipiscing elit.")
f.close()

# recommended method is using a context manager (basically, a with statement)
# it automatically closes file (or database) connection
# open and release locks...
with open('sample.txt', 'w') as f:
    f.write("Lorem ipsum dolor sit amet consectetur adipiscing elit.")


# setting our own context manager just to see whats happening
class Open_File():
    def __init__(self, filename: str, mode: str):
        self.filename: str = filename
        self.mode: str = mode

    # setup method
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file # returns the object we're working with

    # teardown method
    def __exit__(self, exc_type, exc_val, traceback): # extra parameters are for when an exception is thrown
        self.file.close()

with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

print(f.closed)
