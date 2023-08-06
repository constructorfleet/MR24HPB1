#!/usr/bin/env python

"""Package entry point."""
from construct_typed import DataclassStruct
import dataclasses
from typing import Any, Type

from construct import Padding, Int8ub, Padded, this, Byte, len_, Bytes, Aligned, Subconstruct
from construct_typed import DataclassMixin, csfield, DataclassStruct

from MR24HPB1.data_frames.light import LightReport


# from MR24HPB1.types.dataframe import DataFrame


def get_frame_struct(frame: Type[DataclassMixin]) -> DataclassStruct[Type[DataclassMixin]]:
    @dataclasses.dataclass
    class DataFrame(DataclassMixin):
        data: Any = csfield(DataclassStruct(frame))
        check_sum: int = csfield(Int8ub)

    return DataclassStruct(DataFrame)

if __name__ == '__main__':  # pragma: no cover
    test_data = b"\xaa\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xaf"
    print(get_frame_struct(LightReport))
    print(get_frame_struct(LightReport).parse(test_data))
    # print(data_frame.parse(bytes(test_data)))
    # format = get_frame_struct()
    # data = [0x55, 0x0b, 0x00, 0x04, 0x03, 0x06, 0x00, 0x00, 0x80, 0x3F, 0xFC, 0x45]
    #     #[0x55, 0x14, 0x00, 0x03, 0x01, 0x01, 0x74, 0x6d, 0x75, 0x49, 0x61, 0x67, 0x31, 0x74, 0x66, 0x68]
    # print(format.parse(bytes(data)))
    # # main()  # pylint: disable=no-value-for-parameter
