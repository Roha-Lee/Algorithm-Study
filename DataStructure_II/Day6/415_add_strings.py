class Solution:
    def add_digit(self, num1, num2, flow):
        res = num1 + num2 + flow
        flow = 0
        if res > 9:
            res -= 10
            flow = 1
        return res, flow

    def remove_leading_zero(self, num):
        flag = num[0] == '0'
        if flag:
            for idx, elem in enumerate(num[1:],1):
                if not elem == '0':
                    return num[idx:]
            return '0'
        else:
            return num

    def addStrings(self, num1: str, num2: str) -> str:
        string_list = ['0','1','2','3','4','5','6','7','8','9']
        result = []
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2) + 1) +  num2
            num1 = '0' + num1
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1) + 1) +  num1
            num2 = '0' + num2
        if len(num1) == len(num2):
            num1 = '0' + num1
            num2 = '0' + num2

        num1_list = list(num1)
        num2_list = list(num2)
        num1_list.reverse()
        num2_list.reverse()
        flow = 0
        for elem1, elem2 in zip(num1_list, num2_list):
            elem1 = string_list.index(elem1)
            elem2 = string_list.index(elem2)
            res, flow = self.add_digit(elem1, elem2, flow)
            result.insert(0, string_list[res])
        return self.remove_leading_zero(''.join(result))

