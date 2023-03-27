from construct import Struct, Const, Int16ub, Int8ub, Enum, Switch

from . import active_report
from .passive_report import passive_report
from .read_command import read_command
from .write_command import write_command

command_map = {
    "READ": read_command,
    "WRITE": write_command,
    "PASSIVE_REPORT": passive_report,
    "ACTIVE_REPORT": active_report
}
DataFrame = Struct(
    "header" / Const(b"\x55"),
    "length" / Int16ub,
    "function_code" / Enum(Int8ub,
                           READ=0x01,
                           WRITE=0x02,
                           PASSIVE_REPORT=0x04,
                           ACTIVE_REPORT=0x04),
    "function" / Switch(lambda this: this.function_code,
                        command_map)
)

