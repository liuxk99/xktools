from unittest import TestCase

import pomos_csv_parser


class Test(TestCase):
    def test_parse_pomos_csv_file_unix(self):
        pomos_csv_parser.parse_pomos_csv_file("/home/thomas/Downloads/2019-12-03.csv", "trello.md")
        # self.fail()
    pass

    def test_parse_pomos_csv_file_win(self):
        pomos_csv_parser.parse_pomos_csv_file(r"C:\Users\thomas\Downloads\Pomos - 2019-12-14 - 2019-12-14.csv", "trello.md")
        # self.fail()
    pass