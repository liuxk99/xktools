# coding=utf-8
import codecs
import csv
import sys


def parse_pomos_csv_file(src_file, dst_file):
    print "csv_file: %s" % src_file
    print "dst_file: %s" % dst_file

    out_file = codecs.open(dst_file, 'w', 'utf-8-sig')

    with open(src_file)as in_file:
        f_csv = csv.reader(in_file)
        i = 0
        for row in f_csv:
            if i > 0:
                from pomo_info import Activity
                activity = Activity(row[0], row[1], row[2], row[3])
                # print activity.to_markdown()
                out_file.write(activity.to_markdown().decode('utf-8'))
            i = i + 1
    out_file.close()
    pass


def main(argv):
    if len(argv) < 2:
        print "usage: $pomos_csv_file, %dest_file"
    src_file = argv[0]
    dst_file = argv[1]

    parse_pomos_csv_file(src_file, dst_file)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
