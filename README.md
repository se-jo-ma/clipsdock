# clipsdock
Make sure to pip install docker and to have Docker running.
In order to run this project simply run main.py.
This will spin up a Docker container that has clipspy and CLIPS installed on it. In order to run clips navigate to the terminal and run
'''
clips
'''
This will launch CLIPS interactive CLI.
If you prefer to interact with CLIPS using python there is a very minimal and quick "engine" that can be accessed by navigating to /orq/orqengine.py. 
This is just a hollowed out class that spins up a CLIPS environment. You can find a link to clipspy documentation in /orq/orqengine.py to learn about the bindings available.
You can make changes to it or create a new python file. Just make sure to run the file from the command line.
