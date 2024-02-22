import turtle


def koch_curve(t, order, size):
    """
    Generates a Koch curve using turtle graphics.

    Parameters:
    t (turtle.Turtle): The turtle object to draw the curve.
    order (int): The order of the curve.
    size (int): The size of the curve.

    Returns:
    None
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    """
    Draw a Koch curve of a given order and size using the turtle graphics library.

    Parameters:
    - order: an integer representing the order of the Koch curve
    - size: an integer representing the size of the Koch curve (default is 300)

    Returns:
    This function does not return anything.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3 ** 0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


# Виклик функції
draw_koch_curve(3)
