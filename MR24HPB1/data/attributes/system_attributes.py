from construct import Struct, Enum, Int8un

threshold_gears = Struct(
    "threshold" / Int8un
)

scene = Struct(
    "scene" / Enum(Int8un,
                   DEFAULT=0x00,
                   AREA=0x01,
                   BATHROOM=0x02,
                   BEDROOM=0x03,
                   LIVING_ROOM=0x04,
                   OFFICE=0x05,
                   HOTEL=0x06
                   )
)

forced_unoccupied = Struct(
    "forced_unoccupied" / Enum(Int8un,
                               SECONDS_0=0x00,
                               SECONDS_10=0x01,
                               SECONDS_30=0x02,
                               SECONDS_60=0x03,
                               SECONDS_120=0x04,
                               SECONDS_300=0x05,
                               SECONDS_600=0x06,
                               SECONDS_1800=0x07,
                               SECONDS_3600=0x08
                               )
)
