from fastapi import HTTPException, status


class UserExistsException(HTTPException):
    def __init__(self, detail: str = 'User already exists', status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


class InvalidCredentialsException(HTTPException):
    def __init__(self, detail: str = 'Invalid credentials', status_code: int = 401):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers={"WWW-Authenticate": "Bearer"})


class ExternalAPIException(HTTPException):
    def __init__(self, detail: str = 'Failed to process the request', status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


class InvalidCurrencyException(HTTPException):
    def __init__(self, detail: str = 'Invalid currency code', status_code: int = 404):
        super().__init__(status_code=status_code, detail=detail)
