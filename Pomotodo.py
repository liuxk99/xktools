# coding=utf-8
import codecs
import datetime
import sys

act1 = u"09:49 - 10:14\n#时间管理 '日·计划' |2018.05.31 + #生活/日常 '天气' |2018.05.31 + #人文/语言/英语 '单词·知米背单词' |2018.05.31"

taskSep = u" + "
line_feed = u'\n'


def parse_pomo_activity(activity):
    lines = activity.splitlines()
    # for line in lines:
    #     print line

    actTime = datetime.datetime.now().strftime("%Y.%m.%d") + u" " + lines[0]
    # print "time: " + actTime

    actTasks = lines[1].split(taskSep)
    pos = actTasks[0].find(u"#")
    if (pos == 0):
        actTasks[0] = actTasks[0].replace(u"#", u"\#")
    for task in actTasks:
        # print "task: " + task
        pass

    for i in range(len(actTasks)):
        dumpTasks = actTasks[:]

        print actTime
        task = u"**" + actTasks[i] + u"**"
        dumpTasks[i] = task
        print taskSep.join(dumpTasks)
        print '---'

    pass


def activity_to_str(activity):
    res = u""
    lines = activity.splitlines()
    # for line in lines:
    #     print line

    actTime = datetime.datetime.now().strftime("%Y.%m.%d") + u" " + lines[0]
    # print "time: " + actTime

    actTasks = lines[1].split(taskSep)
    pos = actTasks[0].find(u"#")
    if (pos == 0):
        actTasks[0] = actTasks[0].replace(u"#", u"\#")
    for task in actTasks:
        # print "task: " + task
        pass

    for i in range(len(actTasks)):
        dumpTasks = actTasks[:]

        # print actTime
        res += actTime + line_feed
        task = u"**" + actTasks[i] + u"**"
        dumpTasks[i] = task
        res += taskSep.join(dumpTasks) + line_feed
        res += '---' + line_feed
        res += line_feed

    return res
    pass


def parse_pomotodo_file(src_file, dst_file):
    print 'parse_pomotodo_file(%s, %s)' % (src_file, dst_file)

    in_file = codecs.open(src_file, 'r', 'utf-8')
    lines = in_file.readlines()
    # for line in lines:
    #     print line
    activities = []
    pomo_count = len(lines) / 2
    for i in xrange(pomo_count):
        idx = 2 * i
        activity = lines[idx] + lines[idx + 1]
        activities.append(activity)
    activities.reverse()
    out_file = codecs.open(dst_file, 'w', 'utf-8-sig')
    for activity in activities:
        act = activity_to_str(activity)
        out_file.write(act)

def main(argv):
    if len(argv) < 2:
        print "usage: $activities_file, %dest_file"
    src_file = argv[0]
    dst_file = argv[1]

    parse_pomotodo_file(src_file, dst_file)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
