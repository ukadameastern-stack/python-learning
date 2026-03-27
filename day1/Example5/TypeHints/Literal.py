from typing import Literal

def update_order(status: Literal["pending", "shipped", "delivered"]):
    print(f"Order is now {status}")

update_order("pending")   
update_order("shipped")   
update_order("Uday")   
update_order(11)   

'''
Order is now pending
Order is now shipped
Order is now Uday
Order is now 11
'''

'''
⚙️ What actually happens in your code
-------------------------------------

    update_order("Uday")
    update_order(11)

Python simply does:

    print(f"Order is now {status}")

👉 No validation, no restriction → it prints whatever you pass.

'''