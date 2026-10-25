class Solution:
    def unionArray(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        result = []
        i = 0
        j = 0
        while i < n and j < m:
            if nums1[i] <=nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i+=1

            else:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j+=1
            
        while i < n:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i+=1

        while  j < m:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])  
                j+=1 

        return result 
