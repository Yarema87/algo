import copy


def flood_fill(image, start, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[start[0]][start[1]]

    stack = [start]
    while stack:
        r, c = stack.pop()
        if image[r][c] == original_color:
            image[r][c] = new_color
            if r > 0 and image[r - 1][c] == original_color:
                stack.append((r - 1, c))
            if r < rows - 1 and image[r + 1][c] == original_color:
                stack.append((r + 1, c))
            if c > 0 and image[r][c - 1] == original_color:
                stack.append((r, c - 1))
            if c < cols - 1 and image[r][c + 1] == original_color:
                stack.append((r, c + 1))


original_image = [
    ["G", "G", "R", "G", "G"],
    ["G", "G", "G", "R", "G"],
    ["G", "R", "B", "B", "G"],
    ["G", "B", "G", "B", "R"],
    ["G", "G", "G", "G", "G"],
]

print("Original Image:")
for row in original_image:
    print(row)

image_copy = copy.deepcopy(original_image)

start_point = (2, 2)
new_color = "R"
flood_fill(image_copy, start_point, new_color)

start_point = (2, 1)
new_color = "W"
flood_fill(image_copy, start_point, new_color)

print("\nImage after Flood Fill:")
for row in image_copy:
    print(row)
