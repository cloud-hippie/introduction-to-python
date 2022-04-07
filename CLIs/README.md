# CLI - Command Line Interface

The DevOps world revolves around tooling which can be used to automate the process of interacting with services, such as servers, databases, and cloud providers. 

In this section, we will be learning how to create a CLI that can be used to interact with services that we can then deploy as a python module so that we can use it in our projects.

# Real World Scenario

You work as a DevOps engineer for a company that is working to simplify local development. 

You are tasked with creating a CLI that can be used to write configuration files to make it easy for developers to deploy their code to a local development environment. 

The CLI should allow users to create a new configuration file. 

The CLI should populate a value with the following information:

```yml
version: 1.0.0

services: List of the following services
  api: A custom value. No spaces or dashes allowed.
    build: Location of the build
    depends_on:
      - List of services that this service depends on or None
    environment:
      - List of environment variables or None
    networks:
      - List of networks "default" or None
    ports:
      - "List of ports. It comes down as a string. Example: "8080:8080" or None"
    volumes:
      - "List of volumes. It comes down as a string. Example: "./data:/data" or None"
    restart: "always" or "on-failure" or None
```

The CLI should allow the user to add a service to the configuration file.

The CLI should allow the user to get a services atrribute values.


