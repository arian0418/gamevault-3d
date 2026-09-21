# GameVault 3D

An interactive 3D gaming library where users can explore, organize, and showcase a game collection inside a virtual gaming vault.

## Highlights

- Real-time 3D room rendered with Three.js/WebGL
- Cinematic "Enter Vault" landing experience
- Drag-to-orbit camera and scroll-to-zoom navigation
- Clickable 3D game cases with game details
- Playing / Completed / Backlog status tracking
- Searchable and filterable 2D collection view
- Playtime, completion, rating, and per-game analytics
- Persistent status changes using browser Local Storage
- Procedural room geometry, shelves, desk, trophies, lighting, fog, and particles
- Optional generated ambient tone
- Responsive interface

## Tech Stack

- HTML
- CSS
- JavaScript
- Three.js / WebGL
- Browser Local Storage

No framework, Node.js, database, or build tools are required.

## Run

Because the project loads Three.js from a CDN, an internet connection is required.

1. Download the repository.
2. Extract it.
3. Double-click `index.html`.
4. Click **ENTER VAULT**.

If your browser blocks CDN scripts on local files, run a tiny local server from the project folder with:

```
python -m http.server 8000
```

Then visit `localhost:8000`.

## Controls

- **Drag:** orbit the vault
- **Mouse wheel:** zoom
- **Click a game case:** inspect it
- **Vault / Library / Stats:** switch views
- **Change Status:** cycle a selected game through Backlog, Playing, and Completed

## How it works

The room is generated programmatically with Three.js primitives. Each displayed game case is a 3D group linked to a JavaScript game object through an ID. A raycaster detects which 3D object the user clicks and opens the matching game data. The render loop smoothly interpolates room rotation and camera zoom while updating environmental animation.

The library and analytics views use the same game data as the 3D room. Status changes are persisted in Local Storage, so the collection remains updated between browser sessions.

## Project Goal

GameVault 3D explores how a traditional game library can become an interactive spatial interface while demonstrating 3D graphics, event handling, data modeling, state persistence, responsive design, and performance-aware rendering.
