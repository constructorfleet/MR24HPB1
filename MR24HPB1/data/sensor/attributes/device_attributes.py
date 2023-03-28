from construct import Struct, Bytes

device_id = Struct(
    "deviceId" / Bytes(12)
)

software_version = Struct(
    "version" / Bytes(15)
)

hardware_version = Struct(
    "version" / Bytes(8)
)

protocol_version = Struct(
    "version" / Bytes(8)
)
