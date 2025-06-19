def moving_average(data, window_size):
    if window_size > len(data):
        return []

    moving_avg = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        avg = sum(window) / window_size
        moving_avg.append(round(avg, 2))
    return moving_avg

# Example revenue data
revenue = [100, 150, 130, 170, 160, 180]
print(moving_average(revenue, 3))  # Output: [126.67, 150.0, 153.33, 170.0]