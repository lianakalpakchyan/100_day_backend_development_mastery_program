import gc


def process_large_dataset(filename):
    results = []

    with open(filename) as f:
        for i, chunk in enumerate(read_chunks(f, size=10000)):
            processed = expensive_operation(chunk)
            results.append(processed)

            if i % 100 == 0:
                gc.collect(0)
                print(f"Processed {i} chunks, ran GC")

    return results


def read_chunks(file, size):
    while True:
        lines = [file.readline() for _ in range(size)]
        if not lines[0]:
            break
        yield lines


def expensive_operation(chunk):
    return [line.strip().upper() for line in chunk if line]


process_large_dataset('large_data.txt')