from typing import Union

def process_payment(amount: Union[int, float]) -> float:
    return float(amount)


print(process_payment(100))
print(process_payment(100.68))

'''
100.0
100.68
'''


def get_user(user_id: int) -> Union[dict, str]:
    if user_id == 1:
        return {"name": "Uday"}
    return "User not found"

print(get_user(1))
print(get_user(12))

'''
{'name': 'Uday'}
User not found
'''


def find_user(user: Union[int, str]):
    if isinstance(user, int):
        print("Search by ID")
    else:
        print("Search by username")

find_user(12)        
find_user("Uday")   


'''
Search by ID
Search by username

'''

