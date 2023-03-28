import dataclasses

from construct import Const, Int16un, Int8un, Bytes, Select, Float16l, Float16n, Float32n
from construct_typed import DataclassMixin, csfield, DataclassStruct, EnumBase, TEnum


class Direction(EnumBase):
    STATIONARY = 1
    APPROACHING = 2
    RETREATING = 3
    STILL_APPROACHING = 4
    STILL_RETREATING = 5


@dataclasses.dataclass
class ApproachAway(DataclassMixin):
    approach_away: int = csfield(Const(b"\07"))
    _unused: int = csfield(Int16un)
    value: Direction = csfield(TEnum(Int8un, Direction))


@dataclasses.dataclass
class BodyParameters(DataclassMixin):
    movement: int = csfield(Const(b"\06"))
    energy: float = csfield(Float32n)


@dataclasses.dataclass
class EnvironmentStatus(DataclassMixin):
    environment: int = csfield(Const(b"\05"))
    occupied: bool = csfield(Int8un)
    motion: bool = csfield(Int8un)
    _unused: int = csfield(Int8un)


@dataclasses.dataclass
class Heartbeat(DataclassMixin):
    heartbeat: int = csfield(Const(b"\01"))
    occupied: bool = csfield(Int8un)
    breathing: bool = csfield(Int8un)
    _unused: int = csfield(Int8un)


@dataclasses.dataclass
class ActiveOtherReport(DataclassMixin):
    other_report: int = csfield(Const(b"\05"))
    package: dict = csfield(DataclassStruct(Heartbeat))


@dataclasses.dataclass
class ActiveSensorReport(DataclassMixin):
    sensor_report: int = csfield(Const(b"\03"))
    status: dict = csfield(
        Select(
            DataclassStruct(BodyParameters),
            DataclassStruct(EnvironmentStatus),
            DataclassStruct(ApproachAway)
        ))


@dataclasses.dataclass
class SoftwareVersionReport(DataclassMixin):
    attribute: int = csfield(Const(b"\02"))
    software_version: int = csfield(Bytes(15))


@dataclasses.dataclass
class ActiveModuleReport(DataclassMixin):
    module_report: int = csfield(Const(b"\01"))
    attribute: dict = csfield(DataclassStruct(SoftwareVersionReport))


@dataclasses.dataclass
class ActiveReportFrame(DataclassMixin):
    active_report: int = csfield(Const(b"\x04"))
    report: dict = csfield(
        Select(
            DataclassStruct(ActiveModuleReport),
            DataclassStruct(ActiveSensorReport),
            DataclassStruct(ActiveOtherReport)
        ))
