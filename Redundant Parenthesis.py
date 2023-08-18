'''
Title     : Redundant Parenthesis
Author    : Asmit Singh
Solved On   : 18 Aug 2023
Solved Using   : Python3
'''

from collections import defaultdict
class Solution:
    def removeBrackets(self, s: str) -> str:
        c, n, p, mark = list(s), len(s), [float('inf')] * len(s), [0] * len(s)
        prior = defaultdict(int, {'/': 1, '*': 1, '-': 0, '+': 0, '(': 2})
        num, op, par = [], [], []

        i = 0
        while i < n:
            char = c[i]
            if char != ')' and char not in prior:
                num.append(str(char))
            else:
                if char == ')':
                    while c[op[-1]] != '(':
                        Operator = c[op.pop()]
                        operand1 = num.pop()
                        operand2 = num.pop()
                        res = operand1 + Operator + operand2
                        p[par[-1]] = min(p[par[-1]], prior[Operator])
                        num.append(res)
                    op.pop()

                    next_char = c[i+1] if i+1 < n else prior.get('~', -1)
                    stack_top = c[op[-1]] if op and c[op[-1]
                                                      ] != '(' else prior.get('~', -1)

                    if (next_char in prior and prior[next_char] > p[par[-1]]) or (stack_top != '(' and prior[stack_top] > p[par[-1]]):
                        mark[par[-1]] += 1
                        mark[i] += 1

                    if ('-' in (next_char, stack_top)) and p[par[-1]] == 0:
                        mark[par[-1]] += 1
                        mark[i] += 1

                    if ('/' in (next_char, stack_top)) and p[par[-1]] == 1:
                        mark[par[-1]] += 1
                        mark[i] += 1

                    if op and c[op[-1]] == '(':
                        p[op[-1]] = p[par[-1]]
                    par.pop()

                else:
                    if char == '(':
                        op.append(i)
                        par.append(i)
                    else:
                        if not op or prior[char] > prior[c[op[-1]]] or c[op[-1]] == '(':
                            op.append(i)
                        else:
                            Operator = c[op.pop()]
                            operand1 = num.pop()
                            operand2 = num.pop()
                            res = operand1 + Operator + operand2
                            num.append(res)
                            i -= 1
            i += 1

        while op:
            Operator = c[op.pop()]
            operand1 = num.pop()
            operand2 = num.pop()
            res = operand1 + Operator + operand2
            num.append(res)
        ans = ""

        for i in range(n):
            if mark[i] != 0 and (c[i] == '(' or c[i] == ')'):
                ans += c[i]
            elif c[i] != '(' and c[i] != ')':
                ans += c[i]

        return ans

# I already solved this problem on 25 Mar 2023 using C++. But I solved it again using Python3 on 18 Aug 2023.