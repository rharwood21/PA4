from typing import TextIO, Tuple, List, Any
from Repetition import Repetition


def process_signal(signal: [], x: [], y: [], output_file: TextIO) -> tuple[list[Any], list[Any]]:
    """

    :param x:
    :param y:
    :param signal:
    :param output_file:
    :return:
    """
    x_reps = []
    y_reps = []
    noise = []
    # Create current x_rep and y_rep objects
    currentXRep = Repetition(x)
    currentYRep = Repetition(y)
    for i in range(len(signal)):
        if currentXRep.append_symbol(signal[i], i):
            # appending symbol was successful...
            # if repetition is complete, add to x_reps
            if currentXRep.is_complete():
                output_file.write(f"{str(currentXRep)}\n")
                x_reps.append(currentXRep)
                currentXRep = Repetition(x)
        elif currentYRep.append_symbol(signal[i], i):
            # appending symbol was successful
            # if repetition is complete, add to y_reps
            if currentYRep.is_complete():
                output_file.write(f"{str(currentYRep)}\n")
                y_reps.append(currentYRep)
                currentYRep = Repetition(y)
        else:
            noise.append(i)
            # signal did not fit in to x or y so it mus tbe noise

            # determine if leading noise or trailing noise
    return x_reps, y_reps


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    # Read each line in the input
    lines = []
    next_line = input_file.readline()
    while next_line is not None and next_line != "":
        lines.append(next_line)
        next_line = input_file.readline()
    line_number = 1
    for line in lines:
        output_file.write(f"\n\ns{line_number}\n")
        pieces = line.split(',')
        x = pieces[0]
        y = pieces[1]
        signal = pieces[2]

        # call process_signal for each line
        x_reps, y_reps = process_signal(signal, x, y, output_file)
        line_number += 1

    return
