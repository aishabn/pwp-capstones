class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email
        
    def change_email(self, address):
        self.email = address
        print("The user {} email has been updated to {}".format(self.name, self.email))
        
    def __repr__(self):
        return("The user: {}, with email: {}, has {} books read".format(self.name, self.email, len(self.books)))
    
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
        
    def read_book(self, book, rating = None):
        self.books[book] = rating
        
    def get_average_rating(self):
        count = 0
        total = 0
        for rate in self.books.values():
            if rate:
                count += 1
                total += rate
                avg = total / count
        return avg
        
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.ratings = []
        self.isbn = isbn

        
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
        
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN of the book {} has been updated to {}". format(self.title, self.isbn))
        
    def add_rating(self, rating):
        if rating :
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
   
    def __repr__(self):
        return self.title
        
    def get_average_rating(self):
        total = 0
        for rate in self.ratings:
            total += rate
        if len(self.ratings) > 0:
            avg = total / len(self.ratings)
        else:
            avg = 0
        return avg
        
class Fiction(Book):
    
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return("{} by {}".format(self.title, self.author))
        
class Non_Fiction(Book):
    
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
            
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
        
    def __repr__(self):
        return("{}, a {} manual on {}".format(self.title, self.level, self.subject))
        

class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}
   
    def __repr__(self):
        return "TomeRater {} and {}".format(self.users, self.books)

    def __str__(self):
        return "in TomeRater users are {} and books are {}". format(self.users, self.books)
   
    def __eq__(self, other_rater):
        if self.users == other_raters.users and self.books == other_rater.books:
            return True
        else:
            return False
     
    def create_book(self, title, isbn):
        new = Book(title, isbn)
        return new
            
    def create_novel(self, title, author, isbn):
        new = Fiction(title, author, isbn)
        return new
        
    def create_non_fiction(self, title, subject, level, isbn):
        new = Non_Fiction(title, subject, level, isbn)
        return new
        
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        if email in self.users.items():
            print ("The user already exists!")
        else:
            new_user = User(name, email)
            self.users[email] = new_user
            
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
        
    def print_catalog(self):
        for i in self.books:
            print(i)
            
    def print_users(self):
        for u in self.users.values():
            print(u)
    
    def most_read_book(self):
        count = 0
        most = None
        for book in self.books:
            num = self.books[book]
            if num > count:
                count = num
                most = book
        return most
    
    def highest_rated_book(self):
        max_rate = 0
        max_book = None
        for book in self.books:
            avg_book = book.get_average_rating()
            if avg_book > max_rate:
                max_rate = avg_book
                max_book = book
            return max_book
        
    def most_positive_user(self):
        positive = 0
        pos_user = None
        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > positive:
                positive = avg
                pos_user = user
        return pos_user
        

            
