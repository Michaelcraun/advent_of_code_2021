

class BingoBoard:
    marked = []
    rows = []

    def __init__(self, lines):
        currentRow = []
        rows = []
        for row in lines:
            splitRow = row.split(' ')
            for num in splitRow:
                if num != '': currentRow.append(int(num))
            if currentRow != []:
                rows.append(currentRow)
                currentRow = []
        self.rows = rows

    def checkIfWinner(self):
        # Check rows
        for row in self.rows:
            callCount = 0
            for num in row:
                if num in self.marked: callCount += 1
                if callCount == 5: return True

        # Check columns
        for index in range(len(self.rows[0])):
            column = []
            for row in self.rows: 
                callCount = 0
                column.append(row[index])

                for num in column:
                    if num in self.marked: callCount += 1
                    if callCount == 5: return True

        return False

    def mark(self, num):
        self.marked.append(num)
        return self.checkIfWinner()

    def score(self, multiplier):
        unmarked = []
        for row in self.rows:
            for num in row:
                if num not in self.marked:
                    unmarked.append(num)
        
        sum = 0
        for num in unmarked: sum += num
        return sum * multiplier

class Bingo:
    boards = []
    called = []

    def __init__(self):
        self.load()

    def load(self):
        with open ('day4.txt') as file:
            lines = file.readlines()
            currentBoard = None
            rows = []
            for index in range(len(lines)):
                if index == 0:
                    set = []
                    calledNumbers = lines[index].split(',')
                    for num in calledNumbers:
                        set.append(num)
                        if len(set) == 6:
                            self.called.append(set)
                            set = []
                elif lines[index] == '\n' and rows != []:
                    currentBoard = BingoBoard(rows)
                    self.boards.append(currentBoard)
                    currentBoard = None
                    rows = []
                elif lines[index] != '': 
                    rows.append(lines[index].replace('\n', ''))

    def playToWin(self):
        for set in self.called:
            for num in set:
                for board in self.boards:
                    isWinner = board.mark(int(num))
                    if isWinner:
                        return board.score(int(num))

game = Bingo()
print(game.playToWin())
# print(game.playToLose())