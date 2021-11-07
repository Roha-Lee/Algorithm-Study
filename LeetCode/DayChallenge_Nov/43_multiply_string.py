class Solution:
    TABLE = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    def multiply(self, num1: str, num2: str) -> str:
        str_list1 = list(num1)
        str_list2 = list(num2)
        str_list1.reverse()
        str_list2.reverse()
        result = ['0' for _ in range(402)]
        dig1_cur = 0
        for dig1 in str_list1:
            dig2_cur = 0
            for dig2 in str_list2:
                ans = self.multiply_digit(dig1, dig2)
                self.put_ans_to_result(ans, result, dig1_cur + dig2_cur)
                dig2_cur += 1
            dig1_cur += 1
        return self.remove_leading_zero(''.join(result))

    def multiply_digit(self, dig1, dig2):
        return list(str(self.TABLE[dig1] * self.TABLE[dig2]))

    def add_digit(self, num1, num2='0', flow=0):
        res = self.TABLE[num1] + self.TABLE[num2] + flow
        flow = 0
        if res > 9:
            res -= 10
            flow = 1
        return str(res), flow

    def put_ans_to_result(self, ans, result, cur):
        ans.reverse()
        flow = 0
        for i in range(len(ans)):
            result[-cur-1-i], flow = self.add_digit(ans[i], result[-cur-1-i], flow)
        flow_idx = len(ans)
        while flow:
            result[-cur-1-flow_idx], flow = self.add_digit(result[-cur-1-flow_idx], flow = flow)
            flow_idx += 1

    def remove_leading_zero(self, num):
        flag = num[0] == '0'
        if flag:
            for idx, elem in enumerate(num[1:],1):
                if not elem == '0':
                    return num[idx:]
            return '0'
        else:
            return num