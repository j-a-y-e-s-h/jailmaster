from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *
import controller as db_controller

from .add_prison_allocate.gui import AddPrisonAllocate
from .view_prison_allocate.main import ViewPrisonAllocate
from .update_prison_allocate.main import UpdatePrisonAllocate

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def prison_allocate():
    PrisonAllocate()


class PrisonAllocate(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_pca_id = None
        self.prison_allocate_data = db_controller.get_prison_allocate()

        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddPrisonAllocate(self),
            "view": ViewPrisonAllocate(self),
            "edit": UpdatePrisonAllocate(self),
        }

        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)

    def refresh_entries(self):
        self.prison_allocate_data = db_controller.get_prison_allocate()
        self.windows.get("view").handle_refresh()
