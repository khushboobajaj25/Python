ut1_record= dict(x.split() for x in input("Enter ut1 marks").split(","))
ut2_record = dict(x.split() for x in input("Enter ut2 marks").split(","))
ut1_record.update(ut2_record)
print(ut1_record)