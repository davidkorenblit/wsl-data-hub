# Project Context & Overview

## Project Architecture

`wsl-data-hub` is a hybrid repository combining a Python data analytics pipeline with a GitHub Pages Jekyll blog configured for Hebrew Right-to-Left (RTL) publishing.

### Folder Structure
- `_posts/`: Jekyll markdown blog posts published automatically.
- `_layouts/default.html`: Custom HTML layout supporting Hebrew (`dir="rtl"`, `lang="he"`) and Rubik font.
- `assets/css/style.scss`: Dark-mode sports analytics SCSS stylesheet.
- `assets/images/previews/`: Directory where Python scripts output generated charts (radar plots, scatter plots).
- `data/raw/`: Raw scraped datasets (ignored by Git via `.gitignore`).
- `data/teams/`: Structured, processed CSVs for team analysis (tracked by Git).
- `scripts/`: Data fetching, normalization, and visualization Python scripts.
- `docs/`: Project documentation and research plan (`plan.md`).

## Deployment Settings
- **GitHub Pages**: Automatically deployed via GitHub Actions workflow `.github/workflows/deploy.yml`.
- **Baseurl**: `/wsl-data-hub`
- **URL**: `https://davidkorenblit.github.io`
