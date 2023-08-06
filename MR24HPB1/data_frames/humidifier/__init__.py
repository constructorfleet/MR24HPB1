import dataclasses
from typing import Dict, Any

from construct import Const, Int8ub, Int16ub, Select
from construct_typed import DataclassMixin, csfield, DataclassStruct


@dataclasses.dataclass
class Timer(DataclassMixin):
    _timer: int = csfield(Const(b"\x0b"))
    timer_active: bool = csfield(Int8ub)
    timer_duration: int = csfield(Int16ub)


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
class Controls(DataclassMixin):
    _controls_state: int = csfield(Const(b"\x0a"))
    controls_locked: bool = csfield(Int8ub)


@dataclasses.dataclass
class ContinuousProgram(DataclassMixin):
    mist_level: int = csfield(Int8ub)
    duration: int = csfield(Const(b"\xFF\xFF"))
    remaining: int = csfield(Const(b"\xFF\xFF"))


@dataclasses.dataclass
class Program(DataclassMixin):
    mist_level: int = csfield(Int8ub)
    duration: int = csfield(Int16ub)
    remaining: int = csfield(Int16ub)


@dataclasses.dataclass
class ProgramMode(DataclassMixin):
    program: int = csfield(Const(b"\x02"))
    active_program_id: int = csfield(Int8ub)
    program0: Dict = csfield(DataclassStruct(Program))
    program1: Dict = csfield(DataclassStruct(Program))
    continuous: Dict = csfield(DataclassStruct(ContinuousProgram))
    # active_program: Dict =


@dataclasses.dataclass
class SimpleMode(DataclassMixin):
    simple: int = csfield(Const(b"\x01"))
    mist_level: int = csfield(Int8ub)


@dataclasses.dataclass
class DefaultMode(DataclassMixin):
    default: int = csfield(Const(b"\x00"))


@dataclasses.dataclass
class Mode(DataclassMixin):
    _mode: int = csfield(Const(b"\x05"))
    mode: Dict = csfield(
        Select(
            DataclassStruct(DefaultMode),
            DataclassStruct(SimpleMode),
            DataclassStruct(ProgramMode)))


@dataclasses.dataclass
class Active(DataclassMixin):
    _active_state: int = csfield(Const(b"\x01"))
    is_active: bool = csfield(Int8ub)


@dataclasses.dataclass
class Report(DataclassMixin):
    report: int = csfield(Const(b"\xAA"))
    state: Any = csfield(
        Select(DataclassStruct(Active),
               DataclassStruct(Mode),
               DataclassStruct(Controls),
               DataclassStruct(Timer),
               DataclassStruct(Display),
               DataclassStruct(Nightlight)))
