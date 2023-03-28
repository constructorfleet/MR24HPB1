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

@dataclasses.dataclass
class Scene(DataclassMixin):
    active_scene: int = csfield(Const(b"\10"))

@dataclasses.dataclass
class Threshold(DataclassMixin):
    threshold_gears: int = csfield(Const(b"\0C"))

@dataclasses.dataclass
class SystemInquire(DataclassMixin):
    sys_inquiry: int = csfield(Const(b"\04"))
    package: dict = csfield(
        Select(
            DataclassStruct(Threshold),
            DataclassStruct(Scene),
            DataclassStruct(ForceUnoccupied)
        ))

@dataclasses.dataclass
class BodyParameters(DataclassMixin):
    movement: int = csfield(Const(b"\06"))


@dataclasses.dataclass
class EnvironmentStatus(DataclassMixin):
    environment: int = csfield(Const(b"\05"))

@dataclasses.dataclass
class SensoryInquiry(DataclassMixin):
    sensor_inquiry: int = csfield(Const(b"\03"))
    status: dict = csfield(
        Select(
            DataclassStruct(EnvironmentStatus),
            DataclassStruct(BodyParameters)
        ))

@dataclasses.dataclass
class DeviceID(DataclassMixin):
    device_id: int = csfield(Const(b"\01"))

@dataclasses.dataclass
class SoftwareVersion(DataclassMixin):
    software_version: int = csfield(Const(b"\02"))


@dataclasses.dataclass
class HardwareVersion(DataclassMixin):
    hardware_version: int = csfield(Const(b"\03"))

@dataclasses.dataclass
class ProtocolVersion(DataclassMixin):
    protocol_version: int = csfield(Const(b"\04"))


@dataclasses.dataclass
class ModuleInquire(DataclassMixin):
    module_inquiry: int = csfield(Const(b"\01"))
    attribute: dict = csfield(
        Select(
            DataclassStruct(DeviceID),
            DataclassStruct(SoftwareVersion),
            DataclassStruct(HardwareVersion),
            DataclassStruct(ProtocolVersion)
        ))


@dataclasses.dataclass
class ReadFrame(DataclassMixin):
    read: int = csfield(Const(b"\x01"))
    request: dict = csfield(
        Select(
            DataclassStruct(ModuleInquire),
            DataclassStruct(SensoryInquiry),
            DataclassStruct(SystemInquire)
        ))
