"""
**Merge Overlapping Intervals:** Given a collection of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals as they appear.
To create test data for the "Merge Overlapping Intervals" problem, we will provide a list of intervals where each interval is represented as a list or tuple of two numbers,
with the first number representing the start of the interval and the second number representing the end of the interval.

Here is an example of test data for this problem:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
In this example, intervals are represented as lists. Some intervals overlap, such as [1, 3] and [2, 6], because the end of the first interval (3) is greater than or equal to the 
start of the second interval (2).

Now let's explain what the problem is asking, using the test data provided:

Interval [1, 3] and [2, 6]:
These two intervals overlap because 2 <= 3. They should be merged into a single interval [1, 6], which starts at the earliest start time and ends at the latest end time of the 
overlapping intervals.

Interval [8, 10] does not overlap with any other interval:
This interval does not overlap with the previously merged interval [1, 6] or the following interval [15, 18], so it remains as it is.

Interval [15, 18] does not overlap with any other interval:
Similar to the interval [8, 10], this interval does not overlap with any others, so it also remains as it is.

Output : After processing the test data, the expected result would merge the overlapping intervals and return them in the order they appeared:

merged_intervals = [[1, 6], [8, 10], [15, 18]]
"""
import unittest

def find_overlap(intervals: list) -> list:
    print(f"Working with {intervals}")
    new_intervals = []
    # If the Lists are empty
    if not intervals:
        print(f"Empty")
        return []
    
    # Sort by Starting Value of each interval
    intervals.sort(key=lambda x : x[0])
    print(f"Sorted intervals is {intervals}")

    # The first interval goes in by default
    new_intervals.append(intervals[0])

    # Start traversing the list from 2nd item
    for current in intervals[1:]:
        # Get the last interval in the Merged List
        prev = new_intervals[-1]
        print(f"Curent outside IF is {current}")
        print(f"And Prev outside IF is {prev} and new_intervals is {new_intervals}")
        if current[0] <= prev[1]:
            new_intervals[-1] = [prev[0], max(prev[1], current[1])]
            print(f"New Interval Inside is now {new_intervals} for Current {current} and Previous {prev}")

        else:
            new_intervals.append(current)
    return new_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        # Define a list of test cases. Each test case is a tuple where
        # the first element is the input list of intervals, and
        # the second element is the expected output from the function.
        test_data = [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[1, 4], [2, 3]], [[1, 4]]),
            ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
            ([], []),
            ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),
            ([[5, 6], [1, 3], [3, 5]], ([1, 6]))
        ]
        # Loop through each test case and check if the function produces the expected output
        for input_data, expected in test_data:
            # subTest provides a way to differentiate which test case fails if there is an error
            self.subTest(input_data=input_data, expected=expected)
            # Here merge_intervals function is called with the 'intervals' from the test case.
            # The result is then compared with the 'expected' result using assertEqual.
            self.assertEqual(find_overlap(intervals=input_data), expected)      
    
if __name__ == '__main__':
    test_data = [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[1, 4], [2, 3]], [[1, 4]]),
            ([[5, 6], [1, 3], [3, 5]], ([1, 6]))

        ]
    for input_data, expected in test_data:
        merged_data = find_overlap(intervals=input_data)
        print("-" * 110)
        print(f"Original Index is : \t\t{input_data}")
        print(f"Merged Index is   : \t\t{merged_data}")
        print("-" * 110)
    # unittest.main()
    
    