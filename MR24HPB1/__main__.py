#!/usr/bin/env python

"""Package entry point."""
from MR24HPB1.data.data_frame import DataFrame

test_data = [
    0x055,
    0x08,
    0x00,
    0x01,
    0x01,
    0x03,
    0x9A,
    0xFB,
    0xE7,
    0x3F,
    0xFC,
    0x45
]

Data)

if __name__ == '__main__':  # pragma: no cover
    print(DataFrame.parse(bytes(test_data)));
    # main()  # pylint: disable=no-value-for-parameter
