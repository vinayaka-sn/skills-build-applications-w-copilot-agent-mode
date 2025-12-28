# OctoFit Tracker Application

A fitness tracking application built with Django REST Framework and React, featuring superhero users from Marvel and DC teams.

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                          # Python virtual environment
│   ├── octofit_tracker/               # Django project
│   │   ├── models.py                  # Database models
│   │   ├── serializers.py             # REST API serializers
│   │   ├── views.py                   # API views
│   │   ├── urls.py                    # URL routing
│   │   ├── settings.py                # Django settings
│   │   ├── admin.py                   # Admin configuration
│   │   └── management/
│   │       └── commands/
│   │           └── populate_db.py     # Database population script
│   ├── manage.py                      # Django management script
│   └── requirements.txt               # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/                # React components
    │   │   ├── Activities.js
    │   │   ├── Leaderboard.js
    │   │   ├── Teams.js
    │   │   ├── Users.js
    │   │   └── Workouts.js
    │   ├── App.js                     # Main application component
    │   └── App.css                    # Custom styling
    └── package.json                   # Node dependencies
```

## Features

### Backend (Django REST API)
- **User Management**: Track superhero users with profiles and fitness levels
- **Team Management**: Organize users into Marvel and DC teams
- **Activity Logging**: Record workouts including running, walking, cycling, swimming, and strength training
- **Workout Library**: Superhero-themed workout suggestions
- **Leaderboard**: Competitive ranking system based on activity points

### Frontend (React)
- **Responsive Navigation**: Bootstrap-powered navigation menu
- **User Dashboard**: View all superhero users and their profiles
- **Team View**: See team information and members
- **Activity Feed**: Browse all logged activities
- **Workout Browser**: Explore workout suggestions
- **Leaderboard**: Real-time rankings with medals for top performers

## Technology Stack

- **Backend**: Python 3.12, Django 4.1.7, Django REST Framework 3.14.0
- **Frontend**: React 18, Bootstrap 5, React Router
- **Database**: SQLite (development)
- **Styling**: Custom CSS with gradient background, Bootstrap components

## Setup Instructions

### Backend Setup

1. Create and activate virtual environment:
```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3. Run migrations:
```bash
python octofit-tracker/backend/manage.py migrate
```

4. Populate database with test data:
```bash
python octofit-tracker/backend/manage.py populate_db
```

5. Start Django development server:
```bash
python octofit-tracker/backend/manage.py runserver
```

### Frontend Setup

1. Install dependencies:
```bash
cd octofit-tracker/frontend
npm install
```

2. Start React development server:
```bash
npm start
```

## API Endpoints

All endpoints are available at `/api/`:

- `GET /api/users/` - List all user profiles
- `GET /api/teams/` - List all teams
- `GET /api/activities/` - List all activities
- `GET /api/workouts/` - List all workouts
- `GET /api/leaderboard/` - Get current leaderboard rankings

## Test Data

The application comes pre-populated with superhero test data:

### Marvel Team
- Iron Man (Tony Stark)
- Spider-Man (Peter Parker)
- Captain America (Steve Rogers)
- Thor (Thor Odinson)
- Black Widow (Natasha Romanoff)

### DC Team
- Superman (Clark Kent)
- Batman (Bruce Wayne)
- Wonder Woman (Diana Prince)
- Flash (Barry Allen)
- Aquaman (Arthur Curry)

### Statistics
- 10 superhero users
- 2 teams (Marvel & DC)
- 59 logged activities
- 6 workout suggestions
- Dynamic leaderboard rankings

## Codespace Support

The application is configured to work in GitHub Codespaces with automatic port forwarding:
- Backend: Port 8000
- Frontend: Port 3000

## Security Notes

⚠️ **Important**: This application is configured for development only:
- The Django SECRET_KEY is hardcoded (use environment variables in production)
- DEBUG mode is enabled
- CORS allows all origins
- No authentication is required for API access

For production deployment, please review Django security checklist and implement proper security measures.

## License

This project is part of the GitHub Skills "Build Applications with GitHub Copilot Agent Mode" exercise.
