from construct import Struct, Const, Int16ub, Int8ub, Enum, Switch, Int32ub, Float64b

from MR24HPB1.types.attributes.radar_attributes import environment_state, body_parameters_status, direction_state
from MR24HPB1.types.attributes.system_attributes import scene, threshold_gears

report_device_identification = Struct(
    "software_version" / Int8ub
    # "value" / Int8ub[15]
)

report_sensor_identification = Struct(
    "attribute" / Enum(Int8ub,
                       ENVIRONMENT_STATUS=0x05,
                       MOVEMENT_PARAMETERS=0x06,
                       DIRECTION_STATUS=0x07
                       )
#     "value" / Switch(lambda this: this.attribute,
#                      {
#                          "ENVIRONMENT_STATUS": environment_state,
#                          "MOVEMENT_PARAMETERS": body_parameters_status,
#                          "DIRECTION_STATUS": direction_state
#                      })
)

report_command_map = {
    "DEVICE_INFO": report_device_identification,
    "SENSOR_INFO": report_sensor_identification,
}

report_command = Struct(
    "address1" / Enum(Int8ub,
                      DEVICE_INFO=0x01,
                      SENSOR_INFO=0x03,
                      ),
    "report" / Switch(
        lambda this: this.address1,
        report_command_map
    )
)
