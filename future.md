# Future Ideas

Below is a list of ideas for features that this tool would benefit from having added to it in the future. Each feature includes a brief description about what it would be and how it would be implemented. If any future developer is interested on improving this tool (in another senior project for instance), these would be things to look at:

## TRACKS Login Server
The repository module contains code to host a web server that allows containers to be uploaded and downloaded from the cloud. Currently, only the code is presented, and it is not hosted anywhere. Thus, one could work with IT (or host it themselves) to create a server that could be used by any Florida Tech student. In the implementation of repositories, there is no authentification that is done (it is left blank). During this process, the authentification should be hooked up into TRACKS. This will allow for only professors to be able to upload containers to the server. This can be done by modifying `Auth.py`.

## Container Status
There is currently no way to see what containers are running and what they are doing. Add a new command that prints to the user the status of all containers, including if they are started and information on their currently running processes.

## Container Save States
As a user uses a container, the state of the container changes (for instance, when files are added, the container will forever have those files in the future). If the user accidently messes with their container in a way that they did not intend, there is no way to undo those changes other than reinstalling the container. Thus, each container will now have a number of save states that can be loaded back to. One save state will automatically be added when the container is first installed. The developer should keep in mind that a QEMU hard disk can be large, so they will likely need to be smart to not overwhelm the user's disk space.

## Containers For More Courses
There are always more opportunities to make containers for more courses. Although there is a build wizard available with the tool, professors may still prefer to not configure containers themselves. Classes that maybe could use containers: Computer Networks, Assembly, and all Cyber classes. Maybe courses from other majors could use containers?

## Scriptability
Instructors or students may want to create scripts that use this tool to automatically complete certain tasks. For instance, a professor may want to create a script that automatically grades an assignment that is ran in a container. The only way to do this currently is to use shell scripts that run direct cmd commands to the tool. The goal is to make a Python interface that allows users to have friendly access to all functionality of the tool using calls from a Python library.

## Integrate with cmd2
Currently, the cli could be upgraded to be more user friendly. The `cmd2` python library would allow for this. This could create better help menus and tab-completion.

## Graphical Module
Some courses (mostly those from other majors) may require graphical software to be used from within a container. Currently, users are only able to interact with containers through a shell. Find a way to display programs with graphics that are running in containers to users.