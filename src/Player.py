class Player:
    def __init__(self, name):
        self.name = name
        self.table = [[0 for _ in range(3)] for _ in range (3)]
        self.links = [] 
        self.total_points = 0


    def place(self, number, col):
        if col > 2 or col < 0:
            raise Exception("You only have 3 rows!")
        for i in range(2, -1, -1):
            if not(self.table[i][col]):
                self.table[i][col] = number
                self.update_points()
                list(map(lambda p: p.update(number, col), self.links))
                return
        raise Exception(f"Column {col + 1} is full")

    def link(self, another):
        self.links.append(another)
        another.links.append(self)
    

    def update(self, number, col):
        for row in range(2, -1, -1):
            if self.table[row][col] == number:
                self.table[row][col] = 0
        self.update_points()
        self.rearrange(col)

    def rearrange(self, col):
        for row in range(2, 0, -1):
            if not(self.table[row][col]):
                check = row - 1
                while check >= 0 and not(self.table[check][col]):
                    check -= 1
                if check >= 0:
                    self.table[row][col], self.table[check][col] = self.table[check][col], self.table[row][col]


    def update_points(self):
        self.total_points = 0
        for col in range(3):
            multiplier = {}
            for row in range(3):
                current_number = self.table[row][col]
                if current_number in multiplier:
                    multiplier[current_number] += 1
                else:
                    multiplier[current_number] = 1
            for key in multiplier:
                self.total_points += (key * multiplier[key]) * multiplier[key]


    def isfull(self):
        for col in range(3):
            if not(self.table[0][col]):
                return False
        return True

    def __str__(self):
        str = ""
        for row in range(3):
            str += f"{self.table[row]}\t"
            for link in self.links:
                str += f"{link.table[row]}\t"
            str += '\n'
        if len(self.name) > 4:
            str += f"{self.name[:4]}..: {self.total_points}\t"
        else:
            str += f"{self.name}: {self.total_points}\t\t"
        for link in self.links:
            if len(link.name) > 4:
                str += f"{link.name[:4]}..: {link.total_points}\t"
            else:
                str += f"{link.name}: {link.total_points}\t\t"
        str += '\n'
        return str
