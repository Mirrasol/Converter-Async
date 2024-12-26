from Pydantic import BaseModel


class Currencies(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = 1
