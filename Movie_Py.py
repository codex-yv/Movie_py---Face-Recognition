import face_recognition
import numpy as np
import cv2
import os
import threading
import time
from colorama import Fore, Back, Style, init
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from movies import MovieFinder
import re

init()
Global_result = [True]
Global_add_new_img = [False]

actors_found_list = []
# Function to display image with facial landmarks in a separate thread
def display_image_with_landmarks(image_bgr):
    cv2.imshow('Image with Facial Features', image_bgr)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the image window

# Function to read a facial encoding from a txt file
import numpy as np

# Function to read and clean facial encoding from a txt file
def read_encoding_from_txt(file_path):
    with open(file_path, 'r') as file:
        encoding_str = file.read().strip()  # Read the content and strip extra spaces/newlines

        # Handle problematic formats (e.g., remove brackets or unwanted characters)
        if encoding_str.startswith('[') and encoding_str.endswith(']'):
            encoding_str = encoding_str[1:-1]  # Remove the square brackets

        # Now split by spaces instead of commas
        encoding_list = encoding_str.split()  # This splits by any whitespace (including spaces and tabs)

        # Convert each element into a float, ensuring that we handle any errors gracefully
        try:
            encoding_array = np.array([float(x.strip()) for x in encoding_list])
        except ValueError as e:
            print(f"Error converting encoding to float: {e}")
            print(f"Problematic encoding string: {encoding_str}")
            raise  # Re-raise the error for debugging

        return encoding_array


# Compare the known image with the target directory of images (on-the-fly)
def process_images(base_directory, known_image_encoding, file_extensions):
    global Global_result, Global_add_new_img, actors_found_list
    start_time = time.time()  # Start timer for the process_images function
    for folder_name in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder_name)
        
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                
                # Check if the file is a .txt file (for encodings)
                if file_name.lower().endswith('.txt'):
                    print(Fore.LIGHTBLUE_EX + f'Comparing encoding from {folder_name}...')
                    file_name_without_ext = os.path.splitext(file_name)[0]
                    # Read the encoding from the text file
                    try:
                        unknown_encoding = read_encoding_from_txt(file_path)
                    except Exception as e:
                        print(Fore.RED + Back.WHITE + "Error reading encoding from file:", Fore.BLACK + file_name, Style.RESET_ALL + '')
                        print(e)
                        continue  # Skip to the next file
                    
                    # Compare the known image encoding with the current unknown encoding
                    result = face_recognition.compare_faces([known_image_encoding], unknown_encoding)
                    distance = face_recognition.face_distance([known_image_encoding], unknown_encoding)[0]

                    if result[0] == True:
                        if distance < 0.45:
                            elapsed_time = time.time() - start_time  # Calculate elapsed time
                            print(Fore.GREEN + f'Face matched: {folder_name}', Fore.CYAN + f'{distance}', Style.RESET_ALL + '')
                            print(Fore.YELLOW + f'Time taken to find match: {elapsed_time:.2f} seconds', Style.RESET_ALL)
                            print()
                            actors_found_list.append(file_name_without_ext)
                            print(Fore.WHITE+Back.RED+Style.BRIGHT+'Close the image to scan next image if given or for further actions!',Style.RESET_ALL+'')
                            Global_result = [False]
                            Global_add_new_img = [False]
                            print()
                            break
                        else:
                            print(Fore.YELLOW + f"Match with low accuracy: {folder_name}", Fore.CYAN + f'{distance}', Style.RESET_ALL + '')
                            print()
                            result = [False]
                    else:
                        print(Fore.RED + f'Not matched: {folder_name}', Fore.CYAN + f'{distance}', Style.RESET_ALL + '')
                        print()

        if result[0] == True:
            break
        
    if result[0] == False:   
        print("Image Not Found Sorry!")
        Global_result = [True]
        Global_add_new_img = [True]

# Load the known image and compute its encoding
def starter(image_get):
    global Global_result, Global_add_new_img
    image = face_recognition.load_image_file(image_get)
    try:
        image_encoding = face_recognition.face_encodings(image)[0]
    except IndexError:
        print(Fore.RED +Back.WHITE + "No face found in image",Style.RESET_ALL+'')
    # Resize the image to 480px width
    height, width = image.shape[:2]
    new_width = 480
    new_height = int((new_width / width) * height)
    image = cv2.resize(image, (new_width, new_height))

    # Convert the image from RGB to BGR for OpenCV
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Find the face locations in the known image and mark them
    face_location = face_recognition.face_locations(image)
    for (top, right, bottom, left) in face_location:
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)

    # Draw landmarks
    face_landmark_list = face_recognition.face_landmarks(image)
    facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge', 'nose_tip', 'right_eye', 'left_eye', 'top_lip', 'bottom_lip']
    for face_landmarks in face_landmark_list:
        for facial_feature in facial_features:
            for point in face_landmarks[facial_feature]:
                image_bgr = cv2.circle(image_bgr, point, 2, (255, 60, 170), 2)
    if len(face_location)<2:
        # Start the image display in a separate thread
        display_thread = threading.Thread(target=display_image_with_landmarks, args=(image_bgr,))
        display_thread.start()

        # Define image extensions globally
        file_extensions = ['.txt']  # We're only looking for .txt files with encodings
        max_workers = os.cpu_count() 
        print(max_workers)

        # Use multithreading to speed up face recognition across multiple encodings
        Folder_list_root = ['1A','Bhojpuri1', 'Bollywood1', 'Hollywood1', 'Tollywoodd1', 'webseries_west1', 'webseries-ind1']

        for search in Folder_list_root:
            if Global_result[0] == True:
                print(Fore.YELLOW +Back.CYAN + "Searching in :", Fore.RED+f'{search}',Style.RESET_ALL+'')
                with ThreadPoolExecutor(max_workers=4) as executor:
                    try:
                        executor.submit(process_images, search, image_encoding, file_extensions)
                    except UnboundLocalError:
                        print(Fore.WHITE+Back.RED+Style.BRIGHT+'Use clear Image!',Style.RESET_ALL+'')
                        break
            else:
                break
            
        if Global_add_new_img[0] == True:
            print()
            confirmation = input(Fore.YELLOW+"Do you want to add this image(y/n):")
            if confirmation == 'y':
                new_image_name = input("Give the Custom Name to image (don't add any extention) : ")
                print(Style.RESET_ALL+'')
                unknown_image = face_recognition.load_image_file(image_get)
                file_name_without_ext = new_image_name
                saves_path = os.path.join('1A','new data',file_name_without_ext)
                try:                    # Compute encoding for each image on-the-fly
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    print(Fore.CYAN+Back.WHITE+"encoding successful: ", saves_path,Style.RESET_ALL+'')
                except (IndexError,UnboundLocalError):
                    print(Fore.RED + Back.WHITE + "No face found in image or face is not clear:", Fore.BLACK + saves_path, Style.RESET_ALL + '')

                os.makedirs(os.path.dirname(saves_path), exist_ok=True)

                # Open a file in write mode ('w')
                with open(saves_path+'.txt' , "w") as file:
                    # Write text to the file
                    try:
                        file.write(str(unknown_encoding))
                    except UnboundLocalError:
                        print(Fore.RED + Back.WHITE + "No face found in image or face is not clear:", Fore.BLACK + saves_path, Style.RESET_ALL + '')
                        print(Fore.WHITE+Back.RED+Style.BRIGHT+'Close the image to scan next image if given or for further actions!',Style.RESET_ALL+'')

                print(Fore.GREEN+"Text has been written to", saves_path + '.txt',Style.RESET_ALL+'')
            else:
                print(Fore.WHITE+Back.RED+Style.BRIGHT+'Close the image to scan next image if given or for further actions!',Style.RESET_ALL+'')
        else:
            pass
        

        # Wait for the display thread to finish (optional, but good practice)
        display_thread.join()
    else:
        print(Fore.RED +Back.WHITE + f"Found {len(face_location)} faces in a single photo> There should be one.",Style.RESET_ALL+'')
    


# starter(image_get='C:\\Users\\kumkum\\Pictures\\poco c31\\Camera\\bhv.jpg')

print(Fore.GREEN+Style.BRIGHT+'''

███████╗██╗   ██╗███████╗██╗   ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔════╝██║   ██║██╔════╝██╔══██╗
██████╗ ████████║█████╗  ██║   ██║█████╗  ██████╔╝
██╔══╝ ██╔══██║██╔══╝  ██║   ██║██╔══╝  ██╔══██╗
██████╗ ██║  ██║███████╗╚██████╔╝███████╗██║  ██║
╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

███████╗██╗  ██╗████████╗███████╗██████╗ ███████╗███████╗
██╔════╝██║  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝
██████╗ ██║  ██║   ██║   █████╗  ██████╔╝█████╗  █████╗  
╚═══██╗██║  ██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  
██████╔╝╚█████╔╝   ██║   ███████╗██║  ██║███████╗███████╗
╚═════╝  ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝

         ███╗   ███╗███████╗████████╗██╗██╗
         ████╗ ████║██╔════╝╚══██╔══╝██║██║
         ██╔██╗████║█████╗     ██║   ██║██║
         ██║╚██╔██║██╔══╝     ██║   ██║██║
         ██║ ╚═╝ ██║███████╗   ██║   ██║██║
         ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝
         ''',Style.RESET_ALL+'')

print(Fore.CYAN+"\t\tWelcome to MoviePy - The Movie Recognition Program!\n\tThis program identifies actors and their movies from images.\n\tSimply upload an image and get a list of movies starring the detected\n\tactors. It's like magic, but powered by technology! Let's begin...")



print()
print(Fore.YELLOW+"How would you like to find the movies:\n1) I know the names of Actors/Actress\n2) I don't know their names But i have their images.")
opt_input = input(Fore.CYAN+'\nEnter Your Choice ( Number ):')

if opt_input == '1':
    actor_name = input("\nEnter the actors name seperated by comma(,):")
    
    actor_name_list = actor_name.split(',')
    actor_name_list_formated = []
    
    for actors in actor_name_list:
        formated_actor = actors.title().strip()
        # print(formated_actor)
        actor_name_list_formated.append(formated_actor)
        
    actor_list = actor_name_list_formated
    # print(actor_list)
    movie_finder = MovieFinder()

    # Define the actors you are searching 

    # Find movies/web series with the specified actors
    print()
    movies_with_actors = movie_finder.find_movies_with_actors(actor_list)

    if len(movies_with_actors) != 0:  
        print(Fore.GREEN+"Movies Found:-")
        print("-----------------------------------")
        # Print the results
        for movie in movies_with_actors:
            print(movie)
        print("-----------------------------------")
        print(Style.RESET_ALL+'')
    else:
        print("Movie not found! or Wrong spelling of actors/actress")
    
elif opt_input == '2':
    path_list = []
    def select_images():
        global path_list
        # Open file dialog to select multiple image files
        file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All Files", "*.*")))
        
        if file_paths:
            # Update label with the selected file paths (joined by newline for clarity)
            label.config(text="Selected Image Paths:\n" + "\n".join(file_paths))
            
            # Print the file paths in the terminal
            print("Selected Image Paths:")
            for path in file_paths:
                print(path)
                path_list.append(path)
                
        else:
            label.config(text="No files selected")
            
    def recogniser():
        global path_list, Global_result
        for i in path_list:
            Global_result = [True]
            starter(image_get=i)
        root.destroy()
    # Create the main window
    root = tk.Tk()
    root.title("Multiple Image File Selector")
    root.geometry("400x230")
    label = tk.Label(root, text="Select Images of actors", font=('Bahnschrift Condensed',18))
    label.pack(pady=(10,0))
    label = tk.Label(root, text="(multiple images can be selected at a time!)", font=('arial',10,'bold'),
                    fg='red')
    label.pack(pady=(10,0))
    # Create a button to trigger file selection
    button = ctk.CTkButton(root, text="Select Images",font=('Bahnschrift',14), command=select_images,cursor='hand2',
                    fg_color='#148f77', text_color='white', height=30, width=70)
    button.pack(pady=10)
    button = ctk.CTkButton(root, text="Done",font=('Bahnschrift',14), command=recogniser,cursor='hand2',
                    fg_color='Green', text_color='white', height=30, width=70, hover_color='red')
    button.pack(pady=(0,10))

    # Create a label to display the selected file paths
    label = tk.Label(root, text="No files selected", font=('Cascadia Code',10),
                    width=50, anchor="w", justify="left",fg='white',bg='black')
    label.pack(pady=10)
    # Run the Tkinter event loop
    root.mainloop()
    act_final_list = []
    for act in actors_found_list:
        # a='Madhuri_dixit_1'
        act_name = re.sub(r'[_\d-]', ' ', act)

        # Split the string into words
        act_name1 = act_name.split()

        # Join the words and capitalize the first letter of each word
        act_final = ' '.join(act_name1).title()

        print(act_final)
        act_final_list.append(act_final)
    
    print()
    # print(act_final_list)
    print()
    actor_list = act_final_list
    if len(actor_list) != 0:
        movie_finder = MovieFinder()

        # Define the actors you are searching 

        # Find movies/web series with the specified actors
        movies_with_actors = movie_finder.find_movies_with_actors(actor_list)
        if len(movies_with_actors) != 0:  
            print(Fore.GREEN+"Movies Found:-")
            print("-----------------------------------")
            # Print the results
            for movie in movies_with_actors:
                print(movie)
            print("-----------------------------------")
            print(Style.RESET_ALL+'')
        else:
            print("Movie not found! or Wrong spelling of actors/actress")
    else:
        print("Movie Not Found!")
    
else:
    print("Option Not Available!")      