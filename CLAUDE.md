# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Italian academic thesis (tesi di laurea) on IT infrastructure, cloud security, and compliance in retail (GDO). Written in LaTeX using XeLaTeX with Arial font on Windows.

## Build Commands

### Full Compilation (with bibliography)
```bash
compila.bat
```
Performs complete compilation: XeLaTeX → BibTeX → XeLaTeX → XeLaTeX

### Quick Compilation (no bibliography)
```bash
compila_veloce.bat
```
Single XeLaTeX pass for quick preview

### Clean Build Artifacts
```bash
pulisci.bat
```
Removes temporary files (.aux, .bbl, .log, etc.)

### System Verification
```bash
verifica_sistema.bat
```
Checks XeLaTeX installation, fonts, and file structure

## Project Structure

### Core Files
- `main.tex` - Master document with all LaTeX configuration
- `frontespizio.tex` - Title page
- `prefazione.tex` - Preface

### Chapters (`capitoli/`)
- `new1.tex` - Introduction
- `new2.tex` - Threat analysis
- `new3.tex` - Cloud infrastructure
- `new4.tex` - Compliance
- `new5.tex` - Synthesis
- `appendice_*.tex` - Various appendices

### Bibliography (`bibliografia/`)
- `bibliografia.bib` - Main bibliography database
- `cap*_references.bib` - Chapter-specific references

### Figures (`figure/`)
- `thesis_figures/cap*/` - Generated figures by chapter
- Python scripts for automated figure generation

## LaTeX Configuration

### Document Class
```latex
\documentclass[11pt,a4paper,oneside]{book}
```

### Key Packages
- **fontspec** - Arial font family
- **polyglossia** - Italian language support
- **biblatex** - Advanced bibliography with per-chapter references
- **tikz** - Diagrams and graphics
- **listings** - Code highlighting
- **hyperref** - Clickable references

### Compilation Requirements
- XeLaTeX (not pdfLaTeX)
- Arial fonts (Windows system fonts)
- BibTeX/Biber for bibliography

## Figure Generation

Python scripts in `figure/` generate scientific plots:
- Dependencies: numpy, matplotlib, seaborn, pandas, scipy
- Output: PDF/PNG to `thesis_figures/cap*/`

## Important Notes

1. **Always use XeLaTeX**, not pdfLaTeX (font requirements)
2. **Run full compilation** (`compila.bat`) after bibliography changes
3. **Chapter files** are in `capitoli/` with `new*.tex` naming
4. **Bibliography entries** should go in `bibliografia.bib` or chapter-specific files
5. **Figures** should be generated via Python scripts and placed in appropriate `thesis_figures/cap*/` directory
6. **Language**: Document is in Italian - maintain Italian language in content
7. **Academic format**: Maintain 1.5 line spacing, specific margins as configured in main.tex