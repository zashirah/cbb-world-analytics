# cbb-world-analytics

CBB World Analytics is a data project using DuckDB and Motherduck for storage, dbt for transformations, and evidence.dev for the BI layer, along with custom python scripts to scrape data from https://comedybangbang.fandom.com/wiki/Main_Page. 

Currently, the compute is all local to my machine. I will automate at some point. 

## Ingest

There are python scripts to make the following calls:
* get_character
* get_characters
* get_episode
* get_episodes (currently called backfill_all_episodes. needs to be refactored)
* get_guest
* get_guests

## Transformation

Used dbt to create a star schema with a episodes fact table, characters/guests/hosts dimension tables, and cross reference tables to map between the fact and dim tables.

## BI

Using evidence.dev to do some basic analysis. Will include more.

