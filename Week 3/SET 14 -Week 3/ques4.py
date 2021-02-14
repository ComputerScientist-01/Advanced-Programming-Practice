class ques4:
   def __init__(self) -> None:
       pass

   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

obj = ques4()
s = input()
ans = obj.is_valid_parenthese(s)
print(ans)