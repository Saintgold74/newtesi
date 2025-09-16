# Makefile per la generazione delle figure della tesi GIST

LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode

# Directory
CAP1_DIR = cap1
CAP2_DIR = cap2

# Figure Capitolo 1
CAP1_FIGS = evoluzione_attacchi thesis_structure

# Figure Capitolo 2  
CAP2_FIGS = topologia_rete evoluzione_ransomware zero_trust_architecture confronto_metriche roi_analysis

# Target principale
all: cap1 cap2

cap1: $(CAP1_FIGS:%=$(CAP1_DIR)/%.pdf)

cap2: $(CAP2_FIGS:%=$(CAP2_DIR)/%.pdf)

# Regola generica per compilare i PDF
%.pdf: %.tex
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(dir $@) $<
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(dir $@) $<

# Pulizia
clean:
	rm -f $(CAP1_DIR)/*.aux $(CAP1_DIR)/*.log $(CAP1_DIR)/*.out
	rm -f $(CAP2_DIR)/*.aux $(CAP2_DIR)/*.log $(CAP2_DIR)/*.out

clean-all: clean
	rm -f $(CAP1_DIR)/*.pdf
	rm -f $(CAP2_DIR)/*.pdf

.PHONY: all cap1 cap2 clean clean-all
