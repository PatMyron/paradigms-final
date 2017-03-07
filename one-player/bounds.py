def check(x, y):
    left = x
    top = y
    right = x + 16
    bottom = y + 32

    if left < 0 or right > 6345:  # beginning and flag
        return False

    if top > 365:
        if (left > 2200 and right < 2263) or (left > 2746 and right < 2843) or (left > 4888 and right < 4950):  # gaps
            pass
        else:  # ground
            return False

    arrays = [
        # pipes
        [890, 333, 952, 397],
        [1209, 301, 1273, 397],
        [1464, 270, 1528, 396],
        [1816, 270, 1878, 398],
        [5208, 333, 5269, 397],
        [5719, 333, 5782, 397],
        # blocks
        [505, 270, 537, 300],
        [633, 270, 793, 300],
        [697, 140, 729, 173],
        [2456, 270, 2552, 300],
        [2551, 140, 2807, 173],
        [2905, 140, 3032, 173],
        [3000, 270, 3032, 300],
        [3191, 270, 3255, 300],
        [3384, 270, 3415, 300],
        [3480, 270, 3511, 300],
        [3576, 270, 3607, 300],
        [3480, 140, 3511, 173],
        [3768, 270, 3801, 300],
        [3864, 140, 3960, 173],
        [4086, 140, 4215, 173],
        [4119, 270, 4183, 300],
        [5368, 270, 5496, 300],
        [6329, 364, 6362, 397],
        # 1st staircase
        [4280, 365, 4407, 397],
        [4312, 333, 4407, 397],
        [4344, 300, 4407, 397],
        [4376, 269, 4407, 397],
        # 2nd staircase
        [4470, 365, 4599, 397],
        [4470, 333, 4567, 397],
        [4470, 300, 4535, 397],
        [4470, 269, 4503, 397],
        # 3rd staircase
        [4727, 365, 4888, 397],
        [4759, 333, 4888, 397],
        [4791, 300, 4888, 397],
        [4823, 269, 4888, 397],
        # 4th staircase
        [4950, 365, 5080, 397],
        [4950, 333, 5048, 397],
        [4950, 300, 5016, 397],
        [4950, 269, 4984, 397],
        # 5th staircase
        [5784, 365, 6073, 397],
        [5816, 333, 6073, 397],
        [5848, 300, 6073, 397],
        [5880, 269, 6073, 397],
        [5912, 237, 6073, 397],
        [5944, 205, 6073, 397],
        [5976, 173, 6073, 397],
        [6008, 140, 6073, 397]
    ]
    for array in arrays:
        if (right > array[0]) and (left < array[2]):
            if (bottom > array[1]) and (top < array[3]):
                return False

    return True
