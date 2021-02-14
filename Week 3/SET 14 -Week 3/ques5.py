class ques5:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

obj = ques5()
arr = [int(x) for x in input().split()]   
ans = obj.sub_sets(arr)
print(ans)

