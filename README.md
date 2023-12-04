# Containerized App Exercise

## Badges

![Python build & test](https://github.com/software-students-fall2023/4-containerized-app-exercise-cantopop/actions/workflows/containerized-app.yml/badge.svg) 


## Description

When taking notes in class, it can be stressful to try to jot down everything one sees on the slides the professor is presenting. This handy web app allows students to snap a quick picture of a slide that may be too much to write down manually, and the app will automatically convert the text in the image to a text note that can be later referenced. 

## Team Members

Nicolas Izurieta: https://github.com/ni2050

Patrick Zhao: https://github.com/PatrickZhao0

Brad Yin: https://github.com/BREADLuVER

Yucheng Xu: https://github.com/Yucheng-XPH

## Setp-up Instructions

### Step 1, Clone the directory:
```
git clone https://github.com/software-students-fall2023/4-containerized-app-exercise-cantopop.git
```
### Step 2, open Docker desktop and cd into cloned repository:
```
cd "path_to_directory"
```
### Step 3, initialize docker using:
```
Docker stop $(docker ps -a -q)

Docker rm $(docker ps -a -q)

docker rmi ($docker images -a -q)

Docker-compose down

Docker-compose up —build
```
### Step 4, access and webcam:

Now, you can access http://127.0.0.1:5000/, remeber to allow webcam for your web page

## User-guide

