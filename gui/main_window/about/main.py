from pathlib import Path
from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def about():
    About()
class About(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=798,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            36.0,
            43.0,
            anchor="nw",
            text="JailMaster was created by",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 24.0, image=self.image_image_1)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(390.0, 205.0, image=self.image_image_3)

        self.canvas.create_text(
            252.0,
            111.0,
            anchor="nw",
            text="Tinkerer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        self.canvas.create_text(
            252.0,
            127.0,
            anchor="nw",
            text="Jayesh",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            252.0,
            160.0,
            anchor="nw",
            text="Parmar",
            fill="#5E95FF",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_rectangle(
            252.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(489.0, 144.0, image=self.image_image_5)

        self.canvas.create_text(
            231.0,
            352.0,
            anchor="nw",
            text="© Jayesh, All rights reserved",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        # self.canvas.create_text(
        #     246.0,
        #     372.0,
        #     anchor="nw",
        #     text="Open sourced under the MIT license",
        #     fill="#5E95FF",
        #     font=("Montserrat Bold", 16 * -1),
        # )

        self.canvas.create_text(
            252.0,
            207.0,
            anchor="nw",
            text="An AI enthusiast and a data science student,",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            252.0,
            223.0,
            anchor="nw",
            text="Jayesh enjoys immersing himself in the world of",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            252.0,
            239.0,
            anchor="nw",
            text="technology. He can often be found in",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            252.0,
            255.0,
            anchor="nw",
            text="reality, engaging in related activities or watching",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            252.0,
            271.0,
            anchor="nw",
            text="popular movies, anime and series.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        # self.canvas.create_text(
        #     56.0,
        #     207.0,
        #     anchor="nw",
        #     text="A tech-nerd and a freelance programmer,",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )

        # self.canvas.create_text(
        #     56.0,
        #     223.0,
        #     anchor="nw",
        #     text="Jayesh likes to kill his time in a world of",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )

        # self.canvas.create_text(
        #     56.0,
        #     239.0,
        #     anchor="nw",
        #     text="computers. He can often be found in",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )

        # self.canvas.create_text(
        #     56.0,
        #     255.0,
        #     anchor="nw",
        #     text="reality, walking his dog or watching",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )

        # self.canvas.create_text(
        #     56.0,
        #     271.0,
        #     anchor="nw",
        #     text="Star Wars.",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
