'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-04 22:15:52
@LastEditTime: 2019-11-08 17:22:29
@Description:
'''

import os
import json
import Class.strategy


def writeCardClassIndex(cardClassIndex):
    with open(
            './Data/Index/CardClassIndex.json', 'w',
            encoding='utf-8') as outfile:
        json.dump(cardClassIndex, outfile)


def readCardClassIndex():
    with open(
            './Data/Index/CardClassIndex.json', 'r',
            encoding='utf-8') as infile:
        return json.load(infile)


def getNewCardClassNum():
    cardClassIndex = readCardClassIndex()

    numList = []
    for carClassNum in cardClassIndex.keys():
        numList.append(int(carClassNum))
    return max(numList) + 1


class CardClass():
    def __init__(
            self,
            cardClassNum=getNewCardClassNum(),
            cardClassName='',
            cardClassStrategies=[],
            cardClassDescription='',
    ):
        self.cardClassNum = int(cardClassNum)
        self.cardClassName = cardClassName
        self.cardClassStrategies = cardClassStrategies
        self.cardClassDescription = cardClassDescription

    def cardStrategiesResult(self, member, card, product, cost):
        cardStrategiesResult = []
        for x in self.cardClassStrategies:
            s = strategy.Strategy(
                x.get('strategyNum'), x.get('strategyParams'))
            cardStrategiesResult.append(
                s.calculateCost(member, card, product, cost))
        return min(cardStrategiesResult)


def readCardClasses():
    try:
        result = {}
        for root, dirs, files in os.walk('./Data/CardClass/'):
            for f in files:
                if (f.startswith('CardClass') and f.endswith('.json')):
                    with open(
                            './Data/CardClass/' + f, 'r',
                            encoding='utf-8') as infile:
                        cardClass = json.load(infile)
                        result[cardClass.get('cardClassNum')] = CardClass(
                            cardClassNum=cardClass.get('cardClassNum'),
                            cardClassName=cardClass.get('cardClassName'),
                            cardClassStrategies=cardClass.get(
                                'cardClassStrategies'),
                            cardClassDescription=cardClass.get(
                                'cardClassDescription'))
        return result
    except:
        return None


def readCardClass(cardClassNum):
    try:
        with open(
                './Data/CardClass/CardClass' + str(cardClassNum) + '.json',
                'r',
                encoding='utf-8') as infile:
            cardClass = json.load(infile)
            return CardClass(
                cardClassNum=cardClass.get('cardClassNum'),
                cardClassName=cardClass.get('cardClassName'),
                cardClassStrategies=cardClass.get('cardClassStrategies'),
                cardClassDescription=cardClass.get('cardClassDescription'))
    except:
        return None


def cardClass2Dict(cardClass):
    return ({
        'cardClassNum': cardClass.cardClassNum,
        'cardClassName': cardClass.cardClassName,
        'cardClassStrategies': cardClass.cardClassStrategies,
        'cardClassDescription': cardClass.cardClassDescription,
    })


def writeCardClasses(cardClasses):
    for cardClass in cardClasses.values():
        with open(
                './Data/CardClass/CardClass' + str(cardClass.cardClassNum) +
                '.json',
                'w',
                encoding='utf-8') as outfile:
            json.dump(cardClass2Dict(cardClass), outfile)


def writeCardClass(cardClass):
    with open(
            './Data/CardClass/CardClass' + str(cardClass.cardClassNum) +
            '.json',
            'w',
            encoding='utf-8') as outfile:
        json.dump(cardClass2Dict(cardClass), outfile)


if __name__ == '__main__':
    c = CardClass('2类卡', [])
