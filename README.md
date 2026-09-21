# GameVault — Python Gaming Tracker

GameVault is a personal gaming tracker built primarily in **Python**. Track your library, playtime, completion status, ratings, achievements, favorites, notes, and gaming statistics from a Streamlit dashboard.

## Stack
Python • Streamlit • pandas • JSON persistence

## Features
- Dashboard with total games, playtime, completion count, and average rating
- Currently-playing view
- Search and status filtering
- Add, edit, favorite, and delete games
- Quick playtime logging
- Ratings, achievements, notes, genres, and platforms
- Playtime and platform statistics
- JSON export and restore
- Local persistence in `gamevault_data.json`

## Run on Windows
```
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

GameVault intentionally uses Python as its application language. No Node.js, JavaScript build system, backend server, or database installation is required.
