
# Reddit Project (Simple)

Two folders: **scripts/** and **data/** (with raw/ processed/ reports/).
One command appends everything into a single flat file with posts + comments.

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env  # add your keys
python scripts/scrape_and_append.py --subs chile RepublicadeChile --limit 100
```

Outputs:
- `data/raw/snapshot_YYYYMMDD-HHMMSS.csv`  (raw posts-only snapshot)
- `data/processed/master_reddit.csv`        (flat master, post+comment)
- `data/processed/master_reddit.xlsx`       (same, one sheet)
- `data/reports/daily_posts.png`            (quick trend)
