# Movie Recognition and Movie Finder Program

### Overview:
This program helps you identify actors from images and find movies they have starred in. The program offers two modes of operation:
1. **Actor Name Search**: If you know the names of the actors/actresses, you can input their names to search for movies they have starred in.
2. **Image-Based Search**: If you have images of actors, the program can detect their faces and match them with known faces to find movies they appear in.

### Setup:
Before running the program, ensure that you have run the `setup.py` file. Following are the necessary dependencies installed by setup.py file:
1. **`face_recognition`** – for facial recognition tasks.
2. **`numpy`** – for handling arrays and numerical data.
3. **`cv2`** (OpenCV) – for image processing and display.
4. **`tkinter`** – for the graphical user interface.
5. **`concurrent.futures`** – to improve performance using multithreading.
6. **`colorama`** – for colored terminal output.

### Running the Program:
1. **Starting the Program**:
   - Upon running the script (`Movie_Py.py`), the program will ask how you would like to search for movies.
   - You can either provide the **names of the actors** or **images of the actors**.

2. **Actor Name Search**:
   - If you choose this option, you will be prompted to enter actor names (separated by commas). For example: 
     ```
     Madhuri Dixit, Shah Rukh Khan
     ```
   - The program will then search for movies featuring these actors.

3. **Image-Based Search**:
   - If you choose this option, you will be able to select images of actors from your file system.

   - If a match is found with a high enough confidence level, it will search for movies featuring the identified actors.


# Detailed Steps for Image-Based Search:
1. **Image Selection**:
   - Use the **"Select Images"** button in the GUI to choose multiple images of actors.
   - The program will display the selected image paths.

2. **Face Recognition**:
   - The program will process each selected image, detect faces, and match them with stored encodings.
   - If a match is found, the program will display a message indicating which actor was identified.
   - If no match is found, the program will ask if you want to add the new face encoding for future searches.

3. **Adding New Faces**:
   - If the program does not find a match, you have the option to add this new face by providing a custom name for the actor.
4. **Search for Movies**:
   - After detecting and identifying actors, the program will search for movies/web series that the actor has starred in using the `MovieFinder` class.
   - It will display a list of movies if found.

### Important Notes:
- The face matching is done using **face_recognition** library, which compares facial encodings for similarities.

- If no face is detected in an image, you will receive an error message.

### Troubleshooting:
1. **No Face Detected**:
 - If the program cannot detect a face in the provided image, ensure the image is clear and the face is visible.
