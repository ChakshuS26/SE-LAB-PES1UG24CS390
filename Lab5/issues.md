
# Lab 5 – Static Code Analysis
## Dairy Milk Collection Ledger

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL Injection (B608) | Security - Medium | 11 | SQL query used string formatting to insert farmer input directly into the query. | Replaced string formatting with parameterized SQL queries using placeholders. |
| Weak MD5 Hash (B324) | Security - High | 16 | MD5 is a weak hashing algorithm and is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Shell Command Injection (B605) | Security - High | 31 | os.system() executed a shell command using concatenated input. | Removed os.system() and used Python print() instead. |
| Unused Import (F401) | Code Quality | 2 | The json module was imported but never used. | Removed the unused import. |
| Ambiguous Variable (E741) | Code Quality | 26 | Variable name 'l' was difficult to understand. | Renamed it to 'top_supplier'. |
| Incorrect None Comparison (E711) | Bug | 36 | Used == None instead of Python's recommended None identity comparison. | Changed the condition to fat is None. |
| Missing Docstrings (C0114, C0116) | Code Quality | Multiple | Module and functions did not have documentation strings. | Added module and function docstrings. |
| Invalid Function Naming (C0103) | Code Quality | Multiple | Function names used camelCase instead of snake_case. | Renamed functions using snake_case. |
| Long Lines (E501, C0301) | Style | Multiple | Several lines exceeded the recommended line length. | Split long statements across multiple lines. |
| Global Variable Shadowing (W0621) | Code Quality | Multiple | Function parameters reused the name of a global database connection. | Created a database initialization function and passed the connection explicitly. |
| Empty Database Result | Bug | 26 | max() could fail when no farmer records existed. | Added an empty-result check before finding the top farmer. |

## Summary

- Bandit: 3 security findings resolved.
- Pylint: Improved from 2.00/10 to 10.00/10.
- Flake8: All 7 original violations resolved.

The dairy collection program retains its main functionality after the fixes.
