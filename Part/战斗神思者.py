from PublicReference.base import *


class 战斗神思者技能0(主动技能):
    名称 = '普通攻击(一轮)'
    所在等级 = 1
    等级上限 = 3
    基础等级 = 1
    基础 = 9139.2
    成长 = 86.9
    CD = 1.0
    TP成长 = 0.1
    TP上限 = 3

class 战斗神思者技能1(主动技能):
    名称 = '空斩打'
    所在等级 = 1
    等级上限 = 20
    基础等级 = 10
    基础 = 590.5
    成长 = 64.7
    基础2 = 2547.4
    成长2 = 0
    攻击次数2 = 1
    CD = 2.0
    TP成长 = 0.062
    TP上限 = 8

class 战斗神思者技能2(主动技能):
    名称 = '落凤锤'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 1
    基础 = 11232.0
    成长 = 0.0
    CD = 6.0



class 战斗神思者技能3(被动技能):
    名称 = '勇气恩赐'
    所在等级 = 15
    等级上限 = 25
    基础等级 = 15

    def 加成倍率(self, 武器类型):
        return (1.15 + (self.等级 - 15) * 0.02) if self.等级 >= 15 else (1 + self.等级 * 0.01)


class 战斗神思者技能4(主动技能):
    名称 = '光之复仇'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 182.0
    成长 = 18.5
    CD = 0.2
    TP成长 = 0.10
    TP上限 = 7


class 战斗神思者技能5(主动技能):
    名称 = '纯白之刃'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 44
    基础 = 2203.4
    成长 = 248.9
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 7


class 战斗神思者技能6(被动技能):
    名称 = '坚定信念'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        return (1.10 + (self.等级 - 10) * 0.015) if self.等级 >= 10 else (1 + self.等级 * 0.01)


class 战斗神思者技能7(主动技能):
    名称 = '胜利之矛'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 42
    基础 = 1993.6
    成长 = 225.1
    CD = 6.6
    TP成长 = 0.10
    TP上限 = 7


class 战斗神思者技能8(主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级上限 = 50
    基础等级 = 41
    基础 = 3378.0
    成长 = 342.8
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if (self.等级 < 1):
            return 1.0
        else:
            return 1.2


class 战斗神思者技能9(主动技能):
    名称 = '圣光沁盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3561.0
    成长 = 361.3
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 战斗神思者技能10(主动技能):
    名称 = '圣光琉璃碎'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9914.6
    成长 = 1007.6
    CD = 14.4
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25


class 战斗神思者技能11(主动技能):
    名称 = '圣光聚合'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 4113.0
    成长 = 417.5
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 7


class 战斗神思者技能12(主动技能):
    名称 = '忏悔之锤'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6588.0
    成长 = 668.4
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CD *= 0.90


class 战斗神思者技能13(主动技能):
    名称 = '正义审判'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 17520.0
    成长 = 1777.6
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25


class 战斗神思者技能14(被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.015 + 0.02 * self.等级, 5)


class 战斗神思者技能15(主动技能):
    名称 = '天启之珠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 40444.6
    成长 = 9384.5
    CD = 145


class 战斗神思者技能16(主动技能):
    名称 = '圣光突袭'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 10620.0
    成长 = 1077.6
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CD *= 0.90


class 战斗神思者技能17(主动技能):
    名称 = '神圣之矛'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 13062.0
    成长 = 1325.6
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25


class 战斗神思者技能18(主动技能):
    名称 = '神圣之光'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 21714.0
    成长 = 2202.8
    CD = 20.0


class 战斗神思者技能19(主动技能):
    名称 = '圣佑结界'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 39934.0
    成长 = 4051.3
    CD = 40.0


class 战斗神思者技能20(主动技能):
    名称 = '神罚之锤'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.02 * self.等级, 5)


class 战斗神思者技能21(主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 105962.9
    成长 = 18839.3
    CD = 180.0


class 战斗神思者技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 战斗神思者技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 战斗神思者技能24(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


战斗神思者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('战斗神思者技能列表.append(战斗神思者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

战斗神思者技能序号 = dict()
for i in range(len(战斗神思者技能列表)):
    战斗神思者技能序号[战斗神思者技能列表[i].名称] = i

战斗神思者一觉序号 = 0
战斗神思者二觉序号 = 0
战斗神思者三觉序号 = 0
for i in 战斗神思者技能列表:
    if i.所在等级 == 50:
        战斗神思者一觉序号 = 战斗神思者技能序号[i.名称]
    if i.所在等级 == 85:
        战斗神思者二觉序号 = 战斗神思者技能序号[i.名称]
    if i.所在等级 == 100:
        战斗神思者三觉序号 = 战斗神思者技能序号[i.名称]

战斗神思者护石选项 = ['无']
for i in 战斗神思者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        战斗神思者护石选项.append(i.名称)

战斗神思者符文选项 = ['无']
for i in 战斗神思者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        战斗神思者符文选项.append(i.名称)


class 战斗神思者角色属性(角色属性):
    职业名称 = '战斗神思者'

    武器选项 = ['镰刀', '念珠', '战斧', '十字架']

    # '物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法固伤']

    # 默认
    伤害类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.97

    # 基础属性(含唤醒)
    基础力量 = 793.0
    基础智力 = 782.0

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    def __init__(self):
        self.技能栏 = copy.deepcopy(战斗神思者技能列表)
        self.技能序号 = copy.deepcopy(战斗神思者技能序号)


class 战斗神思者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 战斗神思者角色属性()
        self.角色属性A = 战斗神思者角色属性()
        self.角色属性B = 战斗神思者角色属性()
        self.一觉序号 = 战斗神思者一觉序号
        self.二觉序号 = 战斗神思者二觉序号
        self.三觉序号 = 战斗神思者三觉序号
        self.护石选项 = copy.deepcopy(战斗神思者护石选项)
        self.符文选项 = copy.deepcopy(战斗神思者符文选项)
