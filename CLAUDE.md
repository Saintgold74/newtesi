# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Italian academic thesis (tesi di laurea) on IT infrastructure, cloud security, and compliance in retail/GDO (Grande Distribuzione Organizzata) sector. The document uses XeLaTeX with Arial font family and follows strict Italian academic formatting requirements.

## Build Commands

### Windows
- **Full compilation with bibliography**: `compila.bat`
  - Runs complete XeLaTeX → BibTeX → XeLaTeX → XeLaTeX sequence
  - Checks system requirements and opens PDF when complete
- **Quick compilation (no bibliography)**: `compila_veloce.bat`  
  - Single XeLaTeX pass for quick preview of text changes
- **Clean temporary files**: `pulisci.bat`
  - Removes all LaTeX temporary files (.aux, .bbl, .log, .synctex.gz, etc.)
- **System verification**: `verifica_sistema.bat`
  - Checks XeLaTeX installation, Arial fonts, and project structure

### macOS/Linux
```bash
# Full compilation with bibliography
xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex

# Quick compilation (no bibliography)
xelatex main.tex

# Clean build artifacts
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.glo *.ist bu*.aux bu*.bbl
```

## Architecture and Structure

### Document Structure
The thesis uses a modular LaTeX architecture with `main.tex` as the master document that includes:
- `main.tex` - Master document with preamble and document structure
- `capitoli/` - Individual chapters (new1.tex through new5.tex, new4-2.tex)
- `bibliografia/` - Bibliography files (.bib format) with per-chapter references
- `figure/` - Graphics and figure generation system
- `frontespizio.tex` - Title page
- `prefazione.tex` - Preface

### Chapter Organization
1. **Capitolo 1** (`capitoli/new1.tex`) - Introduction and research context
2. **Capitolo 2** (`capitoli/new2.tex`) - Threat landscape and security
3. **Capitolo 3** (`capitoli/new3.tex`) - Infrastructure evolution
4. **Capitolo 4** (`capitoli/new4-2.tex`) - Compliance and regulatory aspects  
5. **Capitolo 5** (`capitoli/new5.tex`) - Synthesis and conclusions (following GIST framework)

### Figure Generation System
- Python scripts in `figure/thesis_figures/` generate academic-quality plots
- Figures are organized by chapter (cap1/, cap2/, etc.)
- Scripts use matplotlib with academic styling and LaTeX font integration
- Generated figures are saved as both PDF and PNG formats
- Dependencies: numpy, matplotlib, seaborn, pandas, scipy

## Technical Requirements

### LaTeX Engine Requirements
- **XeLaTeX** is required (not pdfLaTeX or LuaLaTeX) for fontspec/Arial support
- **Arial font** must be installed (Windows system font)
- **BibTeX** for bibliography processing with `bibunits` package for per-chapter references

### Academic Formatting
- 12pt font size with hierarchical section sizing
- Italian language via Polyglossia package
- Specific margin requirements: top/bottom 3.5cm, left 4.5cm, right 3cm
- 1.5 line spacing and 1.25cm paragraph indentation
- Footnote numbering resets per chapter with parentheses format
- Professional code listings with syntax highlighting

### Package Dependencies
Key packages: fontspec, polyglossia, biblatex, csquotes, tikz, pgfplots, listings, hyperref, geometry, setspace, titlesec, tcolorbox, glossaries

### Bibliography Management
- Uses BibLaTeX with authoryear style and Italian formatting
- Bibliography stored in `bibliografia/newtesi_ref.bib`
- Author names formatted in small caps per Italian academic standards
- Supports multiple citation styles and automatic URL formatting

## Working with Figures

When modifying or creating figures:
1. Use the existing Python scripts as templates
2. Maintain consistent color palette and styling
3. Export as both PDF (for LaTeX) and PNG (for preview)
4. Place generated figures in appropriate chapter subdirectories
5. Update LaTeX references using standardized naming: `fig_X_Y_description` where X=chapter, Y=figure number

## Development Workflow

1. Make content changes in appropriate `.tex` files
2. Run `compila_veloce.bat` for quick preview of text changes
3. Run `compila.bat` for full compilation when adding citations or figures
4. Use `pulisci.bat` to clean up before commits
5. Run `verifica_sistema.bat` if encountering compilation issues

## Critical Notes

1. **XeLaTeX only** - pdfLaTeX will fail due to fontspec requirements
2. **Full compilation sequence** required after bibliography changes: XeLaTeX → BibTeX → XeLaTeX → XeLaTeX
3. **Working directory**: All commands assume execution from project root where `main.tex` is located
4. **Italian language**: All content must maintain Italian academic writing standards
5. **Glossary compilation**: Run `makeglossaries main` if glossary entries are modified
