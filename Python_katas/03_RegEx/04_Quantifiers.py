import re

# Quantifiers tell "how many times" the previous pattern must repeat.
# -------------------------------------------------------------------

text = "a abc abbc abbbc abbbbc 123 1 12 1234 color colour"


# 1) *  -> zero or more times
#    a*  means: match "", "a", "aa", "aaa", ...
#    Here we search for 'ab*c' : 'a', followed by zero or more 'b', then 'c'
pattern_star = r"ab*c"
matches_star = re.findall(pattern_star, text)
print("'*' (zero or more) matches:", matches_star)
# In our text: "abc", "abbc", "abbbc", "abbbbc" will match, but lone "a" will not
# because 'c' is required after the b's.


# 2) +  -> one or more times
#    \d+ means: one or more digits (1, 23, 456, ...)
pattern_plus = r"\d+"
matches_plus = re.findall(pattern_plus, text)
print("'+' (one or more) digit groups:", matches_plus)
# This finds "123", "1", "12", "1234" as separate number sequences.


# 3) ?  -> zero or one time (optional)
#    colou?r means "color" OR "colour":
#    'u' may appear 0 or 1 time.
pattern_question = r"colou?r"
matches_question = re.findall(pattern_question, text)
print("'?' (optional u) matches:", matches_question)
# This will match both "color" and "colour" in the text.


# 4) {n} -> exactly n times
#    \d{3} means: exactly 3 digits in a row, like "123", "456"
pattern_exact = r"\b\d{3}\b"
matches_exact = re.findall(pattern_exact, text)
print("'{n}' (exactly 3 digits) matches:", matches_exact)
# In this text, "123" is exactly three digits;
# "1", "12", and "1234" do not match this pattern.


# 5) {n,} -> at least n times
#    a{2,} means: "aa", "aaa", "aaaa", ...
pattern_at_least = r"ab{2,}c"
matches_at_least = re.findall(pattern_at_least, text)
print("'{n,}' (at least 2 b's) matches:", matches_at_least)
# This matches "abbc", "abbbc", "abbbbc" (2 or more 'b'),
# but not "abc" (only one 'b').


# 6) {n,m} -> between n and m times (inclusive)
#    b{1,3} means: "b", "bb", or "bbb"
pattern_range = r"ab{1,3}c"
matches_range = re.findall(pattern_range, text)
print("'{n,m}' (1 to 3 b's) matches:", matches_range)
# This matches "abc" (1 b), "abbc" (2 b), "abbbc" (3 b),
# but not "abbbbc" (4 b).


# 7) Greedy vs non-greedy (lazy) quantifiers
#    By default, *, +, {n,m} are "greedy": they match as much as possible.
#    Adding ? after them makes them "non-greedy" (lazy), matching as little as possible.
html = "<tag>first</tag><tag>second</tag>"

# Greedy: <.*> tries to match from the first < to the last >
greedy_pattern = r"<.*>"
greedy_match = re.findall(greedy_pattern, html)
print("Greedy '<.*>' match:", greedy_match)

# Non-greedy: <.*?> stops as soon as it can and still make a valid match
lazy_pattern = r"<.*?>"
lazy_match = re.findall(lazy_pattern, html)
print("Non-greedy '<.*?>' matches:", lazy_match)
# Greedy result: one big string "<tag>first</tag><tag>second</tag>"
# Lazy result: '<tag>', '</tag>', '<tag>', '</tag>' separately.
