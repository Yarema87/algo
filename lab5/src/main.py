import os

def max_experience(levels, experience):
    dp = [[0] * (i + 1) for i in range(levels)]

    dp[0][0] = experience[0][0]

    for i in range(1, levels):
        for j in range(i + 1):
            dp[i][j] = experience[i][j] + max(dp[i - 1][j - 1] if j > 0 else 0, dp[i - 1][j] if j < i else 0)
    max_exp = max(dp[levels - 1])
    return max_exp

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, 'career.in')
    output_file_path = os.path.join(script_dir, 'career.out')

    with open(input_file_path, 'r') as file:
        levels = int(file.readline())
        experience = [list(map(int, file.readline().split())) for _ in range(levels)]

    result = max_experience(levels, experience)

    with open(output_file_path, "w") as file_out:
        file_out.write(str(result))
