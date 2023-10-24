import unittest


class Arrays:
    def __init__(self, unsorted_array, reverse):
        self.unsorted_array = unsorted_array
        global sorted_array
        sorted_array = self.merge_sort(unsorted_array, reverse)


    def merge_sort(self, arr, reverse):
        if len(arr) <= 1:
            return arr
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]
        left_half = self.merge_sort(left_half, reverse)
        right_half = self.merge_sort(right_half, reverse)
        if reverse == 0:
            return self.merge(left_half, right_half)
        else:
            return self.reversed_merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def reversed_merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result



    def find_first_unsorted(self, unsorted_array):
        first_unsorted = -1
        for i in range(len(unsorted_array)):
            if unsorted_array[i] != sorted_array[i]:
                first_unsorted = i
                break
        return first_unsorted


    def find_last_unsorted(self, unsorted_array):
        last_unsorted = -1
        for i in range(len(unsorted_array) - 1, 1, -1):
            if unsorted_array[i] != sorted_array[i]:
                last_unsorted = i
                break
        return last_unsorted


    def print_first_and_last(self, unsorted_array):
        print((self.find_first_unsorted(unsorted_array), self.find_last_unsorted(unsorted_array)))


if __name__ == '__main__':
    array1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    array2 = [19, 18, 16, 12, 10, 0, 8, 0, 8, 7, 6, 1]
    Array = Arrays(array2, 1)
    Array.print_first_and_last(array2)


# class Testing(unittest.TestCase):
#     def test_sorted(self):
#         array1 = [1, 2, 3, 4, 5]
#         Array1 = Arrays(array1)
#         self.assertEqual(Array1.find_first_unsorted(array1), -1)
#         self.assertEqual(Array1.find_last_unsorted(array1), -1)
#
#     def test_fully_unsorted(self):
#         array2 = [6, 5, 4, 3, 2, 1]
#         Array1 = Arrays(array2)
#         self.assertEqual(Array1.find_first_unsorted(array2), 0)
#         self.assertEqual(Array1.find_last_unsorted(array2), len(array2)-1)
#
#     def test_one_element(self):
#         array3 = [1]
#         Array1 = Arrays(array3)
#         self.assertEqual(Array1.find_first_unsorted(array3), -1)
#         self.assertEqual(Array1.find_last_unsorted(array3), -1)
