from collections import deque
from typing import List

class Solution:
    '''
    你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
    给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

    '''
    '''
    除了这个方法以外可以DFS
    判断拓扑排序有无环
    这个方法没大看懂
    （如果有环就会出现循环等待的情况
    ）
    【
    给定一个包含 n 个节点的有向图 G，我们给出它的节点编号的一种排列，如果满足：
    对于图 G 中的任意一条有向边 (u,v)(u, v)(u,v)，uuu 在排列中都出现在 vvv 的前面。
    那么称该排列是图 G 的「拓扑排序」。
    】
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        拓扑排序先建立每个的入度数组
        然后入队入度为0的节点
        出队一个节点把所有依赖他的节点入度减一

        '''
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses

