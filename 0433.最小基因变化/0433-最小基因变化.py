from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque()
        q.append([start, 0])
        visited = set()
        char = "ACGT"
        while q: #开始BFS
            cur, cnt = q.popleft() #取一个出来
            if cur == end: #如果找到了
                return cnt
            
            for i in range(len(cur)):
                for j in range(4):
                    new = cur[:i] + char[j] + cur[i + 1:] #生成从当前基因可以变换到的新基因
                    
                    if new in bank and new not in visited: #如果新基因有效
                        visited.add(new)
                        q.append([new, cnt + 1])
                        
        return -1
            