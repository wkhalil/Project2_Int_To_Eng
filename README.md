# IDS 721 Project 2   Yuwei Zhang, Duke MIDS
### Docker Container Project

#### Background
The goal of this project is to build a docker image of an application that converts integers to correct English words. Then push the docker image to DockerHub and pull it down to run it in the AWS Cloud9 environment.

##### Docker Image
The docker image is built upon "python3.6:slim" and details could be obtained from "./Dockerfile"

##### Pull and Use
First, a Cloud9 environment with Docker installed needs to be created (other servers or personal laptops also work).

Then open the terminal and command lines to run the docker image are listed below.
1. first pull down the docker image from Docker Hub (make sure Docker is installed before that)
    > docker pull yuweiz/int_to_eng:1.2
2. Then run the image in command line interactive mode
    > docker run -it yuweiz/int_to_eng:1.2

If the application starts successfully, you'll see hints "please type an integer:(Ctrl+C to stop) "


#### Application
The application comes from a leetcode problem I'm very interested in and worked on. (https://leetcode.com/problems/integer-to-english-words/)

There are many nested logic and edge cases to convert integers to English correctly. Thus I made it an application to convert the integers (range from 0 to 2^31-1).


#### Potential problems during development
1. docker image name must include the docker user name as the first part, in this case, "yuweiz/"
2. to stop the application, press Ctrl+C
3. remember to terminate the Cloud9 environment and corresponding EC2 instance after use
