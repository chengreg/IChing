# -*- encoding: utf-8 -*-
"""
@File    : numberTo64.py
@Time    : 2021/10/4 21:51
@Author  : Chen GangQiang
@Email   : uoaoo@163.com
@Software: PyCharm
"""


class NumberTo64:
    def __init__(self, num1: int, num2: int, num3: int):
        # 初始化三个数字
        self.n1 = num1 % 8
        self.n2 = num2 % 8
        self.n3 = num3 % 6
        if self.n1 == 0:
            self.n1 = 8
        if self.n2 == 0:
            self.n2 = 8
        if self.n3 == 0:
            self.n3 = 6
        # 乾兑离震巽坎艮坤
        self.baguaSort = {"1": "乾", "2": "兑", "3": "离", "4": "震", "5": "巽", "6": "坎", "7": "艮", "8": "坤"}
        self.baguaMean = {"乾": "天", "兑": "泽", "离": "火", "震": "雷", "巽": "风", "坎": "水", "艮": "山", "坤": "地"}

        self.down_name = self.baguaSort[str(self.n1)]
        self.up_name = self.baguaSort[str(self.n2)]
        self.yao = self.n3

        self.down_mean = self.baguaMean[self.down_name]
        self.up_mean = self.baguaMean[self.up_name]

        self.gua_group = self.up_mean + self.down_mean

    def result(self):
        resultDict = {}
        if self.gua_group == "天天":
            resultDict["卦序"] = 1
            resultDict["卦名"] = "乾卦"
            resultDict["组成"] = "乾为天"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地地":
            resultDict["卦序"] = 2
            resultDict["卦名"] = "坤卦"
            resultDict["组成"] = "坤为地"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水雷":
            resultDict["卦序"] = 3
            resultDict["卦名"] = "屯卦"
            resultDict["组成"] = "水雷屯"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山水":
            resultDict["卦序"] = 4
            resultDict["卦名"] = "蒙卦"
            resultDict["组成"] = "山水蒙"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水天":
            resultDict["卦序"] = 5
            resultDict["卦名"] = "需卦"
            resultDict["组成"] = "水天需"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天水":
            resultDict["卦序"] = 6
            resultDict["卦名"] = "讼卦"
            resultDict["组成"] = "天水讼"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地水":
            resultDict["卦序"] = 7
            resultDict["卦名"] = "师卦"
            resultDict["组成"] = "地水师"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水地":
            resultDict["卦序"] = 8
            resultDict["卦名"] = "比卦"
            resultDict["组成"] = "水地比"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风天":
            resultDict["卦序"] = 9
            resultDict["卦名"] = "小畜卦"
            resultDict["组成"] = "风天小畜"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天泽":
            resultDict["卦序"] = 10
            resultDict["卦名"] = "履卦"
            resultDict["组成"] = "天泽履"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地天":
            resultDict["卦序"] = 11
            resultDict["卦名"] = "泰卦"
            resultDict["组成"] = "地天泰"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天地":
            resultDict["卦序"] = 12
            resultDict["卦名"] = "否卦"
            resultDict["组成"] = "天地否"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天火":
            resultDict["卦序"] = 13
            resultDict["卦名"] = "同人卦"
            resultDict["组成"] = "天火同人"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火天":
            resultDict["卦序"] = 14
            resultDict["卦名"] = "大有卦"
            resultDict["组成"] = "火天大有"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地山":
            resultDict["卦序"] = 15
            resultDict["卦名"] = "谦卦"
            resultDict["组成"] = "地山谦"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷地":
            resultDict["卦序"] = 16
            resultDict["卦名"] = "豫卦"
            resultDict["组成"] = "雷地豫"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽雷":
            resultDict["卦序"] = 17
            resultDict["卦名"] = "随卦"
            resultDict["组成"] = "泽雷随卦"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山风":
            resultDict["卦序"] = 18
            resultDict["卦名"] = "蛊卦"
            resultDict["组成"] = "山风蛊"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地泽":
            resultDict["卦序"] = 19
            resultDict["卦名"] = "临卦"
            resultDict["组成"] = "地泽临"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风地":
            resultDict["卦序"] = 20
            resultDict["卦名"] = "观卦"
            resultDict["组成"] = "风地观"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火雷":
            resultDict["卦序"] = 21
            resultDict["卦名"] = "噬嗑卦"
            resultDict["组成"] = "火雷噬嗑"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山火":
            resultDict["卦序"] = 22
            resultDict["卦名"] = "贲卦"
            resultDict["组成"] = "山火贲"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山地":
            resultDict["卦序"] = 23
            resultDict["卦名"] = "剥卦"
            resultDict["组成"] = "山地剥"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地雷":
            resultDict["卦序"] = 24
            resultDict["卦名"] = "复卦"
            resultDict["组成"] = "地雷复"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天雷":
            resultDict["卦序"] = 25
            resultDict["卦名"] = "无妄卦"
            resultDict["组成"] = "天雷无妄"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山天":
            resultDict["卦序"] = 26
            resultDict["卦名"] = "大畜卦"
            resultDict["组成"] = "山天大畜"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山雷":
            resultDict["卦序"] = 27
            resultDict["卦名"] = "颐卦"
            resultDict["组成"] = "山雷颐"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽风":
            resultDict["卦序"] = 28
            resultDict["卦名"] = "大过卦"
            resultDict["组成"] = "泽风大过"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水水":
            resultDict["卦序"] = 29
            resultDict["卦名"] = "坎卦"
            resultDict["组成"] = "坎为水"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火火":
            resultDict["卦序"] = 30
            resultDict["卦名"] = "离卦"
            resultDict["组成"] = "离为火"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽山":
            resultDict["卦序"] = 31
            resultDict["卦名"] = "咸卦"
            resultDict["组成"] = "泽山咸"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷风":
            resultDict["卦序"] = 32
            resultDict["卦名"] = "恒卦"
            resultDict["组成"] = "雷风恒"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天山":
            resultDict["卦序"] = 33
            resultDict["卦名"] = "遁卦"
            resultDict["组成"] = "天山遁"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷天":
            resultDict["卦序"] = 34
            resultDict["卦名"] = "大壮卦"
            resultDict["组成"] = "雷天大壮"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火地":
            resultDict["卦序"] = 35
            resultDict["卦名"] = "晋卦"
            resultDict["组成"] = "火地晋"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地火":
            resultDict["卦序"] = 36
            resultDict["卦名"] = "明夷卦"
            resultDict["组成"] = "地火明夷"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风火":
            resultDict["卦序"] = 37
            resultDict["卦名"] = "家人卦"
            resultDict["组成"] = "风火家人"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火泽":
            resultDict["卦序"] = 38
            resultDict["卦名"] = "睽卦"
            resultDict["组成"] = "火泽睽卦"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水山":
            resultDict["卦序"] = 39
            resultDict["卦名"] = "蹇卦"
            resultDict["组成"] = "水山蹇"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷水":
            resultDict["卦序"] = 40
            resultDict["卦名"] = "解卦"
            resultDict["组成"] = "雷水解"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山泽":
            resultDict["卦序"] = 41
            resultDict["卦名"] = "损卦"
            resultDict["组成"] = "山泽损"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风雷":
            resultDict["卦序"] = 42
            resultDict["卦名"] = "益卦"
            resultDict["组成"] = "风雷益"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽天":
            resultDict["卦序"] = 43
            resultDict["卦名"] = "夬卦"
            resultDict["组成"] = "泽天夬"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "天风":
            resultDict["卦序"] = 44
            resultDict["卦名"] = "姤卦"
            resultDict["组成"] = "天风姤"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽地":
            resultDict["卦序"] = 45
            resultDict["卦名"] = "萃卦"
            resultDict["组成"] = "泽地萃"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "地风":
            resultDict["卦序"] = 46
            resultDict["卦名"] = "升卦"
            resultDict["组成"] = "地风升"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽水":
            resultDict["卦序"] = 47
            resultDict["卦名"] = "困卦"
            resultDict["组成"] = "泽水困"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "水风":
            resultDict["卦序"] = 48
            resultDict["卦名"] = "井卦"
            resultDict["组成"] = "水风井"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽火":
            resultDict["卦序"] = 49
            resultDict["卦名"] = "革卦"
            resultDict["组成"] = "泽火革"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火风":
            resultDict["卦序"] = 50
            resultDict["卦名"] = "鼎卦"
            resultDict["组成"] = "火风鼎"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷雷":
            resultDict["卦序"] = 51
            resultDict["卦名"] = "震卦"
            resultDict["组成"] = "震为雷"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "山山":
            resultDict["卦序"] = 52
            resultDict["卦名"] = "艮卦"
            resultDict["组成"] = "艮为山"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风山":
            resultDict["卦序"] = 53
            resultDict["卦名"] = "渐卦"
            resultDict["组成"] = "风山渐"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷泽":
            resultDict["卦序"] = 54
            resultDict["卦名"] = "归妹卦"
            resultDict["组成"] = "雷泽归妹"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "雷火":
            resultDict["卦序"] = 55
            resultDict["卦名"] = "丰卦"
            resultDict["组成"] = "雷火丰"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "火山":
            resultDict["卦序"] = 56
            resultDict["卦名"] = "旅卦"
            resultDict["组成"] = "火山旅"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "风风":
            resultDict["卦序"] = 57
            resultDict["卦名"] = "巽卦"
            resultDict["组成"] = "巽为风"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"

        if self.gua_group == "泽泽":
            resultDict["卦序"] = 58
            resultDict["卦名"] = "兑卦"
            resultDict["组成"] = "兑为泽"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "风水":
            resultDict["卦序"] = 59
            resultDict["卦名"] = "涣卦"
            resultDict["组成"] = "风水涣"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "水泽":
            resultDict["卦序"] = 60
            resultDict["卦名"] = "节卦"
            resultDict["组成"] = "水泽节"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "风泽":
            resultDict["卦序"] = 61
            resultDict["卦名"] = "中孚卦"
            resultDict["组成"] = "风泽中孚"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "雷山":
            resultDict["卦序"] = 62
            resultDict["卦名"] = "小过卦"
            resultDict["组成"] = "雷山小过"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "水火":
            resultDict["卦序"] = 63
            resultDict["卦名"] = "既济卦"
            resultDict["组成"] = "水火既济"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        if self.gua_group == "火水":
            resultDict["卦序"] = 64
            resultDict["卦名"] = "未济卦"
            resultDict["组成"] = "火水未济"
            resultDict["结构"] = self.up_name + "上" + self.down_name + "下"
        return resultDict

    def printInfo(self):
        print(f"爻的数字结果：{self.n3}")
        print(f"上卦数字结果：{self.n2}")
        print(f"下卦数字结果：{self.n1}")

        print(f"结果为：{self.gua_group}   {self.up_name}上{self.down_name}下")

        print(self.result())


if __name__ == '__main__':
    n64 = NumberTo64(257, 589, 568)
    n64.printInfo()
