users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = set(users)

statistic = {"Общее количество": 0, "Уникальные посещения": 0}

statistic["Общее количество"] = len(users)
statistic["Уникальные посещения"] = len(set(users))

print(statistic)
