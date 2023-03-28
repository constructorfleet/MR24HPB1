from construct import Struct, Int8un, Enum, Switch

from MR24HPB1.data.sensor.attributes.device_attributes import device_id, software_version, hardware_version, protocol_version
from MR24HPB1.data.sensor.attributes.radar_attributes import body_parameters_status, environment_state
from MR24HPB1.data.sensor.attributes.system_attributes import threshold_gears, scene, forced_unoccupied
from MR24HPB1.data.sensor.const import DEVICE_INFO

report_device_identification = Struct(
    "attribute" / Enum(Int8un,
                       DEVICE_ID=0x01,
                       SOFTWARE_VERSION=0x02,
                       HARDWARE_VERSION=0x03,
                       PROTOCOL_VERSION=0x04
                       ),
    "value" / Switch(lambda this: this.attribute,
                     {
                         "DEVICE_ID": device_id,
                         "SOFTWARE_VERSION": software_version,
                         "HARDWARE_VERSION": hardware_version,
                         "PROTOCOL_VERSION": protocol_version
                     })
)

report_sensor_identification = Struct(
    "attribute" / Enum(Int8un,
                       ENVIRONMENT_STATUs=0x05,
                       MOVEMENT_PARAMETERS=0x06
                       ),
    "value" / Switch(lambda this: this.attribute,
                     {
                         "ENVIRONMENT_STATUs": environment_state,
                         "MOVEMENT_PARAMETERS": body_parameters_status
                     })
)

report_system_identification = Struct(
    "attribute" / Enum(Int8un,
                       THRESHOLD=0x0C,
                       SCENE=0x10,
                       FORCED_UNOCCUPIED=0X12
                       ),
    "value" / Switch(lambda this: this.attribute,
                     {
                         "THRESHOLD": threshold_gears,
                         "SCENE": scene,
                         "FORCED_UNOCCUPIED": forced_unoccupied
                     })
)

report_map = {
    "DEVICE_INFO": report_device_identification,
    "SENSOR_INFO": report_sensor_identification,
    "SYSTEM_INFO": report_system_identification
}

passive_report = Struct(
    "address1" / Enum(Int8un,
                      DEVICE_INFO=DEVICE_INFO,
                      SENSOR_INFO=0x03,
                      SYSTEM_INFO=0x04
                      ),
    "command" / Switch(
        lambda this: this.address1,
        report_map
    )
)
