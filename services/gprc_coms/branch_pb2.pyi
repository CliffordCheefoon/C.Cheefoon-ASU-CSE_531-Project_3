# pylint: skip-file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class event_type_enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEPOSIT: _ClassVar[event_type_enum]
    WITHDRAW: _ClassVar[event_type_enum]
    QUERY: _ClassVar[event_type_enum]
DEPOSIT: event_type_enum
WITHDRAW: event_type_enum
QUERY: event_type_enum

class branchEventRequest(_message.Message):
    __slots__ = ["event_id", "customer_id", "event_type", "money", "is_propogate"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    IS_PROPOGATE_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    customer_id: int
    event_type: event_type_enum
    money: float
    is_propogate: bool
    def __init__(self, event_id: _Optional[int] = ..., customer_id: _Optional[int] = ..., event_type: _Optional[_Union[event_type_enum, str]] = ..., money: _Optional[float] = ..., is_propogate: bool = ...) -> None: ...

class branchEventResponse(_message.Message):
    __slots__ = ["event_id", "event_type", "money", "balance", "is_success", "write_id"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WRITE_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_type: event_type_enum
    money: float
    balance: float
    is_success: bool
    write_id: int
    def __init__(self, event_id: _Optional[int] = ..., event_type: _Optional[_Union[event_type_enum, str]] = ..., money: _Optional[float] = ..., balance: _Optional[float] = ..., is_success: bool = ..., write_id: _Optional[int] = ...) -> None: ...
