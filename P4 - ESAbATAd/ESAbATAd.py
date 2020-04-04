
def read_bool(message=""):
    global query_count
    query_count += 1

    print(message, flush=True)
    return int(input()) != 0


if __name__ == "__main__":
    num_tests, num_bits = list(map(int, input().split()))
    for test in range(num_tests):
        query_count = 0
        start_to_end, end_to_start = [read_bool("1")], [read_bool(str(num_bits))]
        while query_count < 150 and len(start_to_end) + len(end_to_start) < num_bits:
            if query_count % 10 == 0:
                len_smallest = min(len(start_to_end), len(end_to_start))
                common_indexes = [i for i in range(len_smallest) if start_to_end[i] == end_to_start[i]]

                # No common elements. Flipping and reversing have the same effect, as does nothing and both
                # All common elements. Nothing and reversing have the same effect, as does flipping and both
                # Some Common, some not. 2 queries to find out which one happened

                flip, reverse, assumption = False, False, False
                if len(common_indexes) == 0:
                    assumption = True
                    if read_bool("1") != start_to_end[0]:
                        reverse = True
                elif len(common_indexes) == len_smallest:
                    assumption = True
                    if read_bool("1") != start_to_end[0]:
                        flip = True
                else:
                    first_diff = next(i for i in range(len_smallest)
                                      if len(common_indexes) <= i or i != common_indexes[i])

                    if read_bool(str(common_indexes[0] + 1)) == start_to_end[common_indexes[0]]:
                        if read_bool(str(first_diff + 1)) != start_to_end[first_diff]:
                            reverse = True
                    else:
                        flip = True
                        if read_bool(str(first_diff + 1)) == start_to_end[first_diff]:
                            reverse = True

                if flip:
                    start_to_end = [not item for item in start_to_end]
                    end_to_start = [not item for item in end_to_start]

                if reverse:
                    start_to_end, end_to_start = end_to_start, start_to_end

                if assumption and len(start_to_end) != len(end_to_start):
                    if len(start_to_end) < len(end_to_start):
                        end_to_start.pop(-1)
                    else:
                        start_to_end.pop(-1)

            if len(end_to_start) < len(start_to_end):
                end_to_start.append(read_bool(str(num_bits - len(end_to_start))))
            else:
                start_to_end.append(read_bool(str(len(start_to_end) + 1)))

        bit_array = ['1' if item else '0' for item in start_to_end + list(reversed(end_to_start))]
        print(''.join(bit_array), flush=True)
        if input() == 'N':
            exit()
