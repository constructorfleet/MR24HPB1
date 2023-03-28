from construct import Struct, Int8un, Enum, Switch

write_system_identification = Struct(
    "attribute" / Enum(Int8un,
                       THRESHOLD=0x0C,
                       SCENE=0x10,
                       FORCED_UNOCCUPIED=0x12
                       ),
    "value" / Int8un
)

write_command_map = {
    "SENSOR_INFO": write_system_identification
}

write_command = Struct(
    "address1" / Enum(Int8un,
                      DEVICE_INFO=0x01,
                      SENSOR_INFO=0x02,
                      SYSTEM_INFO=0x04
                      ),
    "write" / Switch(
        lambda this: this.address1,
        write_command_map
    )
)
