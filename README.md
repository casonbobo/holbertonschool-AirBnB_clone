# AirBnB Clone - Holberton

This repository is the first part of the AirBnB project at Holberton School that will cover fundemental concepts that will help us eventually deploy the server needed for our AirBnB Website(hbnb).

#### Functionalities of this command interpreter:

* Create new objects (ex: a new User or a new Place)
* Retrieve an object from a file, database, etc...
* Do operations on objects (count, compute stats, ect...)
* Update attributes of an object
* Destroy an object

## Installation

* Clone this repository: 'git clone "https://github.com/casonbobo/AirBnB_Clone.git"'
* Access AirBnB directory: 'cd AirBnB_Clone'
* Run hbnb(interactively): './console' and enter'
* Run hbnb(non-interactively): 'echo "<command>" | ./console.py'

## File Description
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console currently supports.

* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - creates a new instance of 'BaseModel', saves it (to JSON file) and print the id
* `destroy` - deletes an instance based on the class name and id (saves to JSON file)
* `show` - prints the string representation of an instance based on the class name and id
* `all` - prints all string representation of all instances based or not on the class name
* `update` - Updates an instance based on the class name and id by adding or updating attribute

## Examples of use
```bash
AirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbhb) create BaseModel
96892712-7e86-4a70-9b48-34b3227bd1
(hbnb) show BaseModel
(hbnb) all BaseModel
{'BaseModel.96892712-7e86-4a70-9b48-34b632272bd1': <models.base_model.BaseModel object at 0x7fc3cbc37190>}
(hbnb) show BaseModel 96892712-7e86-4a70-9b48-34b632272bd1
[BaseModel] (96892712-7e86-4a70-9b48-34b632272bd1) {'id': '96892712-7e86-4a70-9b48-34b632272bd1', 'created_at': datetime.datetime(2023, 6, 14, 7, 30, 28, 205165), 'updated_at': datetime.datetime(2023, 6, 14, 7, 30, 28, 205191)}
(hbnb) destroy BaseModel 96892712-7e86-4a70-9b48-34b632272bd1
(hbnb) show BaseModel 96892712-7e86-4a70-9b48-34b632272bd1
** no instance found **
(hbnb) quit
Goodbye!
```

## Flowchart
![image](https://github.com/casonbobo/holbertonschool-AirBnB_clone/assets/115739693/c06affdc-28b6-48d3-be27-6dfcb5a87507)



## Authors

Cason Bobo - [GitHub](https://github.com/casonbobo)

Caramon Hofstetter - [GitHub](https://github.com/caramonh)
