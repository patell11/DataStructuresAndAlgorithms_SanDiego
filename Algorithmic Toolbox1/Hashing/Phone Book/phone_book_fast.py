
class PhoneBook:
    def __init__(self):
        self.phone_book_lst = [(None,None)] * 10000000

    def process(self, query):
        if query[0] == 'add':
            return self.add_number(query)
        elif query[0] == 'del':
            return self.del_number(query)
        else:
            return self.find_number(query)

    def add_number(self, query):
        number = int(query[1])
        self.phone_book_lst[number] = (number, query[2])

    def del_number(self, query):
        number = int(query[1])
        if self.phone_book_lst[number][0] == number:
            self.phone_book_lst[number] = (None, None)
        else:
            return

    def find_number(self, query):
        number = int(query[1])
        if self.phone_book_lst[number][0] == number:
            return self.phone_book_lst[number][1]
        else:
            return 'not found'


if __name__ == '__main__':
    n_queries = int(input())
    phone_book = PhoneBook()
    for i in range(n_queries):
        query = list(input().split())
        if query[0] == 'find':
            print(phone_book.process(query))
        else:
            phone_book.process(query)
    #print(phone_book.phone_book_lst)