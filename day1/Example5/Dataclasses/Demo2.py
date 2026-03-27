from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    api_key: str

c = Config("XYZ123")

print(c) # Config(api_key='XYZ123')

c.api_key = "PQR456"

print(c) 
# dataclasses.FrozenInstanceError: cannot assign 
# to field 'api_key'
# if @dataclass(frozen=False) then it will 
# print Config(api_key='PQR456')




