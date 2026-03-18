"""List of exception names to skip for retries."""

_default_exceptions_to_skip = [
    "BadRequestError",
    "UnsupportedParamsError",
    "ContextWindowExceededError",
    "ContentPolicyViolationError",
    "ImageFetchError",
    "InvalidRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "UnprocessableEntityError",
    "APIConnectionError",
    "APIError",
    "ServiceUnavailableError",
    "APIResponseValidationError",
    "BudgetExceededError",
]
