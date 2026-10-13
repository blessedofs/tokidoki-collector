# Big Hit Society Tokidoki Collector Library

Upload `index.html`, `cards.json`, and the `assets` folder to the ROOT of your existing `blessedofs/tokidoki-collector` repository. Keep the folder structure intact.

## What is included
- 157 Series 1 and 161 Series 2 checklist POSITIONS based on official KAYOU tier counts (318 positions). These are NOT 318 fully identified cards.
- 32 Series 1 R-tier names transcribed from TCDB, with printed numbering pending independent confirmation against card faces.
- Original Adieu artwork in a separate unconfirmed-series entry.
- All other names, printed card numbers, and images deliberately left unverified. Placeholders are clearly labeled.
- No unauthorized bulk copying of third-party images. Add images only when you have permission to use them.

## Adding a verified card
Find the matching entry in cards.json by series, rarity, and slot number. Set `name`, `printedNumber`, `image` (e.g. `assets/series1-r-001.webp`), `verified`: true, and update `status`. Upload the image to the assets folder. The internal `id` is a unique web key, not necessarily the printed card number.

## Sources
Official Series 1 tier counts: https://www.kayouofficial.com/en-UK/series/series-x0wyu07i
Official Series 2 product: https://www.tokidoki.it/collections/shop-all/products/tokidoki-x-kayou-wonder-voyage-collectible-cards-roaming-edition-series-2
Series 1 R-tier checklist: https://www.tcdb.com/Checklist.cfm/sid/615895/2025-Kayou-Tokidoki-Wonder-Voyage-Roaming-Edition-Series-1

Collector certificate is a personalized keepsake, not proof of card authenticity or ownership.
