# GameVault

GameVault is a personal gaming tracker that turns a player's game history into a useful dashboard and an optional interactive 3D collection.

## Features

- Add, edit, and remove games
- Track Playing, Completed, Backlog, and Dropped status
- Record platform, genre, playtime, personal rating, achievements, start/completion dates, notes, and a custom accent color
- Dashboard with total playtime, completion rate, average rating, achievements, current games, and recent activity
- Search, filter, and sort the full library
- Analytics for most-played games, favorite genres, platforms, and library status
- Interactive Three.js 3D showcase generated from the user's own tracked collection
- Persistent browser storage with Local Storage
- Responsive desktop/mobile layout
- No Node.js, database, account, or build tools required

## Run

Download the repository and open `index.html` in a modern browser. An internet connection is needed for the optional 3D Showcase because Three.js is loaded from a CDN. All core tracking features work in the browser and game data is stored locally on the device.

If your browser restricts CDN scripts from local files, from the project folder run:

```
python -m http.server 8000
```

Then open `localhost:8000`.

## Architecture

The application uses a single shared JavaScript game model. Dashboard metrics, library cards, analytics, editing, and the 3D collection all render from that same data. Changes are serialized to Local Storage. The 3D view maps each tracked game to a Three.js mesh and uses raycasting to connect clicked 3D objects back to their underlying game record.

## Tech

HTML, CSS, JavaScript, Three.js/WebGL, Local Storage.
