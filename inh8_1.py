class Base:
    def __init__(self):
        print("Inside class Base default constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside class Derived default constructor") 


if __name__ == "__main__":
    obj = Derived()
