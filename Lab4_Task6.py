import os

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            print path
        else:
            walk(path)

def walks(dir):
    for root, dirs, files in os.walk(dirn):
        for filename in files:
            print os.path.join(root, filename)

    walks(".")
