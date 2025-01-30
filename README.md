# Flask API App

## Setup Instructions

### Step 1: Create and Activate Virtual Environment

1. **Create a virtual environment**:

   ```
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

### Step 2: Install Dependencies

1. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

### Step 3: Configure the Database

1. **Update the database configuration**:
   - Open the config.py file.
   - Update the SQLALCHEMY_DATABASE_URI with your database information in the appropriate configuration class:
     ```
     class ProductionConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://<DB_USER>:<DB_PASSWORD>@<DB_HOST>/<DB_NAME>'
     ```

### Step 4: Set the Configuration in run.py

1. Set the configuration:
   - Open the run.py file.
   - Ensure the create_app function is called with the correct configuration name:

```
app = create_app('ProductionConfig')
```

### Step 5: Run the Server

1. **Run the server**:

   ```
   python run.py
   ```

2. **Access the API**:
   - The server will be running at `http://localhost:5000`.
   - Use tools like Postman to test the API endpoints.

### Step 6: Import Postman Collection

1. **Import the provided Postman collection**:
   - A JSON file is provided in the root directory which is the export for the collection.
   - Open Postman.
   - Click on the **Import** button.
   - Select the provided JSON file to import the collection.

## API Endpoints

### Mechanic Endpoints

- **POST `/mechanics/`**: Create a new mechanic.
- **GET `/mechanics/`**: Retrieve all mechanics.
- **PUT `/mechanics/<int:id>`**: Update a specific mechanic.
- **DELETE `/mechanics/<int:id>`**: Delete a specific mechanic.

### Service Ticket Endpoints

- **POST `/service-tickets/`**: Create a new service ticket.
- **GET `/service-tickets/`**: Retrieve all service tickets.
