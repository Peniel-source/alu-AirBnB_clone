# AirBnB Clone - Web Static

This directory contains the front-end HTML/CSS implementation for the AirBnB clone project.

## Project Structure

```
web_static/
├── 0-index.html          # Task 0: Inline styling
├── 1-index.html          # Task 1: Head styling
├── 2-index.html          # Task 2: CSS files
├── 3-index.html          # Task 3: Zoning with logo
├── 4-index.html          # Task 4: Search button
├── 5-index.html          # Task 5: More filters
├── 6-index.html          # Task 6: Dropdown hover
├── 7-index.html          # Task 7: Display results
├── 8-index.html          # Task 8: More details
├── styles/               # CSS files
│   ├── 2-common.css
│   ├── 2-header.css
│   ├── 2-footer.css
│   ├── 3-common.css
│   ├── 3-header.css
│   ├── 3-footer.css
│   ├── 4-common.css
│   ├── 4-filters.css
│   ├── 5-filters.css
│   ├── 6-filters.css
│   ├── 7-places.css
│   └── 8-places.css
└── images/               # Image assets
    ├── icon.png
    ├── logo.png
    ├── icon_guests.png
    ├── icon_bedrooms.png
    └── icon_bathrooms.png
```

## Tasks Overview

### Task 0: Inline Styling
- Basic HTML structure with inline styles
- Red header (70px) and green footer (60px)
- Footer fixed to bottom

### Task 1: Head Styling
- Moved styles to `<style>` tag in `<head>`
- Same layout as Task 0

### Task 2: CSS Files
- Separated styles into external CSS files
- 3 CSS files: common, header, footer

### Task 3: Zoning Done
- Added global font styles (Circular, 14px, #484848)
- White backgrounds with borders
- Logo in header, favicon added

### Task 4: Search Button
- Added container (max-width 1000px, centered)
- Filters section with search button
- Button hover effect (90% opacity)

### Task 5: More Filters
- Added Locations and Amenities filter divs
- H3 titles and H4 subtitles
- 25% width each with border separator

### Task 6: Dropdown Hover
- Added dropdown menus (ul.popover)
- Hidden by default, shown on hover
- 2-level structure for locations (states → cities)

### Task 7: Display Results
- Added places section with listings
- Article elements for each place
- 390px width, inline-block layout

### Task 8: More Details
- Price badge (circular, top-right)
- Information section (guests, rooms, bathrooms with icons)
- User section with owner name
- Description section

## Design Specifications

### Colors
- Primary: #FF5A5F (red/pink)
- Text: #484848 (dark gray)
- Borders: #DDDDDD, #CCCCCC (light gray)
- Background: #FAFAFA (off-white)

### Typography
- Font Family: Circular, "Helvetica Neue", Helvetica, Arial, sans-serif
- Base Size: 14px
- Headings: 16px, 30px

### Layout
- Container: max-width 1000px, centered
- Header: 70px height
- Footer: 60px height, fixed bottom
- Filters: 70px height
- Places: 390px width per article

## Compliance

✅ No `!important` in CSS
✅ No ID selectors (#) in CSS
✅ No JavaScript
✅ No inline styles (except Task 0)
✅ Semantic HTML tags (header, footer)
✅ All files end with newline
✅ W3C compliant HTML/CSS

## Viewing the Pages

Open any HTML file in a web browser:
```bash
# Example
firefox web_static/8-index.html
# or
google-chrome web_static/8-index.html
```

## Notes

- This is a static front-end only project
- No backend or dynamic data
- Progressive enhancement from Task 0 to Task 8
- Each task builds upon previous tasks
