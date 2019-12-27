# coding=utf-8
import codecs
import csv
import sys


def parse_pomo_csv_file(src_file, md_file, note_file):
    print "csv_file: %s" % src_file
    print "md_file: %s" % md_file
    print "note_file: %s" % note_file

    out_md = codecs.open(md_file, 'w', 'utf-8-sig')
    out_note = codecs.open(note_file, 'w', 'utf-8-sig')

    with open(src_file)as in_file:
        f_csv = csv.reader(in_file)
        i = 0
        for row in f_csv:
            if i > 0:
                from pomo_info import Activity
                activity = Activity(row[0], row[1], row[2], row[3])
                # print activity.to_markdown()
                out_md.write(activity.to_markdown().decode('utf-8'))
                out_note.write(activity.to_text().decode('utf-8'))
            i = i + 1
    out_md.close()
    out_note.close()

    pass


def main(argv):
    if len(argv) < 3:
        print "usage: $pomos_csv_file, %md_file, %note_file"
    src_file = argv[0]
    md_file = argv[1]
    note_file = argv[2]

    parse_pomo_csv_file(src_file, md_file, note_file)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
