

class Polo:
    def __init__(self, size, color, price=69.99):
        self.size = size
        self.color = color
        self.price = price

    def wash(self):
        #print("WASHING...")
        print(f"WASHING THE {self.size.upper()} {self.color.upper()} POLO!")

if __name__ == "__main__":
    # only execute if run from the command-line (not when imported)

    polo = Polo(size="Large", color="Blue")
    print(polo.size, polo.color, polo.price)
    polo.wash()

    polo2 = Polo(size="Small", color="Yellow")
    print(polo2.size, polo2.color, polo.price)
    polo2.wash()
