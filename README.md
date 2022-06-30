# Thursday 30 June daily challenge


You work at a library. You book catalogue is stored in a dictionary, with author names as the keys, and lists of book names as the values, like so: 

```python
catalogue = {
    "N.K. Jemisin": ["The Fifth Season"],
    "Ursula Le Guin": ["The Left Hand Of Darkness", "Tehanu"],
    "Richard Morgan": ["Woken Furies"],
    "Charlie Jane Anders": ["The City in the Middle of the Night"],
    "Garth Nix": ["Sabriel"],
    "Kiril Yeskov": ["The Last Ringbearer"],
    "Madeleine Miller": ["Tehanu"]
}
```


Write three functions:
- A function called _stock_check to check if a given book is in stock
- A function called _loan_book to remove a book from the catalogue
- A function called _return_book to add a book to the catalogue

## Examples:
_stock_check should accept a catalogue dictionary, an author name, and a book title as its arguments. It should return either True if the book is available, or False if not, like so:

`_stock_check(catalogue, "Ursula Le Guin", "Tehanu")`

### Output is True
 
_loan_book should accept a catalogue dictionary, an author name, and a book title as its arguments. It should return a catalogue dictionary with the book in question removed, like so:

`_loan_book(catalogue, "Ursula Le Guin", "Tehanu")`

### output is:

```python
{
    "N.K. Jemisin": ["The Fifth Season"],
    "Ursula Le Guin": ["The Left Hand Of Darkness"],
    "Richard Morgan": ["Woken Furies"],
    "Charlie Jane Anders": ["The City in the Middle of the Night"],
    "Garth Nix": ["Sabriel"],
    "Kiril Yeskov": ["The Last Ringbearer"],
    "Madeleine Miller": ["Tehanu"]
}
```
 
_return_book should accept a catalogue dictionary, an author name, and a book title as its arguments. It should return a catalogue dictionary with the book in question added, like so:

`_return_book(catalogue, "Phillip K.Dick", "Do Androids Dream of Electric Sheep")
`
### output is:

```python
{
    "N.K. Jemisin": ["The Fifth Season"],
    "Ursula Le Guin": ["The Left Hand Of Darkness"],
    "Richard Morgan": ["Woken Furies"],
    "Charlie Jane Anders": ["The City in the Middle of the Night"],
    "Garth Nix": ["Sabriel"],
    "Kiril Yeskov": ["The Last Ringbearer"],
    "Madeleine Miller": ["Tehanu"],
    "Phillip K.Dick": ["Do Androids Dream of Electric Sheep"]
}
```