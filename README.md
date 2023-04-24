# Jabberwocky

Create and manage containers that contain virtual environments to be used with coursework.

## Features
* Use on-demand virtual development environments custom-tailored to your courses. These virtual environments contain all the necessary custom software you need to develop programs for assignments, as well as to test and debug your software, all wrapped up in a tidy container that you install once.
* Use the pre-made environments created for the Compiler Theory, Programming Languages, and Operating Systems courses.
* Easily emulate foreign guest architectures other than that of your host machine without even having to think about it.
* Run these development environments on all the major platforms: Windows, macOS, and Linux.
* Transfer files between your host’s native filesystem and the container’s virtual filesystem in an intuitive manner.
* Access and interact with the virtual shell of the container just as you would your own.
* Be able to create containers with whatever custom software you need to distribute to your students for a specific course.

## Installation
### Installing Container Manager
Releases for the container manager can be found [here](https://github.com/Kippiii/jabberwocky-container-manager/releases).
If this does not work, the user can install the tool from source. To start building, first ensure that you have Python 3.12 installed. Then,
you will want to install poetry through pip. Next, use the following commands to build from source:
```bash
git clone https://github.com/Kippiii/jabberwocky-container-manager
cd jabberwocky-container-manager
poetry install
poetry shell
python build.py
./build/dist/installer-[platform]-[architecture]
```
Where `platform` and `architecture` correspond to that of your system.

## Resources
* [User Manual](https://kippiii.github.io/jaberwockey-class-site/docs/Sem2/Milestone6/Jabberwocky_User_Manual.pdf)
* [Demo Video](https://www.youtube.com/watch?v=IETEWHmQChI&feature=youtu.be)
* [Future Ideas](./future.md)
* [Container Manager](https://github.com/Kippiii/jabberwocky-container-manager/tree/main)
* [Repo Server](https://github.com/Kippiii/jabberwocky-repo/tree/main)
* [Class Site](https://github.com/Kippiii/jaberwockey-class-site/tree/main)
