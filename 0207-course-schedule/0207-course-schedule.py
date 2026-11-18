class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        remaining = [0] * numCourses
        next_courses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            remaining[course] += 1
            next_courses[prereq].append(course)

        ready = deque()
        for course in range(numCourses):
            if remaining[course] == 0:
                ready.append(course)

        finished = 0

        while ready:
            course = ready.popleft()
            finished += 1

            for next_course in next_courses[course]:
                remaining[next_course] -= 1
                if remaining[next_course] == 0:
                    ready.append(next_course)

        return finished == numCourses
        