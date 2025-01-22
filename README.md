<h1 align="center">Movie_Py - Face Recognition</h1>

<h3 align="center"><b>Movie_Py - Face Recognition</b> This is a fastest ever python program use to find movies based on the actor/actress image that you share with in a second! For more feature read README</h3>
<h3 align = 'center'>

![Static Badge](https://img.shields.io/badge/Artificial_Intellegence%20-%20green)
![Static Badge](https://img.shields.io/badge/Python-blue)
![Static Badge](https://img.shields.io/badge/TKinter-blue)
![Static Badge](https://img.shields.io/badge/Face_Recognition-yellow)
</h3>

### Last updated : `18-01-2025 19:30 PM (IST)`

## Introduction to Movie_Py - Face Recognition

Have you ever come across movie clips on social media platforms, such as reels or shorts, and wondered about the movie name? More often than not, the information you're looking for isn't easily accessible, leaving you scrolling through the comment section in search of answers.

With **Movie_Py - Face Recognition**, you no longer have to waste time. This tool allows you to quickly identify movies by recognizing the faces of actors and actresses. Simply take a screenshot (or multiple screenshots of different actors/actress, as long as the faces are visible) of the actors/actresses and upload them to **Movie_Py - Face Recognition**. The platform will then provide you with a list of all the movies they have starred in together.

If you already know the names of the actors/actresses, you can either download their images from the internet or directly input their names into **Movie_Py - Face Recognition** for accurate movie results.

Additionally, if you're curious about the films in which your favorite actors or actresses have appeared together, **Movie_Py - Face Recognition** makes it easy to find this information.

Thank you for using **Movie_Py - Face Recognition**!


## Installation:

###  *If you are cloning this repository then follow the following steps :*

**Step 1 :**

- Clone the repository in your git repository
```bash
  git clone https://github.com/codex-yv/Movie_py---Face-Recognition.git
```
- After you cloned the repository make sure that you **don't run the code in the same repository (Folder) as it is a .git folder and my cause some unwanted errors.**
- Copy the code in the not .git folder *(folder that don't have `.git` folder in it)* . And we are ready to move on to the next step.

**(`.git` folder remains hidden make sure that you have selected the `show hidden folders`)**

**Step 2 :**

- Open command prompt in the folder named **`dlib-must`**, it consist the following dlib files:
<ul>
    <b>
    * dlib-19.19.0-cp37-cp37m-win_amd64.whl --py version 3.7 <br>
    * dlib-19.19.0-cp38-cp38-win_amd64.whl --py version 3.8<br>
    * dlib-19.22.1-cp39-cp39-win_amd64.whl --py version 3.9<br>
    * dlib-19.22.99-cp310-cp310-win_amd64.whl --py version 3.10<br>
    * dlib-19.24.1-cp311-cp311-win_amd64.whl --py version 3.11 
    </b>
</ul>

- Now in the command prompt install the dlib file which is matching your python version ( for me it is 3.10 )

```bash
  pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
```
Now we are good to go for next step. *(make sure you have installed the dlib file otherwise program will not work)*

**Step 3 :**

- Come to the root folder where **`setup.py`** file is stored.

- **Make sure that you are connected to the internet**.
- Open the Command prompt the current folder path and run the following command :

```Python
  py setup.py
```
- It will install all the necessary packages needed to run the code.

*Now we are ready to move on the final step.*

**Step 4 :**

- **Make sure that you have completed all the above steps.**
- Open command prompt in the path having **`Movie_Py.py`** and run the following command :

```Python
  py Movie_Py.py
```

### For those who are downloading the code in the ZIP format.

- Make sure you ***extract the code on the desktop***
- Follow all the above steps ***expect step 1***

## Screenshots

- After you run the following :

```Python
  py Movie_Py.py
```
<img src="zScreenshots\\1.png" alt="main" width="820" height='450'/>

- **When your choosen option is 1**

<img src="zScreenshots\\1A.png" alt="before" width="450" height='150'/>

- **When your choosen option is 2**

<img src="zScreenshots\\2.png" alt="before" width="450" height='200'/>

*Select images of actor/actress to recognise their face and find movies in which they have appeared together.* (`You can select multiple images.`)

- **Press Done** when you have selected all the images.

<img src="zScreenshots\\3.png" alt="before" width="720" height='450'/>

- **`Close the image after the match for further processing.`**

<img src="zScreenshots\\4.png" alt="before" width="720" height='450'/>

- And here is the **Final Result**

<img src="zScreenshots\\5.png" alt="before" width="450" height='150'/>


## Errors : 
 - For any **`Error/bug/enhancement/etc.`** related problem submit your issue in the issue section.

 <a href="https://github.com/codex-yv/Movie_py---Face-Recognition/issues">Click here to open issue tab</a><br>

 - After you press done and selected image with facial landmark is not being poped up and encountering some open-cv related Errors then run the follwing code.


```Python

  pip uninstall opencv-python
  pip uninstall opencv-contrib-python
  pip install opencv-contrib-python

```

 ## Future Developments
  - Currently the app work on a low data. As we only have some movies ranging from 2015 - 2024. So you may not find some actor/actress or movies. In future you will get 100% result.

  - Advance GUI will be added for more user friendly experience.

  - **One step installation and One step to use**

## Version

***[Note] : When ever you clone/download newer version replace your 1A folder with your older one ( when you cloned for time.) as it is now trained as per your uses!***

### 0.0.1
- It's just the beginning

### 0.0.2
 - Added new movies (bollywood)
 - Fixed UnboundLocal error
 - Added new actor/actress

## Contributing

Contributions are always welcome!

Contribution Branch: `should be same as issue title seperated by '/' and '_' and no other special chars. `.

Please adhere to this project's `Contribution Branch`.

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/youraj-verma-929383317/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="youraj verma" height="30" width="40" /></a>
<a href="https://instagram.com/y.o.u.r.a.j__v.e.r.m.a" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="y.o.u.r.a.j__v.e.r.m.a" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> </p>

<p><img align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=codex-yv&show_icons=true&locale=en&layout=compact" alt="codex-yv" /></p>
