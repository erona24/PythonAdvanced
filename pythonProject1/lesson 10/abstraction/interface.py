from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Implementing the abstract method
    def print_info(self):
        print(f"book: {self.title} by {self.author}")


book3456 = Book(title="atomic habits", author="james clear")

book3456.print_info()
