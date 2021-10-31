record = dict(rec.split() for rec in input("Enter name and marks").split(","))
def based_on_marks(record):
    return record[1]
#Method1: result = dict(sorted(record.items(),key = based_on_marks))
#Method2:
result = dict(sorted(record.items(),key = lambda record:record[1]))
print(result)
"""
lambda:
lambda record:record[1]
accept a parameter:return
"""