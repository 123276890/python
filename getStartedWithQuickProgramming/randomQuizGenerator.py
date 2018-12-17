# -*- coding: utf-8 -*-
"""
假如你是一位地理老师，班上有35 名学生，你希望进行美国各州首府的一个
小测验。不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整
问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭
答案。
"""

import random

# 测试数据。键是状态，值是它们的大写。

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 生成35个测试文件
for quizNum in range(35):
    # 创建测试并回答关键文件。
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    # 写出测验的标题。
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # 打乱州的顺序。
    states = list(capitals.keys())
    random.shuffle(states)


# 遍历所有50个州，每个州提出一个问题。
for questionNum in range(50):
    # 得到正确和错误的答案。
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

# 将问题和答案选项写在测试文件中。
quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
    states[questionNum]))
for i in range(4):
    quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
quizFile.write('\n')
# 将答案键写入文件。
answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
    answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()