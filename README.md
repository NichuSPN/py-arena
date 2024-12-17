# Arena

**Arena** is an API and Relational Engine for Network Applications. This package serves as a data and API access layer, providing a unified interface for interacting with various database systems and APIs.

## Table of Contents

- [Arena](#arena)
  - [Table of Contents](#table-of-contents)
  - [Examples for Reference](#examples-for-reference)
  - [Features](#features)
  - [Usage](#usage)
    - [Using pip to install from Github](#using-pip-to-install-from-github)
    - [Downloading from GitHub](#downloading-from-github)
    - [Initializing API Handlers](#initializing-api-handlers)
  - [API Reference](#api-reference)
    - [APIHandler](#apihandler)
    - [SQLDB (Base Class for Databases)](#sqldb-base-class-for-databases)
    - [Database Classes](#database-classes)
  - [Database Support](#database-support)
  - [Contributing](#contributing)
 
## Examples for Reference
- [Basic Example](https://github.com/NichuSPN/py-arena-example)
- [With StreamLit](https://github.com/NichuSPN/py-arena-streamlit-example)

## Features

- Unified API for interacting with multiple database systems (PostgreSQL, MySQL, SQLite).
- Easy-to-use API handler for making HTTP requests.
- Template-based SQL query resolution.
- Support for callback functions on API requests.

## Usage

### Using pip to install from Github

To install the latest version directly from GitHub, run:

```bash
pip install git+https://github.com/NichuSPN/py-arena.git
```

### Downloading from GitHub

To use the `arena` package, you can download it directly from GitHub. Follow these steps:

1. **Clone the Repository**: Use `git` to clone the repository to your local machine.

   ```bash
   git clone https://github.com/NichuSPN/arena.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd arena
   ```

3. **Install the Package**: Install the package using `pip`. This will install the package along with its dependencies.

   ```bash
   pip install .
   ```

## API Reference

### APIHandler

- **`__init__(baseUrl, headers=None)`**: Initializes the APIHandler with a base URL and optional headers.
- **`runAPI(apiConfig)`**: Executes an API request based on the provided configuration.
- **`runAPIWithCallbacks(apiConfig, onSuccess=None, onError=None)`**: Executes an API request and handles success and error callbacks.

### SQLDB (Base Class for Databases)

- **`create_connection()`**: Creates a connection to the database. Implementation needed in subclasses.
- **`run_sql(query, isUpdate=False)`**: Executes a SQL command on the database. Implementation needed in subclasses.
- **`close_connection()`**: Closes the database connection. Implementation needed in subclasses.
- **`resolve_template(query, params)`**: Resolves a SQL query template with parameters.

### Database Classes

- **Postgres**: Interacts with PostgreSQL databases.
- **MySQL**: Interacts with MySQL databases.
- **SQLite**: Interacts with SQLite databases.

## Database Support

The `arena` package currently supports the following databases:

- PostgreSQL
- MySQL
- SQLite

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.
