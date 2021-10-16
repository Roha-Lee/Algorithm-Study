import hashlib
import sys 
input = sys.stdin.readline
query = input().rstrip()
print(hashlib.sha256(query.encode()).hexdigest())