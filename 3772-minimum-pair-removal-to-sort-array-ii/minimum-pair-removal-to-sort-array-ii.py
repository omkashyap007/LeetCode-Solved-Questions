from sortedcontainers import SortedSet

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        min_pair_set = SortedSet()
        next_index = [i+1 for i in range(n)]
        prev_index = [i-1 for i in range(n)]

        bad_pairs = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                bad_pairs += 1
            min_pair_set.add((nums[i] + nums[i+1],  i))
        ops = 0
        while bad_pairs > 0:
            pair_sum, first = min_pair_set.pop(0)
            second = next_index[first]
 
            first_left = prev_index[first]
            second_right = next_index[second]

            if nums[first] > nums[second]:
                bad_pairs -= 1
            
            if first_left >= 0:
                if (
                    nums[first_left] > nums[first] and
                    nums[first_left] <= nums[first] + nums[second]
                ):
                    bad_pairs -= 1
                elif (
                    nums[first_left] <= nums[first] and
                    nums[first_left] > nums[first] + nums[second]
                ):
                    bad_pairs += 1

            if second_right < n:
                if (
                    nums[second_right] >= nums[second] and
                    nums[second_right] < nums[first] + nums[second]
                ):
                    bad_pairs += 1
                elif (
                    nums[second_right] < nums[second] and
                    nums[second_right] >= nums[first] + nums[second]
                ):
                    bad_pairs -= 1

            if first_left >= 0:
                min_pair_set.discard((nums[first_left]+nums[first], first_left))
                min_pair_set.add((nums[first_left]+ nums[first] + nums[second], first_left))
            
            if second_right < n:
                min_pair_set.discard((nums[second] + nums[second_right], second))
                min_pair_set.add((nums[first] + nums[second] + nums[second_right], first))
                prev_index[second_right] = first

            next_index[first] = second_right
            nums[first] += nums[second]
            ops += 1
        return ops
