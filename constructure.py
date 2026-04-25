class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    
    def move(self):
        print(f"move on ({self.x},{self.y})")

    def draw(self):
        print("draw")

p=Point(10,20)
p.move()
print(p.x)   