import Game as g

players=[]
n=int(input("Enter number players"))
for x in range(n):
    players.append(x)
for i in range(n):
    players[i]=g.Game()
for j in range(n):
    g.Game.send_name(players[j])
k=0
while True:
    g.Game.display(players[k])
    g.Game.running(players[k])
    k+=1
    if k==n:
        k=0