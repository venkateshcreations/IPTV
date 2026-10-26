# Ammi TV Explorer

## Source
- Original site: https://tvexplorer.live/ (India view)
- Live channel source: https://iptv-org.github.io/iptv/countries/in.m3u (CORS-enabled upstream data)
- Fallback streams: https://iptv-org.github.io/api/streams.json
- Bundled snapshot: assets/data/india-channels.json (used only if the live source is unreachable)
- tvexplorer.live/project/data/channels.json is not fetched at runtime — it does not send CORS headers

## Tech
- Single-file HTML app (index.html) + assets/data/india-channels.json + assets/lib/hls.min.js
- Fetches the live India M3U on every load, then adds fallback streams from iptv-org in the background
- HLS playback via hls.js (with native Safari fallback)
- Full-screen video player with custom controls
- Search, category filter chips, favorites (localStorage), multi-stream fallback
- On HTTPS pages, HTTP-only streams are skipped to avoid mixed-content failures

## Run locally
python -m http.server 8123   (or any static server)
then open http://127.0.0.1:8123/

## Deploy (GitHub Pages)
Push the whole folder; index.html is the entry point. All asset paths are relative.

## Notes
- Streams are third-party (iptv-org). Some may still be offline, geo-blocked, or CORS-restricted; the player tries every available stream automatically.
- No tracking scripts. No analytics.
