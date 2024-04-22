import snake_head
import snake_body
import snake_point
from tkinter import *

tk_width = 1000
tk_height = 500
text_h = 40
text_w = tk_width
text_state = "DISABLED"
geometry_str = str(tk_width) + "x" + str(tk_height + text_h)
stop = 0
stopped = 0
speed = 100
bodies = []
state = "game"
func_name = ""
tocolor = 0

root = Tk()
canvas = Canvas(root, width=tk_width, height=tk_height)
canvas.config(background="white")
canvas.bind('<Button-1>', lambda event, x="game": on_click(event, x))
canvas.pack()


def make_point_d():
    point1.set_coordinates(tk_width, tk_height)
    point1.draw(canvas)


def make_point_e():
    point1.erase(canvas)
    make_point_d()


head1 = snake_head.Head()
point1 = snake_point.Point()
make_point_d()


def main():
    global stop, stopped
    canvas.delete("all")
    point1.draw(canvas)
    head1.move(head1.course, head1.real_course)
    head1.draw(canvas)
    if stop == 0:
        root.after(speed, main)
    elif stop == 1:
        global stopped
        stopped = 1
    if head1.pos_x == point1.pos_x and head1.pos_y == point1.pos_y:
        bodies.append(snake_body.Body())
        make_point_d()
        root.after(speed, color_tail)

    for body in bodies:
        if head1.pos_x == body.pos_x and head1.pos_y == body.pos_y:
            print("crash!")
            stop = 1
            stopped = 1
            root.after(2000, start_new_game())
            break

    for count, obj in enumerate(bodies):
        if count == 0:
            obj.old_pos_x = obj.pos_x
            obj.old_pos_y = obj.pos_y
            obj.pos_x = head1.old_pos_x
            obj.pos_y = head1.old_pos_y
            obj.draw(canvas)
            obj.color = obj.real_color
        else:
            obj.old_pos_x = obj.pos_x
            obj.old_pos_y = obj.pos_y
            obj.pos_x = bodies[count - 1].old_pos_x
            obj.pos_y = bodies[count - 1].old_pos_y
            obj.draw(canvas)
            obj.color = obj.real_color

    head1.old_pos_x = head1.pos_x
    head1.old_pos_y = head1.pos_y


def color_tail():
    global tocolor
    try:
        if tocolor >= 0:
            bodies[tocolor].color = "yellow"
        else:
            bodies[0].color = "red"
    except:
        pass
    tocolor += 1
    if tocolor != len(bodies) and not (stopped == 1 or stop == 1):
        root.after(speed, color_tail)
    else:
        tocolor = 0


def on_key_press(event, press):
    global stop
    global stopped
    global speed
    global state
    if state == "game":
        if event.char == "a" and head1.real_course != "right":
            head1.course = "left"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif event.char == "d" and head1.real_course != "left":
            head1.course = "right"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif event.char == "w" and head1.real_course != "down":
            head1.course = "up"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif event.char == "s" and head1.real_course != "up":
            head1.course = "down"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif event.char == "o":
            stop = 1
            stopped = 1
        elif event.char == "t":
            bodies.append(snake_body.Body())
        elif event.char == "+":
            speed -= 10
        elif event.char == "-":
            speed += 10
        elif event.char == "p":
            make_point_e()
    if state == "text":
        if press == "text_enter":
            global func_name
            func_name2 = input1.get("1.0", "2.0")
            func_name = input1.get("2.0", "end-1c")
            input1.delete("1.0", "end-1c")
            input1.delete("0.0", "end-1c")
            if func_name == "":
                func_name2 = func_name2[:-1]
                do_func(func_name2)
            else:
                do_func(func_name)


def clear_map():
    canvas.delete("all")


def do_func(func):
    global stop
    global stopped
    global bodies
    global speed
    if func[0] == "p" and func[1] == "o" and func[2] == "s":
        ch = ""
        buff = 4
        first_num = ""
        second_num = ""
        while ch != ",":
            ch = func[buff]
            buff += 1
            if ch != " " and ch != ",":
                first_num += ch
            if ch == ",":
                buff += 1
                break
        while buff < len(func):
            ch = func[buff]
            buff += 1
            if ch != " ":
                second_num += ch
        first_num = int(first_num)
        second_num = int(second_num)
        head1.erase(canvas)
        head1.pos_x = first_num
        head1.pos_y = second_num
        head1.draw(canvas)
    else:
        if func == "stop":
            stop = 1
            stopped = 1
        if func == "go":
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif func == "reset":
            head1.erase(canvas)
            head1.pos_x = 100
            head1.pos_y = 100
            head1.draw(canvas)
        elif func == "point":
            make_point_e()
        elif func == "body++":
            bodies.append(snake_body.Body())
        elif func == "body--":
            bodies = bodies[0:len(bodies) - 1]
        elif func == "speed++":
            speed -= 10
        elif func == "speed--":
            speed += 10
        elif func == "left" and head1.course != "right":
            head1.course = "left"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif func == "right" and head1.course != "left":
            head1.course = "right"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif func == "up" and head1.course != "down":
            head1.course = "up"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif func == "down" and head1.course != "up":
            head1.course = "down"
            stop = 0
            if stopped == 1:
                root.after(speed, main)
            stopped = 0
        elif func == "ppos":
            input1.insert(END, "x: " + str(point1.pos_x) + ", y: " + str(point1.pos_y))


def on_click(event, *args):
    global state
    for a in args:
        if a == "text":
            state = "text"
            input1.config(state="normal")
        elif a == "game":
            state = "game"
            input1.config(state="disabled")


def start_new_game():
    global stop, stopped
    for n in range(len(bodies) - 1, -1, -1):
        del bodies[n]
    head1.pos_x = 200
    head1.pos_y = 200
    head1.course = "right"
    stop = 0
    stopped = 0


input1 = Text(root, height=text_h, width=text_w, bg="black", fg="white", insertbackground="white")
input1.bind('<Button-1>', lambda event, x="text": on_click(event, x))
input1.bind('<Return>', lambda event, x="text_enter": on_key_press(event, x))
input1.pack()

root.geometry(geometry_str)
root.title("root")
root.bind('<KeyPress>', lambda event, x="pass": on_key_press(event, x))
root.after(0, main)
root.mainloop()
