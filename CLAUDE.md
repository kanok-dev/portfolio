# CLAUDE.md
ี--
This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **portfolio showcase repository** containing screenshots and images from various completed projects. It is NOT a traditional development codebase - there are no build processes, dependencies, or code to compile.

The repository includes:
- Project screenshots organized in subdirectories by project name and technology
- A single static HTML file (`index.html`) that displays all portfolio images in a responsive gallery

## Repository Structure

```
Potforilo-Images/
├── index.html                              # Main portfolio gallery page
├── Stack (NextJs)/                         # Tournament/enrollment platform screenshots
├── KUGarden (ReactJs)/                     # Garden management app screenshots
├── Kanok.me (NextJs)/                      # Personal website screenshot
├── Lotto (NextJs)/                         # Lottery app screenshot
├── LuckyNumberMagic (ReactJs)/             # Lucky number generator screenshot
├── SmartSales (C#,Jquery)/                 # Sales management system screenshots
├── Sport-Games (NextJs)/                   # Sports competition platform screenshots
├── Stock Portfolio Manager (ReactJs)/      # Stock trading portfolio screenshots
├── eOrder-Mobile/                          # Mobile ordering app screenshots
├── Cover-FullStack-Image.png              # Portfolio cover images
├── Cover-FullStack-With-My-Image.jpg
└── Cover-Image-Refactor-Code.png
```

## Project Categories

### Next.js Projects
- **Stack**: Tournament enrollment platform with admin dashboard
- **Kanok.me**: Personal portfolio website
- **Lotto**: Lottery number checking application
- **Sport-Games**: Sports competition management with leaderboards

### React.js Projects
- **KUGarden**: University garden/facilities management
- **LuckyNumberMagic**: Lucky number generator
- **Stock Portfolio Manager**: Comprehensive stock trading portfolio tracker

### Other Technologies
- **SmartSales**: Inventory and sales management system (C#, jQuery)
- **eOrder-Mobile**: Mobile ordering application

## The Gallery Page (index.html)

The `index.html` file is a standalone, self-contained gallery that:
- Uses Tailwind CSS (via CDN) for styling
- Displays projects in categorized sections with technology badges
- Implements a modal lightbox for viewing full-size images
- Requires no build process or dependencies
- Can be opened directly in any browser

## Working with This Repository

### Viewing the Gallery
Simply open `index.html` in a web browser. No server or build process needed.

### Adding New Projects
To add a new project to the gallery:
1. Create a new directory with format: `ProjectName (Technology)`
2. Add screenshot images to the directory
3. Update `index.html` to add a new `<section class="project-section">` with:
   - Project title and technology badge
   - Grid of image cards with onclick handlers
   - Proper image paths relative to the HTML file

### Modifying the Gallery
- The HTML file uses inline styles and Tailwind utility classes
- Modal functionality is handled by vanilla JavaScript at the bottom of the file
- Image paths use relative paths with `../` prefix
- Responsive grid: 1 column (mobile) → 2 (sm) → 3 (lg) → 4 (xl)

### Image Organization
- Each project subdirectory contains only image files (PNG, JPG, WebP)
- No source code exists in this repository
- Image filenames describe the page/feature shown (e.g., "Dashboard-page.png")

## Important Notes

- This is **not a development project** - it's a collection of screenshots from completed work
- There are no package managers, build tools, or dependencies to install
- The HTML file is intentionally standalone for easy deployment
- Images are referenced using relative paths, so directory structure must be maintained
