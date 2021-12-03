class Power:
    @classmethod 
    def load(cls):
        with open('day3.txt') as file:
            return file.readlines()

    @classmethod
    def gammaRate(cls):
        lines = cls.load()
        example = lines[0]
        
        gammaBinary = ''
        for index in range(len(example) - 1): gammaBinary += cls.mostCommonBitAtPosition(index, lines)
        return cls.binaryToDecimal(gammaBinary)

    @classmethod
    def epsilonRate(cls):
        lines = cls.load()
        example = lines[0]
        
        epsilonBinary = ''
        for index in range(len(example) - 1): epsilonBinary += cls.leastCommonBitAtPosition(index, lines)
        return cls.binaryToDecimal(epsilonBinary)

    @classmethod
    def co2ScrubberRating(cls):
        lines = cls.load()
        example = lines[0]

        for index in range(len(example) - 1):
            leastCommon = cls.leastCommonBitAtPosition(index, lines)
            leastCommonLines = filter(lambda line: line[index] == leastCommon, lines)
            mostCommonLines = filter(lambda line: line[index] != leastCommon, lines)
            if len(leastCommonLines) == len(mostCommonLines): lines = filter(lambda line: line[index] == '0', lines)
            else: lines = leastCommonLines
            if len(lines) == 1: return cls.binaryToDecimal(lines[0])

    @classmethod
    def oxygenGeneratorRating(cls):
        lines = cls.load()
        example = lines[0]

        for index in range(len(example) - 1):
            leastCommon = cls.leastCommonBitAtPosition(index, lines)
            leastCommonLines = filter(lambda line: line[index] == leastCommon, lines)
            mostCommonLines = filter(lambda line: line[index] != leastCommon, lines)
            if len(leastCommonLines) == len(mostCommonLines): lines = filter(lambda line: line[index] == '1', lines)
            else: lines = mostCommonLines
            if len(lines) == 1: return cls.binaryToDecimal(lines[0])

    @classmethod 
    def leastCommonBitAtPosition(cls, index, lines):
        chars = map(lambda x: x[index], lines)
        zeros = filter(lambda x: x == '0', chars)
        ones = filter(lambda x: x == '1', chars)
        return '0' if len(zeros) < len(ones) else '1'

    @classmethod
    def mostCommonBitAtPosition(cls, index, lines):
        chars = map(lambda x: x[index], lines)
        zeros = filter(lambda x: x == '0', chars)
        ones = filter(lambda x: x == '1', chars)
        return '0' if len(zeros) > len(ones) else '1'

    @classmethod
    def binaryToDecimal(cls, binary):
        return int(binary,2)

print('Power consumption is {}'.format(Power.gammaRate() * Power.epsilonRate()))
print('Life support rating is {}'.format(Power.oxygenGeneratorRating() * Power.co2ScrubberRating()))