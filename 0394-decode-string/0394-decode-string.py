class Solution(object):
    def decodeString(self, s):
        stack = []
        curr = []
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)         # 숫자 누적

            elif ch == '[':
                stack.append((''.join(curr), k))  # 저장
                curr = []                         # curr 초기화
                k = 0                             # k 초기화

            elif ch == ']':
                prev, repeat = stack.pop()
                curr = [ prev + ''.join(curr) * repeat ]

            else:
                curr.append(ch)    # 문자 추가

        return ''.join(curr)