class DisjointSet:
    def __init__(self):
        self.parents = dict()
        self.email_to_person = dict()
        self.ranks = dict()
    
    def add_person(self, info_list):
        name = info_list[0]
        for i in range(1, len(info_list)):
            self.email_to_person[info_list[i]] = name
            if info_list[i] not in self.parents:
                self.parents[info_list[i]] = info_list[i]
                self.ranks[info_list[i]] = 0
            self.union(info_list[1], info_list[i])
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.ranks[x] > self.ranks[y]:
                self.parents[y] = self.parents[x]
                self.ranks[x] = self.ranks[y]
            elif self.ranks[x] == self.ranks[y]:
                self.parents[y] = self.parents[x]
                self.ranks[x] += 1
                self.ranks[y] += 1
            else:
                self.parents[x] = self.parents[y]
                self.ranks[y] = self.ranks[x]
                 
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet()
        for info_list in accounts:
            ds.add_person(info_list)
        
        results = []
        groups = dict()
        num_groups = 0
        for email in ds.email_to_person:
            pa = ds.find(email)
            if pa in groups:
                results[groups[pa]].append(email)
            else:
                groups[pa] = num_groups 
                num_groups += 1
                results.append([ds.email_to_person[pa], email])
                
        results = [[name, *sorted(emails)] for name, *emails in results]
        return results
            
            
            
            