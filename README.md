# README
@author Justin Noddell

## Overview
- [What is the Tasty, Tasty Recipe Generator Program?](#what-is-the-tasty-tasty-recipe-generator-program)
- [**Installing and Running the Tasty, Tasty Recipe Generator Program**](#installing--running-the-tasty-tasty-generator-program)
    - [Pre-Reqs](#pre-reqs)
    - [Clone the repository](#clone-repository)
    - [Set a (Temporary) Environment Variable](#set-a-temporary-environment-variable)
    - [[Optional] [Recommended] Create and Activate a Virtual Environment](#optional-recommended-create-and-activate-a-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [[Optional] Run tests](#optional-run-tests)
    - [Run Program](#run-program)
    - [Cleanup](#cleanup)
- [Design Approach](#design-approach)
    - [Maintainability](#maintainability)
        - [Code Organization](#code-organization)
        - [Project Structure](#project-structure)
    - [Error Handling](#error-handling)
    - [Testability](#testability)
    - [Usability](#usability)
    - [Security](#security)
        - [API Key Management](#api-key-management)
        - [Other Security](#other-security)
    - [Documentation](#documentation)
        - [User Documentation](#user-documentation)
        - [Technical Documentation](#technical-documentation)
        - [Code Comments](#code-comments)

### What is the Tasty, Tasty Recipe Generator Program?

This program takes user inputted ingredients (such as ones that you might find in your kitchen), and quickly generates a near-endless supply of recipes to show to you. Users can "like" recipes, and the appropriate ingredients will be added to your shopping list. When you are satisfied with your shopping list, you will receive a detailed breakdown of ingredients, sorted by aisle, and with estimated pricing.

### Installing & Running the Tasty, Tasty Generator Program

#### Pre-Reqs:
Confirm the following conditions are met before proceeding:
- your system is running Mac OS
- your system has Python 3.8 or later installed
- your system has git installed

#### Clone Repository
1. Start a terminal session
2. Navigate to the directory where you'd like to clone the project to
3. Clone the repository using the command ```git clone https://github.com/jnoddell/Tasty-Tasty-Recipe-Generator.git```

#### Set a Temporary Environment Variable
1. Navigate to the root directory of the project
2. Create a temporary, virtual environment variable called ```API_KEY``` using the command ```export API_KEY=db11657e774b4e318ab0c9c58c93aa24```
    - **This key has been made inactive**
    - [Recommended] Get an API Key for free by creating a [Spoonacular Account](https://spoonacular.com/food-api)
3. confirm the variable is set by running ```echo $API_KEY```

#### [Optional] [Recommended] Create and Activate a Virtual Environment
1. Now we can create the virtual environment via the command ```python3 -m venv .venv```
2. Next we will activate it: ```source .venv/bin/activate```

#### Install Dependencies
1. Install dependencies using the command ```python3 -m pip install -r requirements.txt```

#### [Optional] Run Tests
1. To run the test suite, use the command ```pytest tests```

#### Run Program
1. To execute the program, type the command ```python3 start.py```

#### Cleanup
1. You can deactivate the virtual environment by entering ```deactivate```
2. exit the terminal, and the API Key will be removed
3. The cloned repository can now be moved to the trash

### Design Approach

#### Maintainability

##### Code Organization:
The code is separated into three main files: ```start.py```, ```lists.py```, and ```command_line_functions.py```. Each file serves a unique but undoubtedly important role in this project.

**```start.py```**
The sole function of this file is to execute what is the Tasty, Tasty Recipe Generator program. In other words, it creates the data structures and calls the functions necessary to move the program along, though there is little detail or actual computation done inline anywhere in this file.

**```lists.py```**
This file is at the core of the project. Two classes reside here: ```IngredientList``` and ```ShoppingList```. ```IngredientList``` is a class that collects and processes all the data that the user inputs as a part of the ingredient list. Furthermore, this class generates recipes to display to the user. ```ShoppingList``` is similar to ```IngredientList``` in that it tracks a list of ingredients, but it stores different data (e.g. alias names, aisles, prices, etc.) Originally, the intention was for ```ShoppingList``` to inherit from ```IngredientList``` but upon further inspection, these two classes do not share as much in common as it may seem on the surface. The ```IngredientList``` class tracks ingredients to use, which ingredients are valid, recipes to make from certain ingredients, and which recipes have been displayed, whereas ```ShoppingList``` simply tracks which ingredients are apart of its list, and pertinent details about said items. Nonetheless, both classes contribute significantly to the operations of this program.

**```command_line_functions.py```**
This file simply provides universally used command line interface (CLI) functions, often times displaying feedback to the user.

##### Project Structure:

```
Tasty, Tasty Recipe Generator/
|-- .gitignore
|-- readme.md
|-- requirements.txt
|-- src/
|   |-- tastypackage/
|       |-- __init__.py
|       |-- command_line_functions.py
|       |-- lists.py
|-- start.py
|-- tests/
    |-- apple_orange_recipes.json
    |-- apple_pork_tenderloin_price_breakdown.json
    |-- roja_sangria_price_breakdown.json
    |-- src/
    |   |-- tastypackage/
    |       |-- __init__.py
    |       |-- command_line_functions.py
    |       |-- lists.py
    |-- test_sample.py
```

The project takes on this particular structure for the following reasons:
1. We can easily add additional packages to ```src/```
2. We can easily add dependencies via ```requirements.txt```

#### Error Handling

Program-Specific Error Cases:

- User attempts view recipes without providing at least one (valid) ingredient:
    - *Solution: The program checks each inputted ingredient against the API such that we know which ingredients are 'valid' and which are not. The program may not advance until at least one valid ingredient has been submitted.*

- User-provided ingredient is unknown and/or it has a typo:
    - *Solution: Request user confirmation of input before adding it to the ingredient list*

- User confirms an unidentifiable ingredient (one not found in any recipes via Spoonacular):
    - *Solution: Allow the user to keep invalid items in their ingredient list, but mark it such that the program does not try and generate recipes with any of them*

- The user provides a faulty API key (does not exist, reached its daily endpoint quota, etc.):
    - *Solution: At instances where this failure may occur, check for a failed response from the API request, and then terminate the program as it requires API access through the end*

- A generated recipe in the queue has already been displayed to the user:
    - *Solution: Track seen recipes IDs in an array, and remove any reoccuring recipes when creating the queue*

- User does not provide valid input into confirmation prompt (y/n):
    - *Solution: Repeat the prompt until a valid input is submitted*

General Error Cases:

- No internet connection prior to starting program:
    - *Solution: At the beginning of the program we send a simple GET request we know will return a certain value, otherwise do not execute the program as the API and/or Internet is not serviceable*

- Loss of internet connection during execution:
    - *Solution: At each API request, check for failed responses and promptly terminate the program if a failure has been detected.*

- User Spamming Inputs:
    - *TBD: Currently there is no measure in place to prevent this action. The program should still complete normally, though the spam will undoubtedly induce lag unto the system.*

#### Testability
There is a test suite found under the ```tests/``` directory, ```test_sample.py``` contains the tests. This test suite can be executed by [installing the program](#installing--running-the-tasty-tasty-generator-program), then navigating to the root of the directory, and typing the command ```pytest tests```.

In terms of testability, the project is certainly testable. That said, it can be time consuming to replicate the many possible user-inputs (edge cases). That is not to say that it cannot be done. Things we would want to test for is basic functionality in functions doing what they are supposed to do as well as private data being confirmed that it is, in fact, private.

The test suite addresses some of these concerns, and does use real data from the API (recipe, pricing data) to help simulate real scenarios, but at this time it does not cover all the cases that it is able to. That said, it is easy to add more testing cases to the file itself as the file can scale as the project does, or different test files could be created for different packages should another one be added.

#### Usability
The goal here is to allow the user to have enough options to navigate the program as necessary while providing useful directions/feedback too. This program provides the basic functions of: adding, removing, and viewing ingredients in the list at any time during the first phase of the program. This also includes providing good feedback to the user as well as information about recipes.

In the second phase of the program, instead of flooding the display with data, the user is prompted to view a basic breakdown of their shopping list which allows them to view the info they may want to see, but without flooding the screen with the same data redundantly between viewing recipes.

There is also some forgiveness in the confirmation prompts (e.g. accepting y or yes as input, confirming ingredient typos, etc.)

#### Security

##### API Key Management
The API Key is sensitive data that we should protect. Hardcoding it would be poor practice as it can easily be compromised by users. Instead, what we implemented here is a temporary environment variable to make this sensitive information private in such a way that we can still run the program, but users cannot exploit this data. The API Key is temporary as the anticipated use case of this program is not for more than even a day, else we could permanently add it or evaluate other options. Moreover, since this key is temporary, it will be forgotten after the terminal session expires.

##### Other Security
Generally, we want to expose as little data to be public as we can. To this end, the classes ```IngredientList``` and ```ShoppingList``` allow us to make all their members private and we do just that, except for when public access is absolutely necessary. There is no need for protected data in this project as the two classes are not inherently related.

#### Documentation

##### User Documentation:
User feedback is as important as user-friendly features themselves: if a user isn't aware of a feature, action, etc., then it might as well not exist. The goal of this program is to provide users a clear response for each action taken, including passive actions (e.g. loss of power), but without overpopulating the screen with text as that may overwhelm the user.

##### Technical Documentation:
See [README](#readme)

##### Code Comments:
There are a fair degree of comments throughout the code. I believe Classes and Functions should provide a clear idea of their purpose to those reading the code. Python is extremely 'readable' but that doesn't mean code comments are unnecessary. Beyond this, I describe local variables and chunks of a function or script where it may be necessary. It's also important to make good use of whitespace.
