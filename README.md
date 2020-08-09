# Flask-Restful-Authentication

Flask-Restful-Authentication is a Flask-based RESTful API that provides user registration, login, refresh token, and logout functionality. It allows users to perform various operations related to user management through the API endpoints.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/username/Flask-Restful-Authentication.git
   ```

2. Install the required dependencies. It is recommended to use a virtual environment:

   ```
   cd Flask-Restful-Authentication
   python -m venv venv
   source venv/bin/activate (for Linux/Mac)
   venv\Scripts\activate (for Windows)
   pip install -r requirements.txt
   ```

3. Configure the application settings in the `config.py` file. Modify the database settings and other configurations as needed.

4. Run the application:

   ```
   flask run
   ```

   The API will be accessible at `http://127.0.0.1:5000/api/v1/user/operation`.

## Endpoints

The following endpoints are available for user operations:

- `POST /api/v1/user/register`: Register a new user with the provided credentials. Required fields: `username` and `password`.

- `POST /api/v1/user/login`: Authenticate a user and obtain an access token and refresh token. Required fields: `username` and `password`.

- `POST /api/v1/user/refresh`: Refresh an expired access token using a valid refresh token. Required field: `refresh_token`.

- `POST /api/v1/user/logout`: Logout a user and revoke the refresh token. Required field: `refresh_token`.

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. When a user logs in, an access token and refresh token are generated. The access token should be included in the `Authorization` header of subsequent requests with the format: `Bearer <access_token>`. The access token has a limited lifespan and can be refreshed using the refresh token.

## Error Handling

The API provides appropriate error responses for various scenarios, including invalid requests, authentication failures, and server errors. The error responses adhere to RESTful principles and include informative error messages.

## Contributing

Contributions to Flask-Restful-Authentication are welcome! If you would like to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the [GNU License](LICENSE).

---

Feel free to modify and customize this README file based on your project's specific details and requirements.