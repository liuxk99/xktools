import os
from unittest import TestCase

import pomos_csv_parser


def parse_csv_file(download_path, csv_file):
    in_file = download_path + os.sep + csv_file
    if os.path.exists(in_file):
        pomos_csv_parser.parse_pomo_csv_file(in_file, "trello.md", "YNote.md")
    else:
        print "'%s' is not exist!" % in_file
    pass


class Test(TestCase):
    def test_parse_pomos_csv_file_unix(self):
        download_path = "/home/thomas/Downloads"
        date = r"2020-03-23"
        csv_file = r"Pomos - %s - %s.csv" % (date, date)

        parse_csv_file(download_path, csv_file)
        # self.fail()

    pass

    def test_parse_pomos_csv_file_win(self):
        download_path = r"C:\Users\thomas\Downloads"
        date = r"2020-03-20"
        csv_file = r"Pomos - %s - %s.csv" % (date, date)

        parse_csv_file(download_path, csv_file)
        # self.fail()

    pass
