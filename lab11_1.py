
import csv


def read_products(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = list(reader)
    return products


def write_products(filename, products):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["product", "price"])
        writer.writeheader()
        writer.writerows(products)


products = read_products("products.csv")
write_products("products_out.csv", products)

print("Дані успішно записано у файл products_out.csv")
