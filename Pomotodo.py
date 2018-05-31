# coding=utf-8
import datetime
import sys

act1 = u"09:49 - 10:14\n#时间管理 '日·计划' |2018.05.31 + #生活/日常 '天气' |2018.05.31 + #人文/语言/英语 '单词·知米背单词' |2018.05.31"

taskSep = u" + "

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

    print actTime
    print taskSep.join(actTasks)

    for i in range(len(actTasks)):
        dumpTasks = actTasks[:]

        print
        print actTime
        task = u"**" + actTasks[i] + u"**"
        dumpTasks[i] = task
        print taskSep.join(dumpTasks)

    pass

def main(argv):
    print u"\#"
    parse_pomo_activity(act1)
    pass

if __name__ == '__main__':
    main(sys.argv[1:])
