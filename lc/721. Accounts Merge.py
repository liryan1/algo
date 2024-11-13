class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        visited_accounts = [False] * len(accounts)
        email_to_account: dict[str, list[int]] = {}
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if not account[j] in email_to_account:
                    email_to_account[account[j]] = []
                email_to_account[account[j]].append(i)

        result: list[list[str]] = []

        def dfs(id: int, emails: set[str]):
            stack = [id]
            while stack:
                curr_id = stack.pop()
                if visited_accounts[curr_id]:
                    continue
                visited_accounts[curr_id] = True
                for j in range(1, len(accounts[curr_id])):
                    email = accounts[curr_id][j]
                    emails.add(email)
                    stack.extend(email_to_account[email])

        for i in range(len(accounts)):
            if visited_accounts[i]:
                continue
            name = accounts[i][0]
            emails: set[str] = set()
            dfs(i, emails)
            result.append([name] + sorted(emails))

        return result
