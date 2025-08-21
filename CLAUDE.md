# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Italian academic thesis (tesi di laurea) on IT infrastructure, cloud security, and compliance in retail (GDO) sector. The document uses XeLaTeX with Arial font family and follows strict Italian academic formatting requirements.

## Build Commands

### macOS/Linux
```bash
# Full compilation with bibliography
xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex

# Quick compilation (no bibliography)
xelatex main.tex

# Clean build artifacts
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.glo *.ist bu*.aux bu*.bbl
```

### Windows
```bash
compila.bat          # Full compilation: XeLaTeX → BibTeX → XeLaTeX → XeLaTeX
compila_veloce.bat   # Single XeLaTeX pass for quick preview
pulisci.bat          # Remove temporary files (.aux, .bbl, .log, etc.)
verifica_sistema.bat # Check XeLaTeX installation, fonts, and file structure
```

## Architecture

### Document Structure
The thesis uses a modular LaTeX architecture with `main.tex` as the master document that includes:
- Per-chapter bibliography management using `bibunits` package
- Automatic figure generation pipeline from Python scripts
- Strict formatting adherence to Italian academic standards (1.5 line spacing, specific margins: top/bottom 3.5cm, left 4.5cm, right 3cm)

### Key Components
- **Master document**: `main.tex` - Contains all package configurations and document settings
- **Chapters**: `capitoli/new[1-5].tex` - Main content chapters following GIST framework
- **Bibliography**: Distributed across `bibliografia/*.bib` files with per-chapter references
- **Figure Generation**: Python scripts in `figure/` automatically generate scientific plots exported to `thesis_figures/cap*/`

## Technical Requirements

### Compilation
- **Engine**: XeLaTeX (required for fontspec/Arial support)
- **Bibliography**: BibTeX with `bibunits` package for per-chapter references
- **Font**: Arial (system font on Windows/macOS)
- **Key packages**: fontspec, polyglossia (Italian), tikz, pgfplots, tcolorbox, glossaries

### Figure Pipeline
Python scripts generate publication-quality figures:
```bash
# Example: Generate all Chapter 3 figures
python figure/thesis_figures/cap3/generate_all_chapter3_figures.py
```
Dependencies: numpy, matplotlib, seaborn, pandas, scipy

## Critical Notes

1. **XeLaTeX only** - pdfLaTeX will fail due to fontspec requirements
2. **Full compilation sequence** required after bibliography changes: XeLaTeX → BibTeX → XeLaTeX → XeLaTeX
3. **Working directory**: All commands assume execution from project root where `main.tex` is located
4. **Figure references**: Use standardized naming: `fig_X_Y_description` where X=chapter, Y=figure number
5. **Italian language**: All content must maintain Italian academic writing standards
6. **Glossary compilation**: Run `makeglossaries main` if glossary entries are modified