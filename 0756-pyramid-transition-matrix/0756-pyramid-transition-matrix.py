import collections


class Solution:

  def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
    # Map every 2-letter pair to its possible top blocks
    prefixToBlocks = collections.defaultdict(list)
    for a in allowed:
      prefixToBlocks[a[:2]].append(a[2])

    def dfs(row: str, nextRow: str, i: int) -> bool:
      # Base case: reached the top of the pyramid
      if len(row) == 1:
        return True

      # If the current layer is finished, move up to the next level
      if len(nextRow) + 1 == len(row):
        return dfs(nextRow, '', 0)

      # Try all valid blocks that can be placed on top of the current pair
      for c in prefixToBlocks[row[i : i + 2]]:
        if dfs(row, nextRow + c, i + 1):
          return True

      return False

    return dfs(bottom, '', 0)