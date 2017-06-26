"""The coin change problem using dynamic programming"
def CoinChange(curr_sum, coins, index, memo):
    if curr_sum == 0:
        return 1
    if curr_sum < 0:
        return 0
    if index >= len(coins):
        return 0
   
    if index in memo and curr_sum in memo[index]:
        return memo[index][curr_sum]
    
    total_ways = 0
    curr_coin_sum = 0
    while(curr_coin_sum <= curr_sum):
        total_ways += getWays(curr_sum - curr_coin_sum, coins, index+1, memo)
        curr_coin_sum += coins[index]
    if index not in memo:
        memo[index] = {}
    memo[index][curr_sum] = total_ways
    return memo[index][curr_sum]
    
"""My iterative solution to "possibleSums" on CodeFights""" 
def possibleSums(coins, quantity):
    sums_for_index = {-1:{0:1}}
    
    for index in range(0, len(coins)):
        sums_for_index[index] = {}
        for past_sum in list(sums_for_index[index-1]):
            sums_for_index[index][past_sum] = 1
            for q in range(0, quantity[index]+1):
                sums_for_index[index][past_sum+coins[index]*q] = 1
    
    return len(sums_for_index[len(coins)-1].items())-1
