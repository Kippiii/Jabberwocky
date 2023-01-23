# Jaberwocky Guide

## Container Install

At the start of the course, the professor should make available an archived folder, such as `container.tar.gz`. You will use this file to install the container.

To install this container into the system, use the following command:
```shell
jab install [container_path] [container_name]
```
For instance, running `jab install container.tar.gz my_container` creates a container from the `container.tar.gz` archive and calls it `my_container`.

## Using the Container

Before using any container, you have to start the container using:
```shell
jab start [container_name]
```

After starting a container, you can begin to use some of the functions to interact with the container. We will now go through some of the common functions you may want to perform on a container.

If you would like to run a command in the container, you can run the following:
```shell
jab run [container_name] [command]
```

If you would like to transfer a file from your file system into the container's file system, you can run the following:
```shell
jab send-file [container_name] [path_to_source] [path_to_destination]
```

If you would like to pull a file from the container's file system to a file from your file system, you can run the following:
```shell
jab get-file [container_name] [path_to_source] [path_to_destination]
```

If you would like to open the interactive shell of the container, you can run the following:
```shell
jab interact [container_name]
```

Finally, when you are done using the container, we recommend that you stop it to ensure that it exits properly. When you are done using the container, you can run the following command to stop it:
```shell
jab stop [container_name]
```

## Questions

If you run into any issues using this tool or have any questions, these questions can be addressed to either iorzel2019@my.fit.edu or dmcdougall2019@my.it.edu.
