'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 17:42:39
@LastEditTime: 2019-11-26 15:54:25
@Description:
'''

import os
import json
import time


def writeMemberIndex(cardClassIndex):
    with open(
            './Data/Index/MemberIndex.json', 'w', encoding='utf-8') as outfile:
        json.dump(cardClassIndex, outfile)


def readMemberIndex():
    with open(
            './Data/Index/MemberIndex.json', 'r', encoding='utf-8') as infile:
        return json.load(infile)


def getNewMemberNum():
    memberIndex = readMemberIndex()

    numList = [-1]
    for memberNum in memberIndex.keys():
        numList.append(int(memberNum))
    return max(numList) + 1


def nowTime():
    return [
        time.localtime(time.time()).tm_year,
        time.localtime(time.time()).tm_mon,
        time.localtime(time.time()).tm_mday,
        time.localtime(time.time()).tm_hour,
        time.localtime(time.time()).tm_min,
        time.localtime(time.time()).tm_sec
    ]


class Member():
    def __init__(self,
                 memberNum=getNewMemberNum(),
                 name='',
                 gender='',
                 phoneNumber='',
                 birthday=[0, 0, 0],
                 createTime=nowTime(),
                 consumptionRecord=[]):
        self.memberNum = memberNum
        self.name = name
        self.gender = gender
        self.phoneNumber = phoneNumber
        self.birthday = birthday
        self.createTime = createTime
        self.consumptionRecord = consumptionRecord


def readMembers():
    try:
        result = {}
        for root, dirs, files in os.walk('./Data/Member/'):
            for f in files:
                if (f.startswith('Member') and f.endswith('.json')):
                    with open('./Data/Member/' + f, 'r') as infile:
                        member = json.load(infile)
                        result[member.get('memberNum')] = Member(
                            memberNum=member.get('memberNum'),
                            name=member.get('name'),
                            gender=member.get('gender'),
                            phoneNumber=member.get('phoneNumber'),
                            birthday=member.get('birthday'),
                            createTime=member.get('createTime'),
                            consumptionRecord=member.get('consumptionRecord'))
        return result
    except:
        return None


def readMember(memberNum):
    try:
        with open('./Data/Member/Member' + str(memberNum) + '.json',
                  'r') as infile:
            member = json.load(infile)
            return Member(
                memberNum=member.get('memberNum'),
                name=member.get('name'),
                gender=member.get('gender'),
                phoneNumber=member.get('phoneNumber'),
                birthday=member.get('birthday'),
                createTime=member.get('createTime'),
                consumptionRecord=member.get('consumptionRecord'))
    except:
        print(Exception)


def Member2Dict(member):
    return ({
        'memberNum': member.memberNum,
        'name': member.name,
        'gender': member.gender,
        'phoneNumber': member.phoneNumber,
        'birthday': member.birthday,
        'createTime': member.createTime,
        'consumptionRecord': member.consumptionRecord
    })


def writeMembers(members):
    for member in members.values():
        with open('./Data/Member/Member' + str(member.memberNum) + '.json',
                  'w') as outfile:
            json.dump(Member2Dict(member), outfile)


def writeMember(member):
    with open('./Data/Member/Member' + str(member.memberNum) + '.json',
              'w') as outfile:
        json.dump(Member2Dict(member), outfile)


if __name__ == '__main__':
    m0 = Member(0, 'TEST0', 'MALE', '18800097819', [1997, 8, 19])
    m1 = Member(1, 'TEST1', 'FEMALE', '18800097818', [1997, 8, 18])
    writeMembers({0: m0, 1: m1})
    m = readMembers()
    i = 0
