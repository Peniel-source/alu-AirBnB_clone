# AirBnB Clone - The Console

## Description

This project is the first step towards building a full web application: the AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Project Overview

The console is a command interpreter to manage objects abstraction between objects and how they are stored. The console will perform the following tasks:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Command Interpreter

### How to start it

To start the console, run the following command:

```bash
./console.py
```

### How to use it

The console works both in interactive and non-interactive mode:

#### Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Available Commands

- **quit** or **EOF**: Exit the program
- **help**: Show available commands or help for a specific command
- **create**: Create a new instance of a class
- **show**: Show string representation of an instance
- **destroy**: Delete an instance
- **all**: Show all instances or all instances of a class
- **update**: Update an instance by adding or updating attributes

### Examples

```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

## Classes

The following classes are implemented:

- **BaseModel**: The base class for all other classes
- **User**: User class that inherits from BaseModel
- **State**: State class that inherits from BaseModel
- **City**: City class that inherits from BaseModel
- **Amenity**: Amenity class that inherits from BaseModel
- **Place**: Place class that inherits from BaseModel
- **Review**: Review class that inherits from BaseModel

## File Storage

The project uses JSON file storage to persist objects. The FileStorage class handles:

- Serialization of instances to JSON file
- Deserialization of JSON file to instances
- Storage and retrieval of all objects

## Testing

To run all tests:

```bash
python3 -m unittest discover tests
```

To run tests for a specific module:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Project Structure

```
├── console.py          # Command interpreter
├── models/            # Model classes
│   ├── __init__.py
│   ├── base_model.py  # BaseModel class
│   ├── user.py        # User class
│   ├── state.py       # State class
│   ├── city.py        # City class
│   ├── amenity.py     # Amenity class
│   ├── place.py       # Place class
│   ├── review.py      # Review class
│   └── engine/        # Storage engine
│       ├── __init__.py
│       └── file_storage.py  # FileStorage class
├── tests/             # Unit tests
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base_model.py
│       ├── test_user.py
│       └── test_engine/
│           ├── __init__.py
│           └── test_file_storage.py
├── AUTHORS            # Contributors
└── README.md          # This file
```
