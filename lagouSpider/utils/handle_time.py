#可以用来处理发布的日期，过于繁琐未完成

import re
import datetime
import time
text = '9:04  发布于拉勾网'
text1 = '1天前  发布于拉勾网'
text2 = '2017-05-16  发布于拉勾网'
match_obj = re.match('(.*?) .*', text1).group(1)
print(match_obj)
if re.match('\d{4}-\d{2}-\d{2}', match_obj):
    print('date')
if re.match('(.*?)天前', match_obj):
    print('date1')
    date = re.match('(.*?)天前', match_obj).group(1)
    if date == '1':
        now_day = int(datetime.datetime.now().day)
        date = int(date)
        print(now_day - date)

if re.match('.*?:.*?', match_obj):
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))



