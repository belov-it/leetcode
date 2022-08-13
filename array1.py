
def is_inc(arr: list) -> bool:
    for i in range(1, len(arr)):
        if (arr[i] <= arr[i-1]):
            return False
    return True


def get_idx(arr: list) -> int:
    for i in range(0, len(arr)-1):
        if (arr[i] >= arr[i+1]):
            return i


def canBeIncreasing(nums: list) -> bool:
    if (is_inc(nums)):
        return True
    return is_inc(nums[0:get_idx(nums)]+nums[get_idx(nums)+1:])


nums = [105, 924, 32, 968]
print(canBeIncreasing(nums))

print(nums[0:get_idx(nums)]+nums[get_idx(nums)+1:])
