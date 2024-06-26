from turtle import Turtle,Screen


screen = Screen()
screen.title("Indian state Game")
image_path = "India_state.gif"
screen.addshape(image_path)
jkp = Turtle()
jkp.shape(image_path)


def get_mouse_click(x,y):
     print(x,y)
screen.onscreenclick(get_mouse_click)
screen.mainloop()

screen.exitonclick()