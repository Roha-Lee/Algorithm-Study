from queue import Queue
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = Queue()
        queue.put((0, nums[0]))
        visited = [False for _ in nums]
        visited[0] = True
        while not queue.empty():
            cur_idx, power = queue.get()
            if cur_idx == len(nums) - 1:
                return True

            if power == 0:
                if not queue.empty():
                    continue
                else:
                    return False

            else:
                for i in range(1, power+1):
                    if cur_idx + i < len(nums):
                        if not visited[cur_idx + i]:
                            queue.put((cur_idx + i , nums[cur_idx + i]))
                            visited[cur_idx + i] = True
                    else:
                        return True

        return False