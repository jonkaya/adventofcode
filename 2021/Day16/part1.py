import binascii

from typing import Dict, List, Literal, Set, Tuple

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

def hex_to_bin(hex: str) -> List[str]:
    return list("".join([hex_to_byte_str[hex_digit] for hex_digit in hex]))

def bin_to_decimal(bin: List[str]) -> int:
    total: int = 0
    i: int = 0

    for digit in reversed(bin):
        if digit == "1":
            total += 2**i
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

def get_packet(buffer: List[str]) -> Tuple[int, List[str]]:
    total_version: int = 0

    packet_version: str = buffer[:3]
    packet_type: str = buffer[3:6]
    del buffer[:6]

    version: int = bin_to_decimal(packet_version)
    type: int = bin_to_decimal(packet_type)

    total_version += version
    if type == 4:
        literal, buffer = get_literal(buffer)
        return total_version, buffer
    elif buffer:
        len_type_id: int = int(buffer.pop(0))
        if len_type_id == 0:
            # read the next 15 bits for length
            length: int = bin_to_decimal(buffer[:15])
            del buffer[:15]

            subpackets: List[str] = buffer[:length]
            del buffer[:length]

            while subpackets:
                subtotal, subpackets = get_packet(subpackets)
                total_version += subtotal
        elif len_type_id == 1:
            # read the next 11 bits for length
            length: int = bin_to_decimal(buffer[:11])
            del buffer[:11]

            for _ in range(length):
                subtotal, buffer = get_packet(buffer)
                total_version += subtotal
    return total_version, buffer


def decode_packet() -> int:
    hex_message: str = None

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue
            hex_message = line

    total, buffer = get_packet(hex_to_bin(hex_message))

    return total

if __name__ == "__main__":
    print(decode_packet())
