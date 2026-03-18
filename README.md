# AI-Powered Financial Advisor Dashboard

## Overview
The AI-Powered Financial Advisor Dashboard is a comprehensive web application designed to help individuals manage and track their financial goals, transactions, and personal profiles. This project offers a user-friendly interface for users to interact with their financial data, set and monitor financial goals, and analyze transaction history. The application is particularly beneficial for individuals seeking to gain better insights into their financial habits and make informed decisions to achieve their financial objectives.

The dashboard leverages FastAPI for the backend, providing robust and efficient API endpoints for data retrieval and manipulation. The frontend is built using HTML, CSS, and JavaScript, offering a seamless and interactive user experience. With a focus on simplicity and functionality, this application serves as a personal financial advisor, empowering users to take control of their financial future.

## Features
- **User Profile Management**: Create and update user profiles with personal information including name and email.
- **Financial Goal Setting**: Define financial goals with target amounts, current savings, and deadlines, and track progress over time.
- **Transaction Tracking**: Record and view transaction history categorized by type, amount, and date.
- **Responsive Design**: Enjoy a consistent user experience across devices with a responsive layout.
- **Dynamic Content Loading**: Fetch and display data dynamically from the server, ensuring up-to-date information.
- **Smooth Navigation**: Utilize smooth scrolling and intuitive navigation for an enhanced user experience.
- **Secure Data Handling**: Ensure data integrity and security with SQLite database management.

## Tech Stack
| Component       | Technology  |
|-----------------|-------------|
| Backend         | FastAPI     |
| Frontend        | HTML, CSS, JavaScript |
| Database        | SQLite      |
| Templating      | Jinja2      |
| Web Server      | Uvicorn     |
| CSS Framework   | Bootstrap   |
| JavaScript Library | Font Awesome |

## Architecture
The project architecture is designed to separate concerns between the frontend and backend, ensuring a clean and maintainable codebase.

```
+-----------------+        +------------------+        +-------------------+
|                 |        |                  |        |                   |
|  Frontend       | <----> |  FastAPI         | <----> |  SQLite Database  |
|  (HTML/CSS/JS)  |        |  (Backend)       |        |  (Data Storage)   |
|                 |        |                  |        |                   |
+-----------------+        +------------------+        +-------------------+
```

### Backend
- **FastAPI** serves as the backend framework, handling API requests and responses.
- **SQLite** is used for data storage, managing user profiles, financial goals, and transactions.
- **Jinja2** templates render HTML pages for the frontend.

### Frontend
- **HTML/CSS/JS** provide the structure, styling, and interactivity of the application.
- **Bootstrap** and **Font Awesome** enhance the visual appeal and usability of the interface.

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-financial-advisor-dashboard-auto.git
   cd ai-powered-financial-advisor-dashboard-auto
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit:
   ```
   http://localhost:8000
   ```

## API Endpoints
| Method | Path                      | Description                              |
|--------|---------------------------|------------------------------------------|
| GET    | /api/users/{user_id}      | Retrieve user profile by ID              |
| POST   | /api/goals                | Create a new financial goal              |
| GET    | /api/transactions         | Retrieve all transactions                |
| PUT    | /api/users/{user_id}      | Update user profile by ID                |

## Project Structure
```
.
├── Dockerfile                  # Docker configuration file
├── app.py                      # Main application file with API endpoints
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the application
├── static/
│   ├── css/
│   │   └── style.css           # CSS styles for the application
│   └── js/
│       └── main.js             # JavaScript for interactivity
├── templates/
│   ├── dashboard.html          # Dashboard page template
│   ├── goals.html              # Financial goals page template
│   ├── profile.html            # User profile page template
│   ├── settings.html           # Settings page template
│   └── transactions.html       # Transactions page template
└── financial_advisor.db        # SQLite database file
```

## Screenshots
*Placeholder for application screenshots*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t financial-advisor-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 financial-advisor-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.