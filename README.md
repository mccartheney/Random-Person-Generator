# Random-Person-Generator
Instantly create unique characters with our Random Person Generator Api. Perfect for writers, game designers, or anyone seeking a touch of randomness. Try it now!

## Table of Contents

- [Installation](#installation)
- [Docker Compose Setup](#docker-compose-setup)
- [Endpoints](#endpoints)
  - [Retrieve All Persons](#retrieve-all-persons)
  - [Create Persons](#create-persons)
- [Contributing](#contributing)
- [Developer Credits](#developer-credits)
- [License](#license)

## Installation

1. Clone the repository:

```bash
https://github.com/mccartheney/Random-Person-Generator
```

2. Navigate to the project directory:
```bash
cd your_repository
```

## Docker Compose Setup

1. Build the Docker image and start the containers:
```bash
docker-compose up --build
```

This command will build the Docker image if it doesn't exist and start the containers defined in the docker-compose.yml file.

## Endpoints

### Retrieve All Persons

- Method: GET
- URL: /persons
- Description: Retrieves a list of all persons.
- Response: Returns a JSON array containing all person objects.

Example :

```bash
GET /persons
```

### Create Persons
- Method: GET
- URL: /persons/create
- Description: Creates 100 persons and returns them.
- Response: Returns a JSON array containing the created person objects.

Example :

```bash
GET /persons/create
```

## Contributing

Contributions are welcome. If you have suggestions or find any issues, please create an issue or submit a pull request.

## Developer Credits

This API is developed by [Mccartheney Mendes](https://github.com/mccartheney).


## license

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
