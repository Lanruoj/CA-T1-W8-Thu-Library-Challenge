#----FUNCTIONS----#

def _author_check(catalogue, author, title):
    if (author in catalogue) and (title in catalogue[author]):
        return True
    else:
        return False

def _loan_book(catalogue, author, title):
    if _stock_check(catalogue, author, title):
        catalogue[author].pop()
        print(f"'{title}' by '{author}' borrowed\nCatalogue:\n{catalogue}")

def _return_book(catalogue, author, title):
        if _stock_check(catalogue, author, title):
            catalogue[author].append(title)
            print("author already in cat")
            print(catalogue)
        #----IF AUTHOR NOT ALREADY IN CATALOGUE----#
        else:
            catalogue[author] = []
            catalogue[author].append(title) 
            print(f"'{title}' by '{author}' returned\nCatalogue:\n{catalogue}")
            print("adding new title")

#----PROGRAM----#

def main(task, author, title):
    catalogue = {
    "N.K. Jemisin": ["The Fifth Season"],
    "Ursula Le Guin": ["The Left Hand Of Darkness", "Tehanu"],
    "Richard Morgan": ["Woken Furies"],
    "Charlie Jane Anders": ["The City in the Middle of the Night"],
    "Garth Nix": ["Sabriel"],
    "Kiril Yeskov": ["The Last Ringbearer"],
    "Madeleine Miller": ["Tehanu"]
    }
    if task=="check":
        if _stock_check(catalogue, author, title):
            print("Book in stock")
        else:
            print("Book not in stock")
    elif task=="loan":
        if _stock_check(catalogue, author, title):
            print("Book in stock")
            _loan_book(catalogue, author, title)
        else:
            print("Book not in stock")
    elif task=="return":
        _return_book(catalogue, author, title)

main("return", "Madeleine Millers", "Tehanul")


