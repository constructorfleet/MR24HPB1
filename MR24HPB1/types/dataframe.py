import dataclasses

from construct import Const, Int16un, Select
from construct_typed import DataclassMixin, csfield, DataclassStruct

from MR24HPB1.types.commands.active_report import ActiveReportFrame
from MR24HPB1.types.commands.passive_report import PassiveReportFrame
from MR24HPB1.types.commands.read import ReadFrame
from MR24HPB1.types.commands.write import WriteFrame


@dataclasses.dataclass
class DataFrame(DataclassMixin):
    header: int = csfield(Const(b"\x55"))
    frame_length: int = csfield(Int16un)
    command: dict = csfield(
        Select(
            DataclassStruct(ActiveReportFrame),
            DataclassStruct(PassiveReportFrame),
            DataclassStruct(WriteFrame),
            DataclassStruct(ReadFrame)
        ))
    crc_check: int = csfield(Int16un)
