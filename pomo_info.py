# coding=utf-8

import dateutil.parser


def get_datetime_from_iso8601(s):
    d = dateutil.parser.parse(s)
    return d


class Activity:
    def __init__(self, _uuid, _begin, _end, _description):
        self._uuid = _uuid
        self._begin = _begin
        self._end = _end
        self._description = _description

    def __str__(self):
        begin_date = get_datetime_from_iso8601(self._begin)
        end_date = get_datetime_from_iso8601(self._end)
        cur_date = begin_date.strftime("%Y/%m/%d")
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s [%s - %s]\n%s' % (cur_date, begin_time, end_time, self._description)

    def to_markdown(self):
        begin_date = get_datetime_from_iso8601(self._begin)
        end_date = get_datetime_from_iso8601(self._end)
        cur_date = begin_date.strftime("%Y/%m/%d")
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s [%s - %s]\n**\\%s**\n---\n' % (cur_date, begin_time, end_time, self._description)

    def to_text(self):
        # to text as YouNote spec.
        begin_date = get_datetime_from_iso8601(self._begin)
        end_date = get_datetime_from_iso8601(self._end)
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s - %s\n%s\n' % (begin_time, end_time, self._description)
    pass
