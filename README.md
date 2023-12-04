# Containerized App Exercise

## Badges

![Python build & test](https://github.com/software-students-fall2023/4-containerized-app-exercise-cantopop/actions/workflows/web.yml/badge.svg) 
![Python build & test](https://github.com/software-students-fall2023/4-containerized-app-exercise-cantopop/actions/workflows/mlc.yml/badge.svg) 

## Description

When taking notes in class, it can be stressful to try to jot down everything one sees on the slides the professor is presenting. This handy web app allows students to snap a quick picture of a slide that may be too much to write down manually, and the app will automatically convert the text in the image to a text note that can be later referenced. 


## Set-up Instructions

### Step 1, Clone the directory:
```
git clone https://github.com/software-students-fall2023/4-containerized-app-exercise-cantopop.git
```
### Step 2, Docker Compose:
```
docker-compose up --build
```
### Step 3, Access the web-app
Now, you can access http://localhost:5000/, remember to allow webcam for your webpage.
### Docker Hub
Alternatively, You can also pull the images from the docker hub
```
docker pull bailongzhao/easy_notes
```
Download the docker-compose file from here and run 
```
docker-compose up
```

## User-guide

### Main Screen
- The main screen serves as the dashboard and starting point.
- From here, you can navigate to 3 different functionalities: all notes, add note, search note.

### Adding Notes
- Navigate to the “Add Notes” section from the main menu.
- You can capture an image using your device's camera, which will be interpreted by our ML function.
- You will then be redirected to a new page where the interpreted note title and body will be shown.
- Click add note if they're satisfactory. If successful, a success message will show.
- The extracted notes will be stored and can be accessed in all notes, search note.

### All Notes
- Access all your saved notes through the “View Notes” section.
- Each note can be edited or deleted.

### Search Notes (case sensitive)
- Use the search functionality to quickly find specific notes.
- Enter part of the note's title or the full title in the search bar to filter out notes.
- Case sensitive

## Digital Ocean
You can access our app through: http://159.203.121.138:5000/
```
http://159.203.121.138:5000/
```

To enable cameras on chrome go to
```
chrome://flags/#unsafely-treat-insecure-origin-as-secure
```
Find "Insecure origins treated as secure", enable it and add our address to the list

## Team Members

Nicolas Izurieta: https://github.com/ni2050

Patrick Zhao: https://github.com/PatrickZhao0

Brad Yin: https://github.com/BREADLuVER

Yucheng Xu: https://github.com/Yucheng-XPH
