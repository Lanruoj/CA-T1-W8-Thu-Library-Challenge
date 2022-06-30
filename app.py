#----FUNCTIONS----#

def _author_check(catalogue, author, title):
    if author in catalogue:
        return True
    else:
        return False

def _title_check(catalogue, author, title):
    if title in catalogue[author]:
        return True
    else:
        return False

def _stock_check(catalogue, author, title):
    if (title in catalogue[author]) and (author in catalogue):
        return True
    else:
        return False
        

def _loan_book(catalogue, author, title):
    if _stock_check(catalogue, author, title):
        catalogue[author].pop()
        print(f"'{title}' by '{author}' borrowed\nCatalogue:\n{catalogue}")

def _return_book(catalogue, author, title):
        # if author AND title already in catalogue
        if _stock_check(catalogue, author, title):
            catalogue[author].append(title)
            print("BOTH EXISTING, ADDED TITLE TO AUTHOR")
        # if only author already in catalogue
        elif _author_check(catalogue, author, title) and not (_title_check(catalogue, author, title)):
            print("EXISTING AUTHOR, ADDED TITLE TO AUTHOR")
            catalogue[author].append(title)
        # if only title already in catalogue
        elif author not in catalogue: 
            print("EXISTING TITLE, ADDED AUTHOR AND TITLE")
            catalogue[author] = []
            catalogue[author].append(title)

        print(catalogue)  
        # print(f"'{title}' by '{author}' returned\nCatalogue:\n{catalogue}")

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


#---- WORKING ----#

# # AUTHOR + TITLE EXISTING
# main("return", "Madeleine Miller", "Tehanu")
# # AUTHOR EXISTING
# main("return", "Madeleine Miller", "Tehanu111")

#---- NOT WORKING----#

# TITLE EXISTING
main("return", "Madeleine Miller111", "Tehanu")
# NONE EXISTING
# main("return", "Madeleine Miller111", "Tehanu111")


