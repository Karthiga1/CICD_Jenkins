# CICD_Jenkins

## Getting Started
For Development, a Rhel server was spun up, Jenkins and all other requirements installed and integrated with Github. 


## Required Jenkins Plugins

Pipeline: Multibranch
Blue Ocean
Pipeline: GitHub
Python
Pipeline: Stage View
Http Request


## Required Jenkins Configuration
Jenkins with Python3 and pip3 installed. Check if requests is installed.
SMTP port has to be opened for mailing

##To run the Jenkinsfile 
Fork the Github repo,branch main

## Folder Structure

```bash
|- Jenkinsfile # Groovy file
|- Build.json # Json to read stages
|- run.py # Contains REST API call and decides if today is a holiday
|- build.py # Creates zip file and other files
|- quality.py # Copies files according to current stage
```
![alt text](https://github.com/Karthiga1/CICD_Jenkins/blob/main/images/image.JPG?raw=true)

## Build tested with different conditions enabled through checkbox

![alt text](https://github.com/Karthiga1/CICD_Jenkins/blob/main/images/image2.JPG?raw=true)


## Contributing


### Branching Strategy


### Committing

