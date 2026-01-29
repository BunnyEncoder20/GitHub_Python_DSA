class Solution:
    def rotateString(self, s, goal):
        # trivia cases:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False

        doubles = s + s
        return goal in doubles


if __name__ == "__main__":
    print(Solution().rotateString("abcde", "cdeab"))
    print(Solution().rotateString("abcde", "adeac"))
