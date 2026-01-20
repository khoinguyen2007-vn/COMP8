import sys

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)
class Library:
    def __init__(self):
        self.books = []
    def add(self, book):
        self.books.append(book)
    def count_by_author(self, name):
        count = 0
        for book in self.books:
            if book.author == name:
                count += 1
        return count
    def find_by_year(self, y):
        count = 0
        for book in self.books:
            if book.year == y:
                count += 1
        return count
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    try:
        n = int(input_data[0])
    except ValueError:
        return
    lib = Library()
    for i in range(1, n + 1):
        if i >= len(input_data):
            break   
        line = input_data[i].strip()
        if not line:
            continue    
        parts = line.split(' ', 1)
        command = parts[0]
        if command == 'ADD':
            args = parts[1].split(';')
            lib.add(Book(args[0], args[1], args[2]))          
        elif command == 'COUNT':
            print(lib.count_by_author(parts[1]))       
        elif command == 'COUNTYEAR':
            print(lib.find_by_year(int(parts[1])))
if __name__ == "__main__":
    solve()