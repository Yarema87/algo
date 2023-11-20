def max_experience(levels, experience):
    # Initialize a 2D list for storing maximum experience at each position
    dp = [[0] * (i + 1) for i in range(levels)]

    # Fill in the values for the first level
    dp[0][0] = experience[0][0]

    # Calculate maximum experience for each level
    for i in range(1, levels):
        for j in range(i + 1):
            dp[i][j] = experience[i][j] + max(dp[i - 1][j - 1] if j > 0 else 0, dp[i - 1][j] if j < i else 0)

    # Find the maximum experience among all positions in the last level
    max_exp = max(dp[levels - 1])

    return max_exp

# Reading input data
with open("career.in", "r") as file:
    levels = int(file.readline())
    experience = [list(map(int, file.readline().split())) for _ in range(levels)]

# Finding the maximum experience using the dynamic programming approach
result = max_experience(levels, experience)

# Writing the result to an output file
with open("career.out", "w") as file_out:
    file_out.write(str(result))
