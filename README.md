# ADSD: Simulation Project

This repository will be used for storing a project that simulates the interaction between a robot and a server implemented in Python. ADSD is a course of the Computer Science major of the Federal University of Campina Grande in Brazil.

## Installing dependencies:

To install project's dependencies, run the following command:

```
pip install -r requirements.txt
```

It is recommended to run the command within a virtual environment.

## Creating the database:
To create the database, run the following commands:

```
sqlite3 tasks.db
sqlite3> .mode csv tasks
sqlite3> .import tasks.csv tasks
```

Before running the commands, make sure SQLite is installed.

## To run the application, run the following commands:

```
python server.py
```

Then, go to http://localhost:5000/tasks.
