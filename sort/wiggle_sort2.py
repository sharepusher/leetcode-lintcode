def wiggleSort(nums):
    # Write your code here
    N = len(nums)
    middle = N // 2
    nums.sort(reverse=True)
    nums[::2], nums[1::2] = nums[middle:], nums[:middle]
    return nums

if __name__ == "__main__":
    import dis
    dis.dis(wiggleSort)
