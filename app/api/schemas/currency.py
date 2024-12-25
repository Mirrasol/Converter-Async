from Pydantic import BaseModel


class Currencies(BaseModel):
    from_currency:
    to_currency:
    amount: float
