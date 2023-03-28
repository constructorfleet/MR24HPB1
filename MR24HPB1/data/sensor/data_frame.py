from construct import Struct, Const, Int16un, Int8un, Enum, Switch

from MR24HPB1.data.sensor.commands.active_report import active_report
from MR24HPB1.data.sensor.commands.passive_report import passive_report
from MR24HPB1.data.sensor.commands.read_command import read_command
from MR24HPB1.data.sensor.commands.write_command import write_command

command_map = {
    "READ": read_command,
    "WRITE": write_command,
    "PASSIVE_REPORT": passive_report,
    "ACTIVE_REPORT": active_report
}
DataFrame = Struct(
    "header" / Const(b"\x55"),
    "length" / Int16un,
    "function_code" / Enum(Int8un,
                           READ=0x01,
                           WRITE=0x02,
                           PASSIVE_REPORT=0x03,
                           ACTIVE_REPORT=0x04),
    "function" / Switch(lambda this: this.function_code,
                        command_map),
    "checksum" / Int16un
)
