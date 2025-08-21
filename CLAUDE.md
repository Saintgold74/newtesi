# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Italian academic thesis project about cybersecurity and infrastructure in the retail/GDO (Grande Distribuzione Organizzata) sector. The thesis is written in LaTeX using XeLaTeX with Arial font to meet specific university requirements.

## Build and Development Commands

### Compilation
- **Full compilation with bibliography**: `compila.bat`
  - Runs complete XeLaTeX compilation cycle with bibliography processing
  - Checks for system requirements and opens PDF when complete
- **Quick compilation (no bibliography)**: `compila_veloce.bat`  
  - Fast compilation for text-only changes
- **Clean temporary files**: `pulisci.bat`
  - Removes all LaTeX temporary files (.aux, .log, .synctex.gz, etc.)
- **System verification**: `verifica_sistema.bat`
  - Checks XeLaTeX installation, Arial fonts, and project structure

### LaTeX Engine Requirements
- **XeLaTeX** is required (not pdfLaTeX or LuaLaTeX)
- **Arial font** must be installed (Windows system font)
- **BibTeX/Biber** for bibliography processing

## Architecture and Structure

### Document Structure
- `main.tex` - Main document with preamble and document structure
- `capitoli/` - Individual chapters (new1.tex through new5.tex, new4-2.tex)
- `bibliografia/` - Bibliography files (.bib format)
- `figure/` - Graphics and figure generation
- `frontespizio.tex` - Title page
- `prefazione.tex` - Preface

### Chapter Organization
1. **Capitolo 1** (`capitoli/new1.tex`) - Introduction and research context
2. **Capitolo 2** (`capitoli/new2.tex`) - Threat landscape and security
3. **Capitolo 3** (`capitoli/new3.tex`) - Infrastructure evolution
4. **Capitolo 4** (`capitoli/new4-2.tex`) - Compliance and regulatory aspects  
5. **Capitolo 5** (`capitoli/new5.tex`) - Synthesis and conclusions

### Figure Generation System
- Python scripts in `figure/thesis_figures/` generate academic-quality plots
- Figures are organized by chapter (cap1/, cap2/, etc.)
- Scripts use matplotlib with academic styling and LaTeX font integration
- Generated figures are saved as both PDF and PNG formats

### Bibliography Management
- Uses BibLaTeX with `verbose` style and Italian formatting
- Bibliography stored in `bibliografia/newtesi_ref.bib`
- Author names formatted in small caps per Italian academic standards
- Supports multiple citation styles and automatic URL formatting

## LaTeX Configuration Details

### Font Configuration
- Uses XeLaTeX with native Arial font support
- Italian language via Polyglossia package
- Specific margin requirements: top/bottom 3.5cm, left 4.5cm, right 3cm
- 1.5 line spacing and 1.25cm paragraph indentation

### Academic Formatting
- 12pt font size with hierarchical section sizing
- Custom chapter and section title formatting
- Footnote numbering resets per chapter with parentheses format
- Professional code listings with syntax highlighting

### Package Dependencies
Key packages: fontspec, polyglossia, biblatex, csquotes, tikz, pgfplots, listings, hyperref, geometry, setspace, titlesec

## Working with Figures

When modifying or creating figures:
1. Use the existing Python scripts as templates
2. Maintain consistent color palette and styling
3. Export as both PDF (for LaTeX) and PNG (for preview)
4. Place generated figures in appropriate chapter subdirectories
5. Update LaTeX references using `\includegraphics{figure/path}`

## Development Workflow

1. Make content changes in appropriate `.tex` files
2. Run `compila_veloce.bat` for quick preview of text changes
3. Run `compila.bat` for full compilation when adding citations or figures
4. Use `pulisci.bat` to clean up before commits
5. Run `verifica_sistema.bat` if encountering compilation issues