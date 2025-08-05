from Player import Player

player1 = Player()
player2 = Player()
player1.link(player2)
player1.place(3,2)
player2.place(2,2)
print(player1)

player1.place(3, 2)
player2.place(6, 2)

print(player1)

player1.place(6, 2)
player2.place(3, 2)
print(player1)
