AirBnB Clone Project
Project Description
This project aims to build an AirBnB clone, including a command-line interpreter for managing AirBnB objects. The project involves the creation of various classes (User, State, City, Place, Amenity, Review) that inherit from a base class (BaseModel). Additionally, an abstracted storage engine (File Storage) is implemented to handle serialization and deserialization of instances.

Command Interpreter
The command interpreter provides a shell-like interface for managing objects within the AirBnB project. It allows users to perform actions such as creating new objects, retrieving objects from storage, performing operations on objects, updating attributes, and destroying objects.

How to Start the Command Interpreter
To start the command interpreter, run the following command:

bash
Copy code
$ ./console.py
How to Use the Command Interpreter
Once in interactive mode, the user can use various commands to interact with the objects. The prompt (hbnb) indicates that the interpreter is ready to receive commands.

Documented commands (type help <topic>):

EOF
help
quit
Examples
Interactive Mode
bash
Copy code
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) update User 1234-5678-9012 email "user@example.com"
Non-Interactive Mode
bash
Copy code
$ echo "create User" | ./console.py
$ echo "show User 1234-5678-9012" | ./console.py
$ echo "update User 1234-5678-9012 email 'user@example.com'" | ./console.py
Authors
The following individuals have contributed to the development of this project:

Author 1
Author 2
...
Branches and Pull Requests
We use branches and pull requests on GitHub to organize our work efficiently. Each feature or bug fix is developed on a separate branch before being merged into the main branch. This helps maintain a clean and organized codebase.
