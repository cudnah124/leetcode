"""
MARIO River Crossing (English problem description)

MARIO is on the left bank of a river and the flagpole (goal) is on the right bank.
There are N wooden piles (numbered 1..N) in the river that Mario can use to cross.
From pile i Mario can jump to i+1, i+2, or i+3.

Pile types (Ai in {0,1,2}):
  - Ai = 0 : good pile (normal).
  - Ai = 1 : unstable pile. Rules:
      * Mario can only step onto pile i from pile i-1 (i.e., arrival step must be 1).
      * From pile i Mario can move to i+1 or i+2 (i.e., outgoing step 3 is not allowed).
  - Ai = 2 : rotten pile. Mario cannot stand on it at all (cannot land there).

Mario starts at the left bank (position 0) and wants to reach the right bank (position N+1).
He can only move forward (no backward moves).
Count the number of different ways Mario can reach the right bank.
Output only the last 9 digits (i.e., result modulo 10^9).

Input format:
  - Line 1: N (1 <= N <= 1000)
  - Line 2: A1 A2 ... AN  (each Ai is 0,1,or 2)

Output:
  - One integer: number of ways modulo 10^9.
"""

arr = [0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2]
def count_ways(arr):
    n = len(arr)
    #Dynamic Programming
    dp = [0] * (n + 2)
    dp[0] = 1#Set left side has 1 way to reach

    for pos in range(1, n + 2):  # 1 -> right side
        total = 0 #steps
        for step in (1, 2, 3): #allow 1, 2, 3 steps
            prev = pos - step
            if prev < 0:
                continue
            # check if prev can be reached by 'step'
            if prev == 0:
                ok_from_prev = True # always can reach left bank
            else:
                prev_type = arr[prev - 1]  # check prev type
                if prev_type == 2:
                    ok_from_prev = False   # cannot stand on prev
                elif prev_type == 1 and step == 3:
                    ok_from_prev = False   # unstable pile does not allow step 3
                else:
                    ok_from_prev = True
            if not ok_from_prev: #if can not reach
                continue

            # check if pos can be reached by 'step'
            if pos == n + 1:
                ok_to_pos = True  # check if right bank has reached
            else:
                pos_type = arr[pos - 1] # check pos type
                if pos_type == 2:
                    ok_to_pos = False  # cannot stand on pos
                elif pos_type == 1 and step != 1:
                    ok_to_pos = False  # unstable pile just can go by 1 'step'
                else:
                    ok_to_pos = True
            if not ok_to_pos: #if can not reach, don't count total
                continue

            total += dp[prev]
        dp[pos] = total
    return dp[n + 1]

print(count_ways(arr) % 1000000000)
