"""
https://adventofcode.com/2022/day/6
"""

def comms_processer() -> int:
    """
    Method that will take in the puzzle input and determine the number of
    characters that need to be processed before the first start-of-packet
    marker is found.
    """
    with open('day-6/data_stream.txt', 'r', encoding="utf-8") as data_stream:
        stream_input = data_stream.read()
        start_of_packet = []
        for index in range(0, len(stream_input) + 1):
            # Add the current character to the start_of_packet list
            start_of_packet.append(stream_input[index])

            # Now look at the four characters to determine if we have a start-of-packet marker
            if len(start_of_packet) != 4:
                continue

            if len(set(start_of_packet)) == len(start_of_packet):
                # We have the start-of-packet marker so return the index
                return index + 1
            # Otherwise, remove the first index to made room for the next character
            start_of_packet.pop(0)


if __name__ == "__main__":
    print("Number of characters need to be processed before the " \
        f"first start-of-packet marker {comms_processer()}")
