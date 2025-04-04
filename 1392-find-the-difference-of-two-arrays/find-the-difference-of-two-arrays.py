class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        ans[0] = list(set(nums1) - set(nums2))
        ans[1] = list(set(nums2) - set(nums1))
        return ans

        # Solution 2: Runtime 577 ms
        # ans = [[],[]]
        # for i in range(len(nums1)):
        #     if nums1[i] not in nums2:
        #         while nums1[i] not in ans[0]:
        #             ans[0].append(nums1[i])
        
        # for j in range(len(nums2)):
        #     if nums2[j] not in nums1:
        #         while nums2[j] not in ans[1]:
        #             ans[1].append(nums2[j])
        
        # return ans
        