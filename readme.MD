# Function executer

A system in Python that receives a text as an input from file or stdin,
and for each line it execute the function with the given parameters.

## Install dependencies

Clone this repository and run the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` is only for the user `functions.py` file.  
The system works with the native Python libraries.

## Usage

### Script help and usage

```text
❯ python app.py -h
usage: app.py [-h] [INFILE]

A system in Python that receives a text as an input from file or stdin, and for each line it execute the function with the given parameters.

positional arguments:
  INFILE      Optional input file. The text file contains lines in the following format: [function name], [comma separated list of arguments] If not provided, the program will read from stdin. To exit, press Ctrl-C (SIGINT).

options:
  -h, --help  show this help message and exit

Example: python app.py input_file.txt
```

### Execute options

1. Execute from file

    ```bash
    python app.py input_file.txt
    ```

2. Execute with STDIN from PIPE input

    ```bash
    cat input_file.txt | python app.py
    ```

3. Execute with STDIN input

    ```bash
    python app.py
    ```

    Then you can paste any function with arguments in the terminal.

    ```text
    get_pokemon_weight, "Pikachu"
    60
    ```

    To exit, press Ctrl-C (SIGINT).

## Adding more functions

The user can implement more functions by adding them to the `functions.py` file.
The input arguments needs to be only arguments and not a key-value.

### Supported types

* int
* str
* list of strings. If you need a list of integers (or any other types) you can convert them within the custom function.

### Input format

The text file contains lines in the following format:[function name], [comma separated list of arguments].

```text
❯ cat input_file.txt
int_in_range, 3, 6, 5
get_pokemon_name, 68
get_pokemon_weight, "Pikachu"
string_in, "abcde","bdc"
list_of_ints_in_range, [1, 55, 33, 2, -33], -90, 100
```

It's the same from STDIN for each line.

## Todo

* [x] Dynamically load functions from a file.
* [x] Dynamically execute functions.
* [x] Pass arguments to functions.
* [x] Set type of arguments.
* [x] Stream mode.
* [x] Script input parameters as CLI arguments.
* [x] CLI help description.
* [ ] Automatic tests.
* [ ] Create a package.
