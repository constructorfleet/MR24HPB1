import dataclasses
from typing import Dict, Any

from construct import Const, Int8ub, Int16ub, Select
from construct_typed import DataclassMixin, csfield, DataclassStruct, EnumBase, TEnum


@dataclasses.dataclass
class Nightlight(DataclassMixin):
    _night_light: int = csfield(Const(b"\x12"))
    night_light_on: bool = csfield(Int8ub)
    brightness: int = csfield(Int8ub)


@dataclasses.dataclass
class Time(DataclassMixin):
    hour: int = csfield(Int8ub)
    minute: int = csfield(Int8ub)


@dataclasses.dataclass
class Display(DataclassMixin):
    _display: int = csfield(Const(b"\x10"))
    display_active: bool = csfield(Int8ub)
    start: Dict = csfield(Time)
    end: Dict = csfield(Time)


@dataclasses.dataclass
class Timer(DataclassMixin):
    _timer: int = csfield(Const(b"\x0b"))
    timer_active: bool = csfield(Int8ub)
    timer_duration: int = csfield(Int16ub)


@dataclasses.dataclass
class Controls(DataclassMixin):
    _controls_state: int = csfield(Const(b"\x0a"))
    controls_locked: bool = csfield(Int8ub)


class FanSpeed(EnumBase):
    NIGHT = 0x10
    LOW = 0x01
    MEDIUM = 0x02
    HIGH = 0x03


@dataclasses.dataclass
class Fan(DataclassMixin):
    _fan_state: int = csfield(Const(b"\x05"))
    fan_speed: FanSpeed = csfield(TEnum(Int8ub, FanSpeed))


@dataclasses.dataclass
class Active(DataclassMixin):
    _active_state: int = csfield(Const(b"\x01"))
    is_active: bool = csfield(Int8ub)


@dataclasses.dataclass
class Report(DataclassMixin):
    report: int = csfield(Const(b"\xAA"))
    state: Any = csfield(
        Select(DataclassStruct(Active),
               DataclassStruct(Fan),
               DataclassStruct(Controls),
               DataclassStruct(Timer),
               DataclassStruct(Display),
               DataclassStruct(Nightlight)))
