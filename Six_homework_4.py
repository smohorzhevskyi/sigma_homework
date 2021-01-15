

def circle(sequence, number):
    counter = 0

    while counter < number:
        for i in range(len(sequence)):
            if counter < number:
                yield sequence[i]
            counter += 1

