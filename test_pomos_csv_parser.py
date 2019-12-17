import os
from unittest import TestCase

import pomos_csv_parser


class Test(TestCase):
    def test_parse_pomos_csv_file_unix(self):
        download_path="/home/thomas/Downloads"
        csv_file = "Pomos - 2019-12-16 - 2019-12-16.csv"
        pomos_csv_parser.parse_pomos_csv_file(download_path + os.sep + csv_file, "trello.md")
        # self.fail()
    pass

    def test_parse_pomos_csv_file_win(self):
        download_path=r"C:\Users\thomas\Downloads"
        csv_file = r"Pomos - 2019-12-16 - 2019-12-16.csv"

        in_file = download_path + os.sep + csv_file
        if os.path.exists(in_file):
            pomos_csv_parser.parse_pomos_csv_file(in_file, "trello.md")
        else:
            print "'%s' is not exist!" % in_file
        # self.fail()
    pass