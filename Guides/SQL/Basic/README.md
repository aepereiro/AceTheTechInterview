# Basic SQL Module

Welcome to the Basic SQL module! This section is specifically designed for beginners to introduce them to the fundamentals of SQL. Here, you will learn how to create and manage databases, execute queries, and manipulate data using SQL.

## Overview

SQL, or Structured Query Language, is the cornerstone of all relational database operations. This module covers the core concepts of SQL, including creating tables, performing basic queries, and understanding key operations such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

## Getting Started with Docker and phpMyAdmin

To provide a consistent and easy-to-setup environment, we utilize Docker to run a MariaDB database server along with phpMyAdmin for database management through a web interface.

### Steps to Set Up Your Environment

1. **Install Docker**:
   - If you don't already have Docker installed, download and install Docker Desktop from [Docker's official site](https://www.docker.com/products/docker-desktop).

2. **Clone the Repository**:
   - Clone this repository and navigate to the `/Guides/SQL/Basic/` directory where the `docker-compose.yml` file is located.

3. **Start Docker Containers**:
   - Open a terminal in the `/Guides/SQL/Basic/` directory.
   - Run the command `docker-compose up -d` to start your MariaDB and phpMyAdmin services.

4. **Access phpMyAdmin**:
   - Open a web browser and go to `http://localhost:8080`.
   - Log in using the username `root` and the password `notSecureChangeMe`.

### How to Use phpMyAdmin

- **Creating Databases and Tables**: Learn how to create your first database and tables within phpMyAdmin.
- **Running SQL Queries**: Use phpMyAdmin’s built-in SQL editor to run queries and see the results.
- **Importing and Exporting Data**: Explore how to import data from SQL files and export your database for backups or transfer.

## Lessons

Each lesson in this module is structured to build on the previous one, gradually introducing more complex SQL concepts and operations:

1. [**Lesson 1: Introduction to Databases and SQL**](1/README.md)
   - Understand what a database is and the basics of SQL commands.

2. [**Lesson 2: Creating and Managing Tables**](2/README.md)
   - Learn about different data types and table management in SQL.

3. [**Lesson 3: Basic Data Manipulation**](3/README.md)
   - Insert, update, and delete records within your tables.

4. [**Lesson 4: Basic Queries**](4/README.md)
   - Practice writing and optimizing select queries to retrieve data effectively.

Additional lessons will be developed and added to cover more topics and provide a comprehensive learning experience.

## Feedback and Contributions

We encourage feedback and contributions to these guides. If you have suggestions for improvement or additional topics, please feel free to contribute by submitting an issue or pull request to this repository.

Thank you for joining us in this learning journey into the world of SQL. Happy learning!
