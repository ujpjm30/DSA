class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log):
            id_, rest = log.split(' ', 1)

            if rest[0].isalpha():
                return (0, rest, id_)
            else:
                return (1,)
        logs.sort(key=key)

        return logs
        