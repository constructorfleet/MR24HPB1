from construct import Struct, Int8un, Enum, Switch, Int64un

from MR24HPB1.data.attributes.radar_attributes import environment_state, body_parameters_status, direction_state

report_device_identification = Struct(
    "software_version" / Int64un
    # "value" / Int8un[15]
)

report_sensor_identification = Struct(
    "attribute" / Enum(Int8un,
                       ENVIRONMENT_STATUS=0x05,
                       MOVEMENT_PARAMETERS=0x06,
                       DIRECTION_STATUS=0x07
                       ),
    "value" / Switch(lambda this: this.attribute,
                     {
                         "ENVIRONMENT_STATUS": environment_state,
                         "MOVEMENT_PARAMETERS": body_parameters_status,
                         "DIRECTION_STATUS": direction_state
                     })
)

report_command_map = {
    "DEVICE_INFO": report_device_identification,
    "SENSOR_INFO": report_sensor_identification,
}

active_report = Struct(
    "address1" / Enum(Int8un,
                      DEVICE_INFO=0x01,
                      SENSOR_INFO=0x03,
                      ),
    "report" / Switch(
        lambda this: this.address1,
        report_command_map
    )
)
