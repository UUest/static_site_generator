# Static Site Generator

A Python-based static site generator that converts Markdown files to HTML with support for GitHub Pages deployment.

## Features

- Converts Markdown content to HTML
- Supports nested directory structures
- Copies static assets (CSS, images, etc.)
- GitHub Pages deployment ready
- Local development support

## Project Structure

```
static_site_generator/
├── content/           # Markdown source files
├── static/           # Static assets (CSS, images)
├── docs/             # Generated HTML files (GitHub Pages output)
├── src/              # Python source code
├── template.html     # HTML template
├── build.sh          # GitHub Pages build script
└── build-local.sh    # Local development build script
```

## Usage

### For GitHub Pages Deployment

1. Update the basepath in `build.sh` to match your repository name:
   ```bash
   python3 src/main.py "/your-repository-name"
   ```

2. Run the build script:
   ```bash
   ./build.sh
   ```

3. Commit and push the changes to your repository.

4. Enable GitHub Pages in your repository settings, pointing to the `docs/` folder.

### For Local Development

1. Run the local build script:
   ```bash
   ./build-local.sh
   ```

2. Serve the files locally:
   ```bash
   cd docs && python3 -m http.server 8000
   ```

3. Visit `http://localhost:8000` in your browser.

## Adding Content

1. Create Markdown files in the `content/` directory
2. Use the following structure for nested pages:
   ```
   content/
   ├── index.md
   ├── about/
   │   └── index.md
   └── blog/
       ├── post1/
       │   └── index.md
       └── post2/
           └── index.md
   ```

3. Add static assets to the `static/` directory

4. Rebuild the site using the appropriate build script

## Template Variables

The HTML template supports the following variables:

- `{{ Title }}` - Page title extracted from the Markdown
- `{{ Content }}` - Converted HTML content
- `{{ BasePath }}` - Base path for deployment (GitHub Pages repository name)

## Link and Image Paths

- Use absolute paths starting with `/` in your Markdown files
- The generator will automatically add the correct basepath for deployment
- Example: `[Link](/about)` becomes `/repository-name/about` for GitHub Pages

## Requirements

- Python 3.x
- Custom modules: `blockfuncs`, `extract_title` (included in `src/`)

## Troubleshooting

### Links not working on GitHub Pages

Make sure you're using the correct basepath in `build.sh`. The basepath should match your repository name exactly.

### CSS not loading

Verify that the CSS file is in the `static/` directory and that the build script successfully copies it to `docs/`.

### Images not displaying

Ensure images are in the `static/images/` directory and referenced with absolute paths in your Markdown files (e.g., `/images/photo.jpg`).