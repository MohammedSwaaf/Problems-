class add:
    def sum(self,nums,target):
        list={}
        for i,j in enumerate(nums):
            if j in list:
                return list[j], i
            else:
                list[target-j] = i
        return []
obj=add()
print(obj.sum([2,7,11,15],9))