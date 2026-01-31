# Announcement Banner Configuration

## Overview
The announcement banner now supports dynamic configuration through the database, eliminating the need to modify code when updating announcements.

## Configuration

The banner configuration is stored in MongoDB in the `banner` collection with the following structure:

```json
{
  "_id": "announcement_banner",
  "enabled": true,
  "message": "📢 Activity registration is open until the end of the month. Don't miss your spot!",
  "end_date": "2026-01-31T23:59:59Z"
}
```

### Fields:
- **enabled** (boolean): Controls whether the banner is displayed
- **message** (string): The text content to display in the banner
- **end_date** (string): ISO 8601 formatted date/time when the banner should stop displaying

## How it Works

1. **Backend**: The `/banner` API endpoint retrieves the configuration from the database
2. **Frontend**: On page load, JavaScript fetches the banner configuration
3. **Auto-hide**: The banner is hidden if:
   - `enabled` is `false`
   - Current date/time is after `end_date`
   - The API request fails

## Benefits

- No code changes required to update banner content
- Automatic expiration prevents displaying outdated information
- Can be easily enabled/disabled without deployment
- Supports future enhancements like multiple banners or scheduling

## Updating the Banner

To update the banner, simply modify the document in the MongoDB `banner` collection. No code deployment is needed.
# Test
