const twoSum = (nums, target) => {
  const prevNums = {};                         // 存放出现过的数字，和对应的索引
  for (let i = 0; i < nums.length; i++) {      // 遍历每一项
    const curNum = nums[i];                    // 当前项
    const targetNum = target - curNum;         // 希望从过去的数字中找到的呼应项
    const targetNumIndex = prevNums[targetNum];// 在prevNums中找targetNum的索引
    if (targetNumIndex !== undefined) {        // 如果能找到
      return [targetNumIndex, i];              // 直接返回targetNumIndex和当前的i
    }                                          // 如果找不到，说明之前没出现过targetNum
    prevNums[curNum] = i;                      // 往prevNums存当前curNum和对应的i
  }
}