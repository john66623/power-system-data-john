# Power System Data

Datasets used in the course *Dynamiske Kraftnett*.

## Repository structure

- `load/` : electricity demand data
- `prices/` : electricity prices
- `production/` : generation data
- `src/` : scripts used to generate the datasets
- `docs/` : documentation and source descriptions

## Data sources

- ENTSO-E
- Statnett
- NVE
- SSB
- Elhub

## Updating datasets

Scripts used to generate datasets are located in `src/`.

## Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then edit `.env` and insert your ENTSO-E API key:

```text
ENTSOE_API_KEY=your_api_key_here
```

## Additional

This repo is a clone used for mandatory and experimental uploads through Git. Additional folders have been made for each new mandatory assignment through the course ELK330 at University of Stavanger. 
