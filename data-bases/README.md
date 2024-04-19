To create a new database and grant a user the necessary permissions in a database management system (DBMS), follow the steps appropriate to the DBMS you are using. Here are examples using MySQL/MariaDB and PostgreSQL:

## MySQL/MariaDB

1. **Connect to the database server**:
   - If you're connecting via the command line, use the following command:
     ```shell
     mysql -u root -p
     ```
   - Provide the root user's password when prompted.

2. **Create a new database**:
   - Execute the following SQL command to create a new database (replace `database_name` with your desired database name):
     ```sql
     CREATE DATABASE database_name;
     ```

3. **Create a new user**:
   - Execute the following SQL command to create a new user (replace `username` and `password` with your desired username and password):
     ```sql
     CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
     ```

4. **Grant privileges to the user**:
   - Execute the following SQL command to grant privileges to the user over the database:
     ```sql
     GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
     ```

5. **Flush privileges**:
   - Execute the following command to reload the grant tables and apply your changes:
     ```sql
     FLUSH PRIVILEGES;
     ```

6. **Exit**:
   - Type `exit` to leave the MySQL/MariaDB command line interface.

## PostgreSQL

1. **Connect to the database server**:
   - If you're connecting via the command line, use the following command:
     ```shell
     psql -U postgres
     ```
   - Provide the postgres user's password when prompted.

2. **Create a new database**:
   - Execute the following SQL command to create a new database (replace `database_name` with your desired database name):
     ```sql
     CREATE DATABASE database_name;
     ```

3. **Create a new user**:
   - Execute the following SQL command to create a new user (replace `username` and `password` with your desired username and password):
     ```sql
     CREATE USER username WITH PASSWORD 'password';
     ```

4. **Grant privileges to the user**:
   - Execute the following SQL command to grant privileges to the user over the database:
     ```sql
     GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
     GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO username; --after use database_name if have problems to create tables
     ```

5. **Exit**:
   - Type `\q` to leave the PostgreSQL command line interface.

These steps are common for creating a database and granting privileges to a user in MySQL/MariaDB and PostgreSQL. The commands may vary slightly in other database management systems such as SQL Server or Oracle. Always refer to the documentation specific to your DBMS for precise instructions.