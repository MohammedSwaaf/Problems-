class add:
    def sum(self,nums,target):
        list={}
        for i,j in enumerate(nums):
            if j in list:
                return list[j],i
            else:
                list[target-j]=i
        return []
obj=add([2,7,11,15],9)
add.sum()

def run():
    nums=[5,1,5,3,4]
    target=9
    obj=add()
    print(obj.sum(nums=nums,target=target))
if __name__ == "__main__":
    run()
