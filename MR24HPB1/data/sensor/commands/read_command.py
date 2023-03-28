from construct import Struct, Int8un, Enum, Switch

from MR24HPB1.types.const import DEVICE_INFO

read_device_identification = Struct(
    "attribute" / Enum(Int8un,
                       DEVICE_ID=0x01,
                       SOFTWARE_VERSION=0x02,
                       HARDWARE_VERSION=0x03,
                       PROTOCOL_VERSION=0x04
                       )
)

read_sensor_identification = Struct(
    "attribute" / Enum(Int8un,
                       ENVIRONMENT_STATUS=0x05,
                       MOVEMENT_PARAMETERS=0x06
                       )
)

read_system_identification = Struct(
    "attribute" / Enum(Int8un,
                       THRESHOLD=0x0C,
                       SCENE=0x10,
                       FORCED_UNOCCUPIED=0x12
                       )
)

read_command_map = {
    "DEVICE_INFO": read_device_identification,
    "SENSOR_INFO": read_sensor_identification,
    "SYSTEM_INFO": read_system_identification
}

read_command = Struct(
    "address1" / Enum(Int8un,
                      DEVICE_INFO=DEVICE_INFO,
                      SENSOR_INFO=0x02,
                      SYSTEM_INFO=0x04
                      ),
    "command" / Switch(
        lambda this: this.address1,
        read_command_map
    )
)
