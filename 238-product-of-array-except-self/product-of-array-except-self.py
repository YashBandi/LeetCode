class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        c = 0
        if nums[0]==nums[1]==0:
            ans0 = 0
        else:
            ans0 = 1
        l = []
        answer = []
        for i in range(len(nums)):
            ans = ans * nums[i]
            i += 1
        #print(ans)
        if ans!=0:
            for i in range(len(nums)):  
                answer = l.append(ans//nums[i])   
                #print(l)
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    c += 1
            #print(c)
            if c > 1:
                for i in range(len(nums)):  
                        answer = l.append(0)
                        i += 1

            else:
                if c == 1:
                    for i in range(len(nums)):    
                        if nums[i]!=0:
                            ans0 = ans0 * nums[i]
                            i += 1
                            print(ans0)
                for i in range(len(nums)):
                    if nums[i]!=0:  
                        answer = l.append(0)
                        i += 1
                    else:
                        answer = l.append(ans0)
                        i +=1  
                #print(l)

        return l

