class Directory:
    def __init__(self, name, children, parent):
        self.name = name
        self.children = children
        self.parent = parent

    def mkdir(self, name):
        self.children.append(Directory(name, [], self))

    def addfile(self, name, size):
        self.children.append(File(name, int(size)))

    def child_by_name(self, name):
        for child in self.children:
            if isinstance(child, Directory) and child.name == name:
                return child

    def size(self):
        sum = 0
        for child in self.children:
            if isinstance(child, File):
                sum += child.size
            else:
                sum += child.size()
        return sum

    def print_recursive(self):
        print(self.name)
        for child in self.children:
            child.print_recursive()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print_recursive(self):
        print(self.name, self.size)


def main():
    answer1 = None
    answer2 = None

    file = open("./7.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    dir = Directory("/", [], None)

    for line in lines:
        if line == "$ cd /" or line == "$ ls":
            continue

        split = line.split()

        if split[0] == "$" and split[1] == "cd":
            if split[2] == "..":
                dir = dir.parent
            else:
                dir = dir.child_by_name(split[2])

        if line[0:3] == "dir":
            dir.mkdir(line[4:])

        if split[0][0:1].isdecimal():
            dir.addfile(split[1], split[0])

    while dir.parent is not None:
        dir = dir.parent

    # dir.print_recursive()

    dirs = []

    def find_dirs(dir):
        dirs.append(dir)
        for child in dir.children:
            if isinstance(child, Directory):
                find_dirs(child)

    find_dirs(dir)

    sum = 0

    for d in dirs:
        s = d.size()
        if s < 100000:
            sum += s

    will_delete = -1

    to_be_deleted_size = 30000000 - (70000000 - dir.size())

    for d in dirs:
        s = d.size()
        if s > to_be_deleted_size:
            if will_delete == -1 or s < will_delete:
                will_delete = s

    answer1 = sum
    answer2 = will_delete

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
