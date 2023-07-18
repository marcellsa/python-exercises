# Dado o seguinte arquivo no formato JSON, leia seu conteúdo e calcule
# a porcentagem de livros em cada categoria em relação ao número total
# de livros. O resultado deve ser escrito em um arquivo no formato CSV
# como o exemplo abaixo.
import json
import csv

# Recuperar o arquivo books
def retrive_books(file):
    return json.load(file)


# Calcular a qauntidade de livros por categoria
def count_books_by_category(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
              categories[category] = 0
            categories[category] += 1
    return categories


# Calcular percentual de livros
def calculate_percentage_by_category(book_count_by_category, total_books):
    return [
        [category, books_amout / total_books]
        for category, books_amout in book_count_by_category.items()
    ]


# Escrever o csv
def write_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main":
    # retrive books
    with open('books.json') as file:
        books = retrive_books(file)

    # count by category
    book_count_by_category = count_books_by_category(books)

    # calculate percentage
    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(book_count_by_category, number_of_books)

    # write csv file
    header = ['categorias', 'porcentagem']
    with open('report.csv', 'w') as file:
        write_csv_report(file, header, books_percentage_rows)
