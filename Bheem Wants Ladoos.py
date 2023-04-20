'''
Title     : Bheem Wants Ladoos
Domain    : ???
Author    : Asmit Singh
Solved On   : 20 Apr 2023
Solved Using   : Python3
'''

class Solution:
    def ladoos(self, root, home, k):
        graph = {}
        self.preOrder(root, graph, None)
        vis = {}
        for i in graph:
            vis[i] = 0
        temp = graph[home]
        vis[home] = 1
        ans = 0
        while (len(temp) > 0 and k > 0):
            k -= 1
            for i in range(len(temp)):
                tempo = temp.pop(0)
                if (tempo != None and vis[tempo] == 0):
                    vis[tempo] = 1
                    ans += tempo
                    temp += graph[tempo]
        return ans+home

    def preOrder(self, root, graph, parent):
        if (root == None):
            return None
        elif (root.data not in graph):
            graph[root.data] = [parent, self.preOrder(
                root.left, graph, root.data), self.preOrder(root.right, graph, root.data)]
        return root.data
