class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        # [1] find if next path is word or ".."
        for next in path.split("/"):
            if next == "" or next == ".":
                continue
            # [1-1] if ".." -> pop to go upper folder
            elif next == "..":
                if len(answer):
                    answer.pop()
            # [1-2] if word -> go to /next
            else:
                answer.append("/" + next)
        # [2] In case of root path, return "/"
        return "".join(answer) if len(answer) else "/"