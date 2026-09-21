# GameVault

GameVault is a polished personal gaming tracker and interactive collection showcase built with HTML, CSS, JavaScript, Local Storage, and Three.js.

## Finished feature set

- Add, edit, remove, search, filter, and sort games
- Track Playing, Completed, Backlog, and Dropped games
- Record platform, genre, hours, rating, achievements, dates, notes, and favorites
- Use a cover image URL or upload a cover directly from your computer
- Quick-log +1 or +5 hours from a game's detail view
- Dashboard for total playtime, completion rate, ratings, achievements, current games, and recent activity
- Analytics for playtime, genres, platforms, and status distribution
- Interactive 3D showcase generated from the same tracked library
- Export the full library to a JSON backup and restore it later
- Persistent Local Storage and responsive desktop/mobile design
- No Node.js, database, account, or build process required

## Run

Download the repository and open `index.html` in a modern browser.

The tracker itself runs locally. Google Fonts and the optional 3D Showcase use internet-hosted resources. If your browser restricts CDN scripts from local files, run this from the project folder:

```
python -m http.server 8000
```

Then open `localhost:8000`.

## Data

Game data is stored in the browser with Local Storage. Use **BACKUP** in the header to export your collection before clearing browser data or moving computers, then use **RESTORE** to import it.

Uploaded cover images are converted to local data URLs. GameVault limits uploaded covers to 900 KB to keep browser storage manageable.

## Architecture

A single JavaScript game model powers every view. The dashboard, collection, statistics, detail modal, favorites, quick playtime logging, and 3D scene all update from the same persisted data. Three.js maps game records to interactive meshes and raycasting maps 3D clicks back to the corresponding game.

## Tech

HTML • CSS • JavaScript • Three.js/WebGL • Local Storage • FileReader/Blob browser APIs
