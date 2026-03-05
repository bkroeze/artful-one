# Filedrop App

Secure file download system with token-based authentication, expiration dates, and usage limits.

## Setup

1. Configure `FILEDROP_BASE_DIR` in settings (defaults to `filedrop_files/` in project root)
2. Run migrations: `uv run manage.py migrate`
3. Create files in the base directory manually

## Usage

### 1. Place File
Put files in the configured `FILEDROP_BASE_DIR` directory.

### 2. Create Drop
In Django Admin:
- Go to File Drop > Drops
- Click "Add Drop"
- Enter shortname (slug) and filename (just the filename, not path)
- Save

### 3. Generate Token
On the Drop change page:
- Click "Generate Token" button
- Set expiration (days) and usage limit
- Save
- Copy the generated token

### 4. Share Download Link
The admin shows the full download URL:
```
/filedrop/<shortname>/?token=<token-value>
```

## Security Features

- Path traversal protection (filename validation)
- Token expiration dates
- Usage limits per token
- Token deactivation
- Download logging (IP, user agent, timestamp)
- One-to-many tokens per drop (different clients get different tokens)

## URL Pattern

```
GET /filedrop/<shortname>/?token=<token>
```

Response codes:
- 200: Success (file download)
- 400: Missing token
- 403: Invalid/expired/exceeded token
- 404: Drop or file not found

## Models

### Drop
- `shortname`: Unique slug identifier
- `filename`: Name of file in base directory
- `created_at`: Timestamp

### Token
- `drop`: Foreign key to Drop
- `token_value`: Unique secure string
- `expiration_date`: When token expires
- `usage_limit`: Maximum downloads allowed
- `usage_count`: Current download count
- `is_active`: Boolean flag

### DownloadLog
- `token`: Foreign key to Token
- `ip_address`: Client IP
- `user_agent`: Client user agent
- `timestamp`: When download occurred
- `success`: Whether download succeeded
- `error_message`: Error details if failed
