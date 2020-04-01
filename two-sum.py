def twoSum(nums, target):
        """Given an array of integers, return indices of two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        Example: 
        Give nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        indices = {}
        for idx, num in enumerate(nums):
           indices.setdefault(num, []).append(idx)
        for k, v in indices.items():
            i = v.pop()
            if target - k in indices and indices[target-k]:
                return i, indices[target-k].pop()


    