import unittest
import os

from stock_search import StockSearch
from stock_picker import read_csv_file


class SimpleTest(unittest.TestCase):
    def test_stock_search(self):
        """Method to test StockSearch class and its method"""

        rows = read_csv_file(os.path.dirname(os.path.abspath(__file__)) + "/sample.csv")
        stock_search = StockSearch()

        for row in rows:
            stock_search.insert(row[0])

        self.assertEqual(stock_search.search("AICIXE"), (True, "AICIXE"))
        self.assertEqual(stock_search.search("AICIE"), (False, "AICIXE"))
        self.assertEqual(stock_search.search("AM"), (False, "AMBKP"))

    def test_csv(self):
        """Method to test read csv function"""

        rows = read_csv_file(os.path.dirname(os.path.abspath(__file__)) + "/sample.csv")
        self.assertEqual(len(rows), 5)


if __name__ == "__main__":
    unittest.main()
