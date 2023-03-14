
class GotCharacter:
    """ A class representing the "Game of Thrones" character. """
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Lannister(GotCharacter):
    """ A class representing the Lannister family. Or when bad things happen to good people. """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"

    def print_house_words(self):
        """ Print the house words of the Lannister family """
        print(self.house_words)

    def die(self):
        """ Kill the character """
        self.is_alive = False

    def	__str__(self) -> str:
        txt = "{} with house {} and house words '{}' is alive? {}".format(
            self.first_name,
            self.family_name,
            self.house_words,
            self.is_alive)
        return txt

def	main( ):
    """ Main function """
    a = Lannister("Peter", True)
    a.print_house_words()
    print(a)
    
if __name__ == "__main__":
    main()
