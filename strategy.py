'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-04 22:15:52
@LastEditTime: 2019-11-07 11:13:03
@strategyDescription:
'''

import json


def discount(member, card, product, cost, strategyParams):
    return cost * strategyParams[0]


def fullReduction(member, card, product, cost, strategyParams):
    return cost - int(cost / strategyParams[0]) * strategyParams[1]


strategyNum2Func = {0: discount, 1: fullReduction}
strategyNum2Name = {0: '折扣', 1: '满减'}
strategyNum2Description = {0: '', 1: ''}


class Strategy():
    def __init__(
            self,
            strategyNum,
            strategyParams,
            strategyDescription='',
    ):
        self.strategyNum = strategyNum
        self.strategyParams = strategyParams
        self.strategyDescription = strategyDescription

    def calculateCost(self, member, card, product, cost):
        return strategyNum2Func.get(self.strategyNum)(member, card, cost,
                                                      self.strategyParams)


if __name__ == '__main__':
    s = Strategy(1, [30, 5], '')
    print(s.calculateCost(0, 0, 100, 0))
