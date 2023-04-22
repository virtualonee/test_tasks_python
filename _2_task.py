import math


class Segment:
    count = 1

    def __init__(self, position, value):
        self.value = value
        self.range = value
        self.position = position


def build_optimal_ranges(seg_list: list[Segment], points: int):
    seg_dict: dict[int, list[Segment]]
    seg_dict = {0: seg_list}

    for iterator in range(1, points+1):
        seg_dict[iterator] = (seg_dict[iterator-1])

        max_value = 0
        min_count = 1
        iter = 0
        index = 0

        for segment in seg_dict[iterator]:
            if (segment.value > max_value) and (segment.count <= min_count):
                max_value = segment.value
                min_count = segment.count
                index = iter

            iter += 1

        seg_dict[iterator][index].count += 1
        seg_dict[iterator][index].value = seg_dict[iterator][index].range / seg_dict[iterator][index].count

    return seg_dict[points]


def get_result_list(seg_lis: list[Segment]):
    result_list = []

    for i in seg_lis:
        for j in range(0, i.count):
            result_list.append(i.value)

    return result_list



if __name__ == '__main__':
    while True:
        segment_list = []
        n = int(math.fabs(int(input("Input n (number of ATMs.): "))))
        k = int(math.fabs(int(input("Input k (number of additional ATMs): "))))

        for i in range(0, n):
            segment_list.append(Segment(i, math.fabs(int(input("S["+str(i)+"] = ")))))

        segment_list.sort(key=lambda x: x.value, reverse=True)

        segment_list = build_optimal_ranges(segment_list, k)

        segment_list.sort(key=lambda x: x.position, reverse=False)

        print(get_result_list(segment_list))

        print()
