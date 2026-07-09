"""
LESSON 1 — LIST PROBLEMS

Instructions:
  1. Read 01_lists_basics.md first.
  2. Use the 4-step framework (00_problem_solving_framework.md) BEFORE coding.
  3. Solve ONE at a time. Run the file: python3 lessons/01_lists_problems.py
  4. Each problem prints PASS/FAIL automatically. Tests are at the bottom.
  5. Stuck for 15+ min? Ask me for a HINT (not the answer).
"""


# -----------------------------------------------------------------------------
# PROBLEM 1 — Sum of a list  (Pattern: REDUCE)
# Return the sum of all numbers in the list. Don't use the built-in sum().
# Example: sum_list([1, 2, 3, 4]) → 10
# Edge case: empty list should return 0.
# -----------------------------------------------------------------------------
def sum_list(numbers):
    # TODO: your code here
    result = 0
    for ele in numbers:
        result=result+ele
    return result

    pass


# -----------------------------------------------------------------------------
# PROBLEM 2 — Squares  (Pattern: TRANSFORM)
# Return a new list with each number squared.
# Example: squares([1, 2, 3]) → [1, 4, 9]
# -----------------------------------------------------------------------------
def squares(numbers):
    # TODO  
    result=[]
    for ele in numbers:
        result.append(ele*ele)
    return result

    pass


# -----------------------------------------------------------------------------
# PROBLEM 3 — Only positives  (Pattern: FILTER)
# Return a new list containing only the positive numbers (> 0).
# Example: only_positives([-2, 3, 0, 5, -1]) → [3, 5]
# Note: 0 is NOT positive.
# -----------------------------------------------------------------------------
def only_positives(numbers):
    # todo
    result=[]
    for i in numbers:
        if (i>0):
            result.append(i)
    return result
    pass


# -----------------------------------------------------------------------------
# PROBLEM 4 — Find the max  (Pattern: REDUCE)
# Return the largest number. Don't use built-in max().
# Example: find_max([3, 7, 2, 9, 4]) → 9
# Edge case: if the list is empty, return None.
# -----------------------------------------------------------------------------
def find_max(numbers):
    # TODO dont suggest code
    if len(numbers)>0:
        target=numbers[0]
        for i in numbers[1:]:
            if i>target:
                target=i 
        return target
    else:
        return None
    pass


# -----------------------------------------------------------------------------
# PROBLEM 5 — Reverse a list  (Pattern: TRANSFORM with order)
# Return a NEW list with items in reverse order. Don't use [::-1] or .reverse().
# Example: reverse_list([1, 2, 3]) → [3, 2, 1]
# -----------------------------------------------------------------------------
def reverse_list(items):
    # TODO
    i=len(items)-1
    result=[]
    while i>=0:
        result.append(items[i])
        i=i-1
    return result
    pass


# =============================================================================
# TESTS — don't modify below this line
# =============================================================================
def run_tests():
    tests = [
        ("P1 sum_list",       sum_list([1, 2, 3, 4]),         10),
        ("P1 sum_list empty", sum_list([]),                    0),
        ("P2 squares",        squares([1, 2, 3]),             [1, 4, 9]),
        ("P2 squares empty",  squares([]),                    []),
        ("P3 only_positives", only_positives([-2, 3, 0, 5, -1]), [3, 5]),
        ("P3 only_pos zero",  only_positives([0, 0, 0]),       []),
        ("P4 find_max",       find_max([3, 7, 2, 9, 4]),       9),
        ("P4 find_max one",   find_max([5]),                   5),
        ("P4 find_max empty", find_max([]),                    None),
        ("P4 find_max negs",  find_max([-5, -2, -10]),         -2),
        ("P4 find_max 1 neg", find_max([-100]),                -100),
        ("P5 reverse_list",   reverse_list([1, 2, 3]),         [3, 2, 1]),
        ("P5 reverse empty",  reverse_list([]),                []),
    ]
    passed = 0
    for name, got, expected in tests:
        if got == expected:
            print(f"  PASS  {name}")
            passed += 1
        else:
            print(f"  FAIL  {name}  expected={expected!r}  got={got!r}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
