class Point:
    def move(self):
        print("Point moved")

    def draw(self):
        print("draw")


p1=Point()
p1.draw()
p1.x=10
p1.y=20
print(p1.x)