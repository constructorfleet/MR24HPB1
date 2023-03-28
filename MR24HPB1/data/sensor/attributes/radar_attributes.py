from construct import Struct, Enum, Int8un, Int64un, Const, Float32l

body_parameters_status = Struct(
    "environment_status" / Float32l
)

environment_state = Struct(
    "occupied" / Enum(Int8un,
                      UNOCCUPIED=0x01,
                      OCCUPIED=0x01
                      ),
    "moving" / Enum(Int8un,
                    STATIONARY=0x00,
                    MOVING=0x01),
    "padding" / Const(b"\xFF")
)

direction_state = Struct(
    "direction_state" / Enum(Int64un,
                             UNKNWONW=0x010101,
                             ON_APPROACH=0x010102,
                             ON_AWAY=0x010103,
                             SUSTAINED_APPROACH=0x010104,
                             SUSTAINED_AWAY=0x010105
                             )

)
