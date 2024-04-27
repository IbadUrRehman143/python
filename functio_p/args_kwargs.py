# def func(a, b, *args):
#     print(a, b, args)

def name(n):
    print(end=f"{n} ")
def age(a):
    print(end=f"{a} ")
def is_mail(g):
    print(end=f"{g} ")

def person(skin_color, **kwargs):
    # print(kwargs)
    print(end=f"{skin_color} ")
    name(kwargs["n"])
    age(kwargs["a"])
    is_mail(kwargs["g"])


# func("gulalam", "jee", "suroor", 4, 6)
# func(b=5, a=7)
person("asd", a = 5, g = "male", n = "gul")
person(a = 5, g = "male", skin_color="asd",  n = "gul")
    
# rect = [2, 5]
rect = {
    "width": 2,
    "height": 5,
    "color": "red",
    "stroke_width": 5
}

# print("width", rect["width"])
# print("height", rect["height"])
# print("s width", rect["stroke_width"])