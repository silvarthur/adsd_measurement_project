# ADSD: Simulation Project

This repository will be used for storing a project that simulates the interaction between a robot and a server implemented in Python. ADSD is a course of the Computer Science major of the Federal University of Campina Grande in Brazil.

## Creating the database
To create the database, run the following commands:

```
sqlite3 tasks.db
sqlite3> .mode csv tasks
sqlite3> .import tasks.csv tasks
```
