# Ammi TV Explorer

## Source
- Original: https://tvexplorer.live/
- Country filter: India (IN) only — 746 channels
- Channel data: https://tvexplorer.live/project/data/channels.json (filtered to IN)
- Enriched with categories from https://iptv-org.github.io/api/channels.json

## Tech
- Single-file HTML app (index.html) + assets/data/india-channels.json + assets/lib/hls.min.js
- HLS playback via hls.js (with native Safari fallback)
- Full-screen video player with custom controls
- Search, category filter chips, favorites (localStorage), multi-stream fallback

## Run locally
python -m http.server 8123   (or any static server)
then open http://127.0.0.1:8123/

## Deploy (GitHub Pages)
Push the whole folder; index.html is the entry point. All asset paths are relative.

## Notes
- Streams are third-party (iptv-org). Some may be geo-blocked or offline; the player falls back to the next available stream automatically.
- No tracking scripts. No analytics.
