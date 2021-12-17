from functools import reduce
from operator import mul

from typing import List, Tuple

INPUT_FILE_NAME = "input"

hex_to_byte_str = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

OPS = {
    0: lambda it: sum([x.get_val() for x in it]),
    1: lambda it: reduce(mul, [x.get_val() for x in it]),
    2: lambda it: min([x.get_val() for x in it]),
    3: lambda it: max([x.get_val() for x in it]),
    5: lambda it: 1 if it[0].get_val() > it[1].get_val() else 0,
    6: lambda it: 1 if it[0].get_val() < it[1].get_val() else 0,
    7: lambda it: 1 if it[0].get_val() == it[1].get_val() else 0,
}


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.subpackets = list()
        self.val = None

    def get_val(self) -> int:
        if self.type == 4:
            return self.val
        else:
            return OPS[self.type](self.subpackets)


def hex_to_bin(hex: str) -> List[str]:
    return list("".join([hex_to_byte_str[hex_digit] for hex_digit in hex]))


def bin_to_decimal(bin: List[str]) -> int:
    total: int = 0
    i: int = 0

    for digit in reversed(bin):
        if digit == "1":
            total += 2 ** i
        i += 1
    return total


def get_literal(buffer: List[str]) -> Tuple[int, List[str]]:
    literal: List[str] = list()

    while buffer:
        literal.extend(buffer[1:5])

        if buffer[0] == "0":
            del buffer[:5]
            break
        del buffer[:5]
    return bin_to_decimal(literal), buffer


def get_packet(buffer: List[str]) -> Tuple[Packet, List[str]]:

    packet_version: str = buffer[:3]
    packet_type: str = buffer[3:6]
    del buffer[:6]

    version: int = bin_to_decimal(packet_version)
    type: int = bin_to_decimal(packet_type)

    packet = Packet(version, type)
    if type == 4:
        literal, buffer = get_literal(buffer)
        packet.val = literal

        return packet, buffer
    elif buffer:
        len_type_id: int = int(buffer.pop(0))
        if len_type_id == 0:
            # read the next 15 bits for length
            length: int = bin_to_decimal(buffer[:15])
            del buffer[:15]

            subpackets: List[str] = buffer[:length]
            del buffer[:length]

            while subpackets:
                subpacket, subpackets = get_packet(subpackets)
                packet.subpackets.append(subpacket)
        elif len_type_id == 1:
            # read the next 11 bits for length
            length: int = bin_to_decimal(buffer[:11])
            del buffer[:11]

            for _ in range(length):
                subpacket, buffer = get_packet(buffer)
                packet.subpackets.append(subpacket)

    return packet, buffer


def decode_packet() -> int:
    hex_message: str = None

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue
            hex_message = line

    packet, buffer = get_packet(hex_to_bin(hex_message))

    return packet.get_val()


if __name__ == "__main__":
    print(decode_packet())
