from collections import Counter

str = "Hello, world! QA rocks."
words = str.split()
for w in words[::-1]:
    print(w)
    
    
def count_status(str):
    return dict(Counter(str))
    
print(count_status(["PASS","FAIL","SKIP","PASS","FAIL"]))

def flatten(lst):
    return [x for sub in lst for x in sub]

print(flatten([[1,2],[3],[4,5]]))


from datetime import datetime
def is_valid_date(s):
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False

print(is_valid_date("2024-03-23"))
print(is_valid_date("03-2024-23"))
