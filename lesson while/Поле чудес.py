x = y = 0
step_y = 1
step_x = 0
while (cmd := input()) != 'СТОП':
    if cmd == 'шаг':
        x += step_x
        y += step_y
    elif cmd == 'направо':
        if step_y == 1 and step_x == 0:
            step_y = 0
            step_x = 1
        elif step_y == 0 and step_x == 1:
            step_y = -1
            step_x = 0
        elif step_y == -1 and step_x == 0:
            step_y = 0
            step_x = -1
        elif step_y == 0 and step_x == -1:
            step_y = 1
            step_x = 0
    elif cmd == 'налево':
        pass
print(x, y)
