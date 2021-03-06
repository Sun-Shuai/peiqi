# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/1/20 10:26 AM
@file: main.py
@desc: 画一个小猪佩奇
"""

from turtle import *


def draw_nose(x, y):
    pu()
    goto(x, y)
    pd()
    seth(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()

    pu()
    seth(90)
    fd(25)
    seth(0)
    fd(10)
    pd()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

    pu()
    seth(0)
    fd(20)
    pd()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def draw_head(x, y):
    color((255, 155, 192), "pink")
    pu()
    goto(x, y)
    seth(0)
    pd()
    begin_fill()
    seth(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    seth(161)
    circle(-300, 15)
    pu()
    goto(-100, 100)
    pd()
    seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def draw_ears(x, y):
    color((255, 155, 192), "pink")
    pu()
    goto(x, y)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    pu()
    seth(90)
    fd(-12)
    seth(0)
    fd(30)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def draw_eyes(x, y):
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)
    pd()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()

    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)
    pd()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()


def draw_cheek(x, y):
    color((255, 155, 192))
    pu()
    goto(x, y)
    pd()
    seth(0)
    begin_fill()
    circle(30)
    end_fill()


def draw_mouth(x, y):
    color(239, 69, 19)
    pu()
    goto(x, y)
    pd()
    seth(-80)
    circle(30, 40)
    circle(40, 80)


def draw_body(x, y):
    color("red", (255, 99, 71))
    pu()
    goto(x, y)
    pd()
    begin_fill()
    seth(-130)
    circle(100, 10)
    circle(300, 30)
    seth(0)
    fd(230)
    seth(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    seth(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()


def draw_hands(x, y):
    color((255, 155, 192))
    pu()
    goto(x, y)
    pd()
    seth(-160)
    circle(300, 15)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(0)
    pd()
    seth(-10)
    circle(-20, 90)

    pu()
    seth(90)
    fd(30)
    seth(0)
    fd(237)
    pd()
    seth(-20)
    circle(-300, 15)
    pu()
    seth(90)
    fd(20)
    seth(0)
    fd(0)
    pd()
    seth(-170)
    circle(20, 90)


def draw_foot(x, y):
    pensize(10)
    color((240, 128, 128))
    pu()
    goto(x, y)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)

    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(40)
    seth(0)
    fd(90)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)


def draw_tail(x, y):
    pensize(4)
    color((255, 155, 192))
    pu()
    goto(x, y)
    pd()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)


def setting():
    pensize(4)
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(200)


if __name__ == '__main__':
    setting()
    draw_nose(-100, 100)
    draw_head(-69, 167)
    draw_ears(0, 160)
    draw_eyes(0, 140)
    draw_cheek(80, 10)
    draw_mouth(-20, 30)
    draw_body(-32, -8)
    draw_hands(-56, -45)
    draw_foot(2, -177)
    draw_tail(148, -155)
    done()
