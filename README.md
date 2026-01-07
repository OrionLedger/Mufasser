# Mufasser

Mufasser is an Enterprise Assistant workflow where it supports orchastration processes and automating it easily using AI supported workflows, 

---

## Architecture Overview

The system is composed of five explicit agents orchestrated using LangGraph:
1. Input Classifier
   Tag the input type so it's purpose and route could be detected

2. Query Analyzer  
   Interprets the user question and prepares a retrieval query.

3. Routing
   custom cases decision routing is used to gurantee consistency and stability

2. Actuation  
   Each route is responsible for a process, each process has seperated sequential actions to be performed, some using AI if needed.

3. Answer Generator  
   Produces an answer strictly using actuation state and prompt template.

---

## Project Structure
Folders Structure:

~~~
Root
 ├───infrastructure
 ├───logs
 ├───models
 ├───monitoring
 ├───repo
 ├───src
 │   ├───actuation
 │   ├───perception
 │   ├───preprocessing
 │   ├───reasoning
 │   ├───state_representation
~~~

 1. **src** <br>
which contais execution pipelines

 2. **models** <br>
contains used models inference files

 3. **monitoring**<br>
  contains the repo(s) that manages the monitoring of pipelines perforemence and efficiency

 4. **logs**<br>
contains log records 

 5. **Repo**<br>
 Database repo(s) which will support retrieving and authorized writing, updating, or deleting

 6. **infrastructure** <br>
 contains configuration for all external dependencies, packages, workflows, and technologies which will be used by other repos or modules of the system
