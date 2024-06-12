# csv-to-md-table
Convertor from csv file to markdown table format.

# Usage

```python
python convert.py input.csv output.md
```

input.csv
```csv
,A,B
1,1A,1B
2,2A,2B
```

output.md
```md
|  | A | B |
|---|---|---|
| 1 | 1A | 1B |
| 2 | 2A | 2B |
```