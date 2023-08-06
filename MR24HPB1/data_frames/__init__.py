import dataclasses
from typing import Any, Type

from construct import Padding, Int8ub
from construct_typed import DataclassMixin, csfield, DataclassStruct

def get_frame_struct(frame: Type[DataclassMixin]) -> DataclassStruct[Type[DataclassMixin]]:
    @dataclasses.dataclass
    class DataFrame(DataclassMixin):
        data: Any = csfield(DataclassStruct(frame))
        _padding: bytes = csfield(Padding(19 - DataclassStruct(frame).sizeof()))
        check_sum = csfield(Int8ub)

    return DataclassStruct(DataFrame)
