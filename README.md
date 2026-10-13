# Big Hit Society Collector Certificate Library

GitHub Pages-ready static website with searchable Series 1 / Series 2 gallery, card-specific NFC links, editable locally stored collector names, and downloadable PNG certificates.

## Important catalog status
The software supports **both** series, but the complete official card checklist and image rights were not supplied. Only the previously provided Adieu card is seeded, and its Series 2 assignment is **provisional**. Do not advertise the gallery as a complete or verified checklist until you have added and verified the cards.

## Add all cards
Edit `cards.json` to add objects with `id`, `series` (`Series 1` or `Series 2`), `name`, `collection`, `rarity`, `image` (local relative path), and `verified`. Put images under `assets/`. The CSV is an editing template, not automatically loaded. Every ID must be unique. Use actual printed IDs, not invented sequential numbers. Update the provisional Series 2 designation for Adieu after verifying.

Example card-specific NFC link: `https://YOUR-USERNAME.github.io/YOUR-REPO/?card=TD-SSR-035`.

## Publish
Upload the contents of this directory to a GitHub repo; enable Pages from main/root. All image files and cards.json must be uploaded. The site must be served via HTTP(S) for `fetch` to load cards.json.

Names are stored only in each device's browser, keyed per card design. They are editable, not verified owner records. Certificates are collectible keepsakes, not grading/authentication or ownership verification.
