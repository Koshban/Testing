'''

'''

def draw_line(tick_length:int, tick_label: str = ''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(centre_length: int):
    if centre_length > 0:
        draw_interval( centre_length=centre_length - 1)  # Top ticks
        draw_line(centre_length)                         # Centre tick
        draw_interval( centre_length=centre_length - 1)  # Bottom tick

def draw_ruler(num_of_inches: int = 12, major_length: int = 4):
    draw_line(major_length, '0')
    for j in range(1, num_of_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == "__main__":
    draw_ruler()