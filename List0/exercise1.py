def draw_triangle(height):
    if height < 2:
        print("You need at least 2 rows to make a triangle")
    else:
        for i in range(height, 0, -1):
            spaces = " " * (height - i)
            stars = "*" * (2*i - 1)
            print(spaces + stars)


height = int(input("Enter the height of the inverted triangle that you want to generate: "))
draw_triangle(height)

