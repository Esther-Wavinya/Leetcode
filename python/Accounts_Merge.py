# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


# Example 1:
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

# Example 2:
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


# Constraints:
#     1 <= accounts.length <= 1000
#     2 <= accounts[i].length <= 10
#     1 <= accounts[i][j].length <= 30
#     accounts[i][0] consists of English letters.
#     accounts[i][j] (for j > 0) is a valid email.

# To merge the given list of accounts, we can use a graph-based approach. We can create a graph where each node represents an email and each edge between two nodes indicates that the two emails belong to the same account. We can then traverse the graph to find all connected components, which represent all the merged accounts. For each connected component, we can extract the account name and all the associated emails, sort the emails, and add the resulting list to the output.

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                for j in range(i + 1, len(emails)):
                    graph[emails[i]].append(emails[j])
                    graph[emails[j]].append(emails[i])

        # Traverse the graph to find all connected components
        visited = set()
        output = []
        for email in graph:
            if email not in visited:
                # Start a new connected component
                visited.add(email)
                stack = [email]
                component = [email]
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                            component.append(neighbor)
                # Sort and add the component to the output
                output.append([name] + sorted(component))

        return output

# The time complexity of this solution is O(n^2), where n is the total number of emails in all accounts. The space complexity is also O(n^2), since we store the adjacency list and the visited set.
