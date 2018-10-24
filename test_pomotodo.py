# coding=utf-8
import codecs
import os
from unittest import TestCase

import Pomotodo
from Pomotodo import parse_pomo_activity


class TestParse_pomo_activity(TestCase):
    def test_parse_pomo_activity(self):
        act1 = u"09:49 - 10:14\n#时间管理 '日·计划' |2018.05.31 + #生活/日常 '天气' |2018.05.31 + #人文/语言/英语 '单词·知米背单词' |2018.05.31"
        parse_pomo_activity(act1)

        act2 = u"11:12 - 11:43\n#时间管理/工具 'pomotodo·parser'"
        parse_pomo_activity(act2)
        pass

    def test_pomotodo_001(self):
        act2 = u"18:34 - 19:38\n#产品(Zero65)/Issue '重量级改变·Screen compatibility'"
        parse_pomo_activity(act2)
        pass

    def test_pomotodo_002(self):
        # parse a file
        path = r"E:\\"
        src_file = r"activities.txt"
        dst_file = r"pomo.txt"

        f = codecs.open(path + os.path.sep + src_file, 'r', 'utf-8')
        lines = f.readlines()

        # for line in lines:
        #     print line

        activities = []
        pomo_count = len(lines) / 2
        for i in xrange(pomo_count):
            idx = 2 * i
            activity = lines[idx] + lines[idx + 1]
            activities.append(activity)

        activities.reverse()

        out_file = codecs.open(path + os.path.sep + dst_file, 'w', 'utf-8-sig')
        for activity in activities:
            act = Pomotodo.activity_to_str(activity)
            out_file.write(act)

        pass
