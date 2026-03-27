from typing import Optional, Union, List, Dict, Literal

# Optional → value can be None
def get_user(name: Optional[str]) -> str:
    return name or "Guest"

# Union → multiple allowed types
def process(value: Union[int, str]) -> str:
    return str(value)

# List
def get_items() -> List[int]:
    return [1, 2, 3]

# Dict
def get_user_map() -> Dict[str, int]:
    return {"age": 25}

# Literal → restrict values (very useful in APIs)
def set_status(status: Literal["success", "error"]) -> None:
    print(status)