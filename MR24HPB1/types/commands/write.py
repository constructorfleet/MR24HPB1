import dataclasses

from construct import Const, Int8un, Select
from construct_typed import DataclassMixin, csfield, DataclassStruct, EnumBase, TEnum


class Scene(EnumBase):
    DEFAULT = 0
    AREA = 1
    BATHROOM = 2
    BEDROOM = 3
    LIVING_ROOM = 4
    OFFICE = 5
    HOTEL = 6


class ForceUnoccupied(EnumBase):
    SECONDS_0 = 0
    SECONDS_10 = 1
    SECONDS_30 = 2
    SECONDS_60 = 3
    SECONDS_120 = 4
    SECONDS_300 = 5
    SECONDS_600 = 6
    SECONDS_1800 = 7
    SECONDS_3600 = 8


@dataclasses.dataclass
class ForceUnoccupied(DataclassMixin):
    force_unoccupied: int = csfield(Const(b"\12"))
    time: ForceUnoccupied = csfield(TEnum(Int8un, ForceUnoccupied))


@dataclasses.dataclass
class Scene(DataclassMixin):
    active_scene: int = csfield(Const(b"\10"))
    scene: Scene = csfield(TEnum(Int8un, Scene))


@dataclasses.dataclass
class Threshold(DataclassMixin):
    threshold_gears: int = csfield(Const(b"\0C"))
    threshold: int = csfield(Int8un)


@dataclasses.dataclass
class SystemWrite(DataclassMixin):
    sys_report: int = csfield(Const(b"\04"))
    package: dict = csfield(
        Select(
            DataclassStruct(Threshold),
            DataclassStruct(Scene),
            DataclassStruct(ForceUnoccupied)
        ))


@dataclasses.dataclass
class WriteFrame(DataclassMixin):
    write: int = csfield(Const(b"\x02"))
    command: dict = csfield(
        Select(
            DataclassStruct(SystemWrite),
        ))
