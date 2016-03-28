# What
A python program which solves `abcd-efgh=ijkl-mnop=qqqqq` problem.
- Fixed width of 4 
- Using `itertools.permutations`
- Brute force
- Only problem with base >= 17 can be solved

# Assumptions
- `q = 1`
- `a`, `e`, `i`, `m` will not be 0
- Lower bound of search space of `mnop` is `2034` (a width 5 version will be `20345` and so on)

# Methodology
1. Enumerate all `mnop` (2034, base ^ width)
2. Let `ijkl = qqqqq - mnop`
3. Filter combinations of `ijkl`, `mnop` that has distinct digits and does not contain 1
4. Generate set of digits which is unused in `ijkl`, `mnop` and `qqqqq` (always be 1)
5. Brute force by permutations

# Performance
Multithread (or multiprocessing) support is implemented to have more brutal brute force. For a monsterous home PC that has 32 cores of CPU (64 threads with HT on), the performance is barely acceptable.
- 17: 2.7s
- 18: 14s
- 19: 2m
- 20: 8m
- 21: did not run, assumed to be 20-30m
