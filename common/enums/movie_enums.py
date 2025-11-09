from enum import Enum, auto

class MovieOperations(Enum):
    ADD = auto()
    UPDATE = auto()
    DELETE = auto()
    FIND_BY_TITLE = auto()
    FIND_BY_AGE_LIMIT = auto()
    FIND_BY_AGE_LIMIT_LOWER_THAN = auto()
    FIND_BY_AGE_LIMIT_LOWER_THAN_OR_EQUALS = auto()
    FIND_BY_AGE_LIMIT_GREATER_THAN = auto()
    FIND_BY_AGE_LIMIT_GREATER_THAN_OR_EQUALS = auto()
    DEFAULT = auto

class AgeLimit(Enum):
    AGE_3 = 3
    AGE_6 = 6
    AGE_12 = 12
    AGE_13 = 13
    AGE_16 = 16
    AGE_17 = 17
    AGE_18 = 18
