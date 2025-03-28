# How to

1. Generate Table
```bash

uv run generate_table.py

```
2. Fill the table

```bash
uv run fill_tabe.py

```

2. 

import subprocess

# Define the SQLite command and the SQL file
command = "sqlite3 your_database.db < inserts.sql"

# Run the command
subprocess.run(command, shell=True, check=True)