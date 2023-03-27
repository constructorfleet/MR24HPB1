from construct import Struct, Float64b, Int32ub, Enum, Int8ub, Int64ub

body_parameters_status = Struct(
    "environment_status" / Int64ub
)

environment_state = Struct(
    "environment_state" / Enum(Int32ub,
                               UNOCCUPIED=0x00FF,
                               STATIC=0x0100,
                               MOVING=-0x0101
                               )
)

direction_state = Struct(
    "direction_state" / Enum(Int64ub,
                             UNKNWONW=0x010101,
                             ON_APPROACH=0x010102,
                             ON_AWAY=0x010103,
                             SUSTAINED_APPROACH=0x010104,
                             SUSTAINED_AWAY=0x010105
                             )

)
