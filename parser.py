import json
from models import Product

class Parser:

    def parse(self, filename):
        """
        Parses a JSON file into a Python dictionary
        :param filename: a string, in the format of "product.json", the file needs to be in the same directory
        :return: a dictionary containing all products and their properties.
        """
        with open(filename, "r") as file:
            products_list = json.load(file)
        return products_list

    def add_product(self, product_list):
        """

        :param product_list: a list of dictionaries. Each dictionary represents a product
        :return: a list of products
        """
        final_list = {}
        increment = 0
        for product in product_list:
            print(product)
            p = Product(product['name'], product['price'], product['stock'], product['updated'])
            final_list[0] = product
            increment += 1
        return final_list
