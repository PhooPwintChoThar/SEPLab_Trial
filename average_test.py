from average import findAverage

def run_test(values, minv=0, maxv=10):
    print("Input:", values)
    result = findAverage(values, minv, maxv)
    print("\nOutput:", result)
    print("-"*40)


# Test cases for 6 basis paths
tests = [
    [5, 8, -999],                 # Path 1
    [-999],                       # Path 2
    [1,2,3,4,5,6,7,8,9,10,11],    # Path 3
    [5, -2, 7, -999],             # Path 4
    [3, 12, 6, -999],             # Path 5
    [2,4,6,8,-999]                # Path 6
]

for t in tests:
    run_test(t)