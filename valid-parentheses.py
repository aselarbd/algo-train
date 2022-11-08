from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        valid = True
        open_brackets = ('(', '{', '[')
        bracket_match = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if stack:
                    if stack.pop() != bracket_match[char]:
                        valid = False
                        break
                else:
                    valid = False
                    break

        if stack:
            valid = False

        return valid


if __name__ == '__main__':
    s = "()[]{}"
    answer = Solution().isValid(s=s)
    print(answer)
