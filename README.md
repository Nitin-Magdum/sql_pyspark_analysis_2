## Installation and Setup
To set up the project and run the PySpark application, follow these steps:

1.  **Clone the Repository**
First, clone the repository to your local machine. Open a terminal and run:
```bash
git clone https://github.com/Nitin-Magdum/sql_pyspark_analysis_1.git
```
  

2. **Navigate to the Project Directory**
```bash
cd sql_pyspark_analysis
```
3. **Install Required Dependencies**
This project requires certain Python libraries to run properly. These dependencies are listed in the `requirements.txt` file. You can install them using the following command:
```bash
pip install -r requirements.txt
```
4. **Download PostgreSQL JDBC Driver**
The project also requires the PostgreSQL JDBC Driver to connect to a PostgreSQL database. Follow these steps to download and set it up:

-   Go to the PostgreSQL JDBC Driver download page: [PostgreSQL JDBC Driver](https://jdbc.postgresql.org/download/)
-   Download the appropriate `.jar` file for your environment.
-   Place the downloaded `.jar` file into your project's working folder. This allows PySpark to access the driver.

Alternatively, you can set the path to the `.jar` file as a global variable if you prefer.

5. **Questions and Table Structure**
   The questions related to the dataset can be found in the file named [Questions](Questions.md). Additionally, the structure and names of the relevant 
    tables are defined in the file [Table](Table_Structure.md).
