'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 17:39:02
@LastEditTime: 2019-11-05 18:22:13
@Description:
'''

import time
import json

def nowTime():
    return [
        time.localtime(time.time()).tm_year,
        time.localtime(time.time()).tm_mon,
        time.localtime(time.time()).tm_mday,
        time.localtime(time.time()).tm_hour,
        time.localtime(time.time()).tm_min,
        time.localtime(time.time()).tm_sec
    ]


class Card():
    def __init__(self,
                 cardNum,
                 cardClassNum,
                 memberNum,
                 createTime=nowTime(),
                 consumptionRecord=[]):
        self.cardNum = cardNum
        self.cardClassNum = cardClassNum
        self.memberNum = memberNum
        self.createTime = createTime
        self.consumptionRecord = consumptionRecord

    def cardConsumption(self):
        pass


if __name__ == '__main__':
    c = Card(0, 0, 0)
