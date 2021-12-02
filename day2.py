
class Submarine:
    aim = 0
    depth = 0
    horizontal = 0

    @classmethod
    def load(cls):
        with open('day2.txt') as file:
            return file.readlines()

    @classmethod
    def compute(cls):
        for line in cls.load():
            split = line.split(" ")
            if "down" in line: cls.aim += int(split[1])
            elif "up" in line: cls.aim -= int(split[1])
            elif "forward" in line:
                cls.horizontal += int(split[1])
                cls.depth += cls.aim * int(split[1])

# def load(cls):
#     with open('day2.txt') as file:
#         return file.readlines()
        
# def findAim(cls):
#     aim = 0
#     for line in load():
#         split = line.split(" ")
#         if "down" in line: aim += int(split[1])
#         elif "up" in line: aim -= int(split[1])
#         elif "forward" in line: 
#     return aim

# def findDepth():
#     depth = 0
#     for line in load():
#         split = line.split(" ")
#         if "down" in line: depth += int(split[1])
#         elif "up" in line: depth -= int(split[1])
#     return depth

# def findHotizontal():
#     horizontal = 0
#     for line in load():
#         split = line.split(" ")
#         if "forward" in line: horizontal += int(split[1])
#     return horizontal

# depth = findDepth()
# horizontal = findHotizontal()
# print(depth * horizontal)

sub = Submarine()
sub.compute()
print(sub.horizontal * sub.depth)