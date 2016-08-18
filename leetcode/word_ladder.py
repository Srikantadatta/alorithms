__author__ = 'srikanta'
import unittest

class Solution:
    def word_ladder(self,start,end,list):
        visited, q = [], []
        path_len, path = 1, [start]
        q.append((start,path_len,path))
        while q:
            cur,path_len,_ = q.pop(0)
            visited.append(cur)
            for e in self.get_elements(cur,list,visited):
                q.append((e,path_len+1,path.append(e)))
                if len(set(e).intersection(set(end)))== 2:
                    path.append(end)
                    return path_len+2, path
        return -1

    def get_elements(self, cur,list,visited):
        return filter(lambda x: x not in visited and len(set(x).intersection(set(cur)))== 2,list)

start = "hit"
end = "cog"
dic = ["hot","dot","dog","lot","log"]
print Solution().word_ladder(start,end,dic)
