"""
Qno10: Moving Average
Calculate a moving average over a window of values.

Difficult words:
- moving average: average of each consecutive window
- window: fixed-size subset of data
- consecutive: following continuously in order
"""

data = [10, 20, 30, 40, 50, 60, 70]
window_size = 3

moving_averages = []
for i in range(len(data) - window_size + 1):
    window = data[i:i + window_size]
    avg = sum(window) / window_size
    moving_averages.append(avg)

print("Data:", data)
print("Window size:", window_size)
print("Moving averages:", moving_averages)
