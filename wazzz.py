import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import numpy as np

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor App")

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.blur_button = tk.Button(self.root, text="Apply Gaussian Blur", command=self.apply_gaussian_blur)
        self.blur_button.pack()

        self.gray_button = tk.Button(self.root, text="Convert to Grayscale", command=self.convert_to_grayscale)
        self.gray_button.pack()

        self.draw_line_button = tk.Button(self.root, text="Draw Line", command=self.draw_line)
        self.draw_line_button.pack()

        self.show_red_button = tk.Button(self.root, text="Show Red Channel", command=lambda: self.show_channel('r'))
        self.show_red_button.pack()

        self.show_green_button = tk.Button(self.root, text="Show Green Channel", command=lambda: self.show_channel('g'))
        self.show_green_button.pack()

        self.show_blue_button = tk.Button(self.root, text="Show Blue Channel", command=lambda: self.show_channel('b'))
        self.show_blue_button.pack()

        self.crop_button = tk.Button(self.root, text="Crop Image", command=self.crop_image)
        self.crop_button.pack()

        self.average_button = tk.Button(self.root, text="Apply Average Filter", command=self.apply_average_filter)
        self.average_button.pack()

        self.draw_circle_button = tk.Button(self.root, text="Draw Circle", command=self.draw_circle)
        self.draw_circle_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            self.original_image = image.copy()
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def apply_gaussian_blur(self):
        if hasattr(self, 'original_image'):
            blurred_image = self.original_image.filter(ImageFilter.GaussianBlur(radius=2))
            self.display_image(blurred_image)

    def convert_to_grayscale(self):
        if hasattr(self, 'original_image'):
            grayscale_image = self.original_image.convert("L")
            self.display_image(grayscale_image)

    def draw_line(self):
        if hasattr(self, 'original_image'):
            drawn_image = self.original_image.copy()
            draw = ImageDraw.Draw(drawn_image)
            draw.line([(20, 50), (100, 150)], fill="red", width=3)
            del draw
            self.display_image(drawn_image)

    def show_channel(self, channel):
        if hasattr(self, 'original_image'):
            r, g, b = self.original_image.split()
            if channel == 'r':
                channel_image = Image.merge('RGB', (r, r, r))
            elif channel == 'g':
                channel_image = Image.merge('RGB', (g, g, g))
            elif channel == 'b':
                channel_image = Image.merge('RGB', (b, b, b))
            self.display_image(channel_image)

    def display_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def crop_image(self):
        if hasattr(self, 'original_image'):
            x1, y1 = map(int, input("Enter the top-left coordinates of the crop area: ").split())
            x2, y2 = map(int, input("Enter the bottom-right coordinates of the crop area: ").split())
            cropped_image = self.original_image.crop((x1, y1, x2, y2))
            self.display_image(cropped_image)

    def apply_average_filter(self):
        kernel_size_entry = tk.Entry(self.root)
        kernel_size_entry.pack()

        apply_button = tk.Button(self.root, text="Apply", command=lambda: self.apply_average_filter_action(kernel_size_entry))
        apply_button.pack()

    def apply_average_filter_action(self, kernel_size_entry):
        kernel_size = int(kernel_size_entry.get())
        # Здесь продолжается ваш код для применения среднего фильтра с заданным размером ядра

    def draw_circle():
    center_x = int(center_x_entry.get())
    center_y = int(center_y_entry.get())
    radius = int(radius_entry.get())
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='black')

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

center_x_entry = tk.Entry(root)
center_y_entry = tk.Entry(root)
radius_entry = tk.Entry(root)

draw_button = tk.Button(root, text="Draw Circle", command=draw_circle)
draw_button.pack()

center_x_entry.pack()
center_y_entry.pack()
radius_entry.pack()

root = tk.Tk()
app = ImageProcessorApp(root)
root.mainloop()