class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        logs = sorted(zip(timestamp, username, website))

        visits = defaultdict(list)
        for time, user, site in logs:
            visits[user].append(site)

        counts = Counter()
        for user, sites in visits.items():
            for pattern in set(combinations(sites, 3)):
                counts[pattern] += 1

        best = max(sorted(counts), key=counts.get)
        return list(best)