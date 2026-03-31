# Car Listing System

A web-based application for managing and browsing car listings, built with Flask and SQLite.

## Features

- **Browse Cars**: View paginated list of available cars with search and filter options.
- **Admin Panel**: Secure admin interface for managing car listings.
- **Image Support**: Upload images or provide URLs for car photos (images are optional).
- **Search & Filter**: Search by name, fuel type, car type, and number of seats.
- **Export Data**: Export car listings to Excel format with optional logo.
- **Responsive Design**: Clean, user-friendly interface.

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, Jinja2 templates
- **Other**: OpenPyXL for Excel export, Werkzeug for file handling

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/carlistingsystem.git
   cd carlistingsystem
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - The app will automatically create the SQLite database (`cars.db`) on first run.
   - Optionally, run the seed script to populate with sample data:
     ```bash
     python seed.py
     ```

4. **Configure environment** (optional):
   - Set `SECRET_KEY` environment variable for production security.
   - Default admin credentials: username `admin`, password `password123`.

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```
   The app will start on `http://localhost:10000` (or the port set in `PORT` env var).

2. **Access the app**:
   - **Public view**: Browse cars at the home page.
   - **Admin login**: Go to `/login` to access the admin panel.
   - **Admin features**: Add, edit, or delete cars; manage images.

3. **API Endpoint**:
   - `GET /api/car/<car_id>`: Get car details in JSON format.

## Project Structure

```
carlistingsystem/
├── app.py                 # Main Flask application
├── models.py              # Database models (Car, CarImage)
├── seed.py                # Script to populate sample data
├── requirements.txt       # Python dependencies
├── schema.sql             # Database schema (optional)
├── static/                # Static files (CSS, images)
│   ├── style.css
│   ├── styles.css
│   └── images/
├── templates/             # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   └── admin/
│       ├── add_car.html
│       ├── dashboard.html
│       └── edit_car.html
└── README.md              # This file
```

## Development Notes

- **Database**: Uses SQLite for simplicity. Switch to PostgreSQL/MySQL in production by updating `SQLALCHEMY_DATABASE_URI`.
- **Security**: Admin credentials are hardcoded for demo. Use a proper user system in production.
- **Images**: Stored in `static/images/`. Supports both local uploads and external URLs.
- **Export**: Generates Excel files with car data. Logo is optional and sourced from `static/images/src/logo.png`.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test thoroughly.
4. Submit a pull request.

## License

This project is open-source. Feel free to use and modify as needed.