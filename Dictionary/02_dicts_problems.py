"""
LESSON 2 — DICTIONARY PROBLEMS

Same rules as before:
  1. Read 02_dicts_basics.md first.
  2. Use the 4-step framework BEFORE writing code.
  3. Run: python3 lessons/02_dicts_problems.py
  4. Stuck for 15+ min? Ask for a HINT.
"""


# -----------------------------------------------------------------------------
# PROBLEM 1 — Count letters  (Pattern: COUNT)
# Given a string, return a dict mapping each character to how many times
# it appears.
# Example: count_letters("apple") → {"a": 1, "p": 2, "l": 1, "e": 1}
# Edge case: empty string → {}
# -----------------------------------------------------------------------------
def count_letters(text):
    # TODO
    mydict={}
    for ele in text:
        mydict[ele]= mydict.get(ele,0)+1
    return mydict

# -----------------------------------------------------------------------------
# PROBLEM 2 — Most frequent  (Pattern: COUNT + REDUCE)
# Given a list of words, return the word that appears MOST often.
# If there's a tie, return any of the tied words.
# Example: most_frequent(["a", "b", "a", "c", "b", "a"]) → "a"
# Edge case: empty list → None
# Hint: this is TWO steps — first count, then find the max.
# -----------------------------------------------------------------------------
def most_frequent(words):
    # TODO
    result_dict= {}
    maxn=0
    maxele= None
    for item in words:
        if item in result_dict:
            result_dict[item]+=1
        else:
            result_dict[item]=1
    for key, val in result_dict.items():
        if maxn<val:
            maxn=val
            maxele=key
    return maxele
    pass


# -----------------------------------------------------------------------------
# PROBLEM 3 — Has duplicates?  (Pattern: dict as "seen" tracker)
# Return True if the list contains any duplicate value, else False.
# Example: has_duplicates([1, 2, 3, 2]) → True
#          has_duplicates([1, 2, 3, 4]) → False
# Try to RETURN EARLY as soon as you find a duplicate (don't scan the rest).
# -----------------------------------------------------------------------------
def has_duplicates(items):
    # TODO
    res_dic={}
    for i in items:
        if (i in res_dic):
            return True
        else:
            res_dic[i]=1
    return False        
    pass


# -----------------------------------------------------------------------------
# PROBLEM 4 — Group by length  (Pattern: GROUP)
# Given a list of strings, return a dict where:
#   - keys are word lengths
#   - values are LISTS of words with that length
# Example: group_by_length(["hi", "bye", "yo", "cat"])
#          → {2: ["hi", "yo"], 3: ["bye", "cat"]}
# -----------------------------------------------------------------------------
def group_by_length(words):
    # TODO
    res_dic= {}

    for i in words:
        if (len(i) in res_dic):
            res_dic[len(i)].append(i)
        else:
            res_dic[len(i)]= [i]

    return res_dic
    
    pass
 

# -----------------------------------------------------------------------------
# PROBLEM 5 — Invert a dict  (Pattern: TRANSFORM)
# Swap keys and values. Assume all values are unique.
# Example: invert_dict({"a": 1, "b": 2}) → {1: "a", 2: "b"}
# -----------------------------------------------------------------------------
def invert_dict(d):
    dnew= {}
    for key, val in d.items():
        dnew[val]=key

    return dnew
    pass


# =============================================================================
# TESTS
# =============================================================================
def run_tests():
    tests = [
        ("P1 count_letters",      count_letters("apple"),
            {"a": 1, "p": 2, "l": 1, "e": 1}),
        ("P1 empty string",       count_letters(""),                 {}),
        ("P1 single char",        count_letters("aaaa"),             {"a": 4}),

        ("P2 most_frequent",      most_frequent(["a", "b", "a", "c", "b", "a"]), "a"),
        ("P2 single word",        most_frequent(["only"]),           "only"),
        ("P2 empty",              most_frequent([]),                 None),

        ("P3 has_duplicates yes", has_duplicates([1, 2, 3, 2]),      True),
        ("P3 has_duplicates no",  has_duplicates([1, 2, 3, 4]),      False),
        ("P3 empty",              has_duplicates([]),                False),

        ("P4 group_by_length",    group_by_length(["hi", "bye", "yo", "cat"]),
            {2: ["hi", "yo"], 3: ["bye", "cat"]}),
        ("P4 empty",              group_by_length([]),               {}),

        ("P5 invert_dict",        invert_dict({"a": 1, "b": 2}),     {1: "a", 2: "b"}),
        ("P5 empty",              invert_dict({}),                   {}),
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
