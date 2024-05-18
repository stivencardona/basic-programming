from random import randint

memo = {}

for _ in range(1000000):
    professional_id = randint(1, 2999)
    appointment_id = randint(1, 499999)
    
    if professional_id in memo:
        if not appointment_id in memo[professional_id]:
            print(f'{professional_id}, {appointment_id}')
            memo[professional_id][appointment_id] = True
    else:
        print(f'{professional_id}, {appointment_id}')
        memo[professional_id] = { appointment_id: True }