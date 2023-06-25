#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

# Function to perform drug detection and analysis on the selected image
def process_image():
    # Get the selected image path from the dropdown box
    image_path = image_paths.get()

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Perform drug detection and component analysis on the image
    # Your code here
    # Example: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Example: Calculate the histogram of the grayscale image
    histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Example: Visualize the histogram using Matplotlib
    plt.figure()
    plt.plot(histogram)
    plt.title('Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

    # Example: Display information about the particular medicine
    medicine_info = get_medicine_info()
    print("Medicine Information:")
    print(f"Name: {medicine_info['name']}")
    print(f"Dosage: {medicine_info['dosage']}")
    print(f"Side Effects: {medicine_info['side_effects']}")
    print(f"Warnings: {medicine_info['warnings']}")

    # Display the results
    display_image(gray)

# Function to display the image
def display_image(image):
    # Convert the OpenCV image to PIL format
    image_pil = Image.fromarray(image)

    # Resize the image for better visualization
    image_pil = image_pil.resize((400, 400))

    # Create an ImageTk object to display in the GUI
    image_tk = ImageTk.PhotoImage(image_pil)

    # Update the image label in the GUI
    image_label.configure(image=image_tk)
    image_label.image = image_tk

# Function to get information about the particular medicine
def get_medicine_info():
    # Retrieve medicine information from a data source
    # Your code here
    # Example: Retrieve information from a dictionary
    medicine_info = {
        'name': 'Medicine Name',
        'dosage': 'Dosage Information',
        'side_effects': 'Side Effects Information',
        'warnings': 'Warnings Information'
    }

    return medicine_info

# Create a Tkinter root window
root = tk.Tk()
root.title("Drug Detection and Analysis")

# Create a dropdown box to select the image
image_paths = tk.StringVar()
image_dropdown = tk.OptionMenu(root, image_paths, "Select Image")
image_dropdown.pack()

# Create a button to trigger image processing
process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack()

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Function to open the file dialog and populate the dropdown box with image paths
def select_image():
    # Prompt the user to select an image using the file dialog
    image_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg"), ("All Files", "*.*")])

    # Update the dropdown box with the selected image path
    image_paths.set(image_path)

# Create a button to open the file dialog
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack()

# Run the Tkinter event loop
root.mainloop()


# In[ ]:




