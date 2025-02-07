class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Stores ball -> color mapping
        color_count = {}  # Tracks the number of balls using each color
        distinct_colors = set()  # Tracks distinct colors
        output = []

        for x, y in queries:
            # If the ball already has the same color, skip updating
            if x in ball_colors and ball_colors[x] == y:
                output.append(len(distinct_colors))
                continue
            
            # Remove old color if it exists
            if x in ball_colors:
                old_color = ball_colors[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    distinct_colors.discard(old_color)

            # Assign new color to ball
            ball_colors[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            distinct_colors.add(y)

            # Store the count of distinct colors after each query
            output.append(len(distinct_colors))

        return output