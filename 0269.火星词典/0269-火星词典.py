class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import defaultdict, deque

        indegree = defaultdict(int)
        children = defaultdict(set)
        all_chars = set()
        for word in words:
            for ch in word:
                all_chars.add(ch)
        
        for i in range(1, len(words)):
            # find the first different char in words[i] and words[i - 1]
            j = 0
            while j < len(words[i]) and j < len(words[i - 1]):
                if words[i][j] != words[i - 1][j]:
                    if words[i][j] not in children[words[i - 1][j]]:
                        indegree[words[i][j]] += 1
                        children[words[i - 1][j]].add(words[i][j])
                    break
                if j == len(words[i]) - 1 and j < len(words[i - 1]) - 1:
                    return ""
                j += 1
           
        # t -> f, w -> e, r -> t, e -> r
        queue = deque()
        # print (indegree)
        # print (children)
        for ch in all_chars:
            if indegree[ch] == 0:
                    queue.append(ch)
        # print (queue)
        res = ""
        while queue:
            cur = queue.popleft()

            res += cur
            for child in children[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return res if len(res) == len(all_chars) else ""

        