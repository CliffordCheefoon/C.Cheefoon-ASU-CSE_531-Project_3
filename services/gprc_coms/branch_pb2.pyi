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
    query: _ClassVar[event_type_enum]
DEPOSIT: event_type_enum
WITHDRAW: event_type_enum
query: event_type_enum

class branchEventRequest(_message.Message):
    __slots__ = ["id", "event_type", "money"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    event_type: event_type_enum
    money: float
    def __init__(self, id: _Optional[int] = ..., event_type: _Optional[_Union[event_type_enum, str]] = ..., money: _Optional[float] = ...) -> None: ...

class branchEventResponse(_message.Message):
    __slots__ = ["id", "event_type", "money", "balance"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    event_type: event_type_enum
    money: float
    balance: float
    def __init__(self, id: _Optional[int] = ..., event_type: _Optional[_Union[event_type_enum, str]] = ..., money: _Optional[float] = ..., balance: _Optional[float] = ...) -> None: ...
