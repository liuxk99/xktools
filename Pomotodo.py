# coding=utf-8
import sys

pomo = u"09:45 - 10:10 #人文/语言/英语 '单词·知米背单词' |2018.05.30 + #财经/理财/投资/股票 '乐视网·操盘' |2018.05.30"
split = u" + "

def main(argv):
    tasks = pomo.split(split)
    for task in tasks:
        print task
    pass

if __name__ == '__main__':
    main(sys.argv[1:])
