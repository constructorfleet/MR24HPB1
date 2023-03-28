import dataclasses

from construct import Const, Int16un, Int8un, Bytes, Select, Float16l
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
class PassiveSystemReport(DataclassMixin):
    sys_report: int = csfield(Const(b"\04"))
    package: dict = csfield(
        Select(
            DataclassStruct(Threshold),
            DataclassStruct(Scene),
            DataclassStruct(ForceUnoccupied)
        ))

@dataclasses.dataclass
class BodyParameters(DataclassMixin):
    movement: int = csfield(Const(b"\06"))
    energy: float = csfield(Float16l)


@dataclasses.dataclass
class EnvironmentStatus(DataclassMixin):
    environment: int = csfield(Const(b"\05"))
    occupied: bool = csfield(Int8un)
    motion: bool = csfield(Int8un)
    _unused: int = csfield(Int8un)

@dataclasses.dataclass
class PassiveSensorReport(DataclassMixin):
    sensor_report: int = csfield(Const(b"\03"))
    status: dict = csfield(
        Select(
            DataclassStruct(EnvironmentStatus),
            DataclassStruct(BodyParameters)
        ))

@dataclasses.dataclass
class DeviceID(DataclassMixin):
    _attribute: int = csfield(Const(b"\01"))
    device_id: int = csfield(Bytes(12))

@dataclasses.dataclass
class SoftwareVersion(DataclassMixin):
    _attribute: int = csfield(Const(b"\02"))
    software_version: int = csfield(Bytes(15))


@dataclasses.dataclass
class HardwareVersion(DataclassMixin):
    _attribute: int = csfield(Const(b"\03"))
    hardware_version: int = csfield(Bytes(8))

@dataclasses.dataclass
class ProtocolVersion(DataclassMixin):
    _attribute: int = csfield(Const(b"\04"))
    protocol_version: int = csfield(Bytes(8))


@dataclasses.dataclass
class PassiveModuleReport(DataclassMixin):
    module_report: int = csfield(Const(b"\01"))
    attribute: dict = csfield(
        Select(
            DataclassStruct(DeviceID),
            DataclassStruct(SoftwareVersion),
            DataclassStruct(HardwareVersion),
            DataclassStruct(ProtocolVersion)
        ))


@dataclasses.dataclass
class PassiveReportFrame(DataclassMixin):
    passive_report: int = csfield(Const(b"\x03"))
    report: dict = csfield(
        Select(
            DataclassStruct(PassiveModuleReport),
            DataclassStruct(PassiveSensorReport),
            DataclassStruct(PassiveSystemReport)
        ))
