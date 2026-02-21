class Cookie:
    def __init__(self,color:str):
        self.color=color

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
        return color

first_cookie=Cookie("green")

print(first_cookie.color)

second_cookie=Cookie("white")
print(second_cookie.color)

first_cookie.setColor("white")
second_cookie.setColor("green")

print(first_cookie.color)
print(second_cookie.color)

print(first_cookie.getColor())
