#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    bytes_to_follow = 0
    first_byte_mask = 1 << 7
    second_byte_mask = 1 << 6

    for byte in data:
        current_byte_mask = 1 << 7

        if bytes_to_follow == 0:
            while current_byte_mask & byte:
                bytes_to_follow += 1
                current_byte_mask >>= 1

            if bytes_to_follow == 0:
                continue

            if bytes_to_follow == 1 or bytes_to_follow > 4:
                return False

        else:
            if not (byte & first_byte_mask and not (byte & second_byte_mask)):
                return False

        bytes_to_follow -= 1

    return bytes_to_follow == 0
