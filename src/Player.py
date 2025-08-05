class Player:
    def __init__(self):
        self.table = [[0 for _ in range(3)] for _ in range (3)]
        self.links = [] 
        self.total_points = 0


    def place(self, number, col):
        if col > 2 or col < 0:
            raise Exception("You only have 3 rows!")
        for i in range(2, -1, -1):
            if not(self.table[i][col]):
                self.table[i][col] = number
                list(map(lambda p: p.update(number, col), self.links))
                return
        raise Exception("Column is full")

    def link(self, another):
        self.links.append(another)
        another.links.append(self)
    

    def update(self, number, col):
        for i in range(2, -1, -1):
            if self.table[i][col] == number:
                self.table[i][col] = 0
        self.rearrange(col)

    def rearrange(self, col):
        for i in range(2, 0, -1):
            if not(self.table[i][col]):
                check = i - 1
                while check >= 0 and not(self.table[check][col]):
                    check -= 1
                if check >= 0:
                    self.table[i][col], self.table[check][col] = self.table[check][col], self.table[i][col]

    def __str__(self):
        str = ""
        for row in range(3):
            str += f"{self.table[row]}    "
            for link in self.links:
                str += f"{link.table[row]}    "
            str += '\n'
        return str
