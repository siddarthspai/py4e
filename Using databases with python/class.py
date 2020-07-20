class PartyAnimal:
    x=0
    def __init__(self):
        print("Hello")
    def party(self):
        self.x+=1
        print("So far",self.x)
    def __del__(self):
        print("Bye",self.x)
an= PartyAnimal()
an.party()
an.party()
an.party()
an=42
print("an contains",an)