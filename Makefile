# Makefile for running notebooks and building the Jupyter Book
#
# Usage:
#   make help          - Show available commands
#   make all           - Run all lecture notebooks
#   make run-lectures  - Run all lecture notebooks (same as all)
#   make run-homework  - Run all homework notebooks
#   make run-00        - Run a specific lecture notebook (00-13)
#   make hw-01         - Run a specific homework notebook (01-13, project)
#   make build-book    - Build the Jupyter Book
#   make clean         - Clean up build artifacts

# =============================================================================
# Configuration
# =============================================================================

# Use the project's virtual environment directly
VENV_BIN = .venv/bin

# Jupyter command for executing notebooks
# Uses nbconvert to execute notebooks in place
JUPYTER_EXEC = $(VENV_BIN)/jupyter nbconvert --to notebook --execute --inplace

# Base directory for lecture notebooks
NOTEBOOK_DIR = dsmles

# =============================================================================
# Lecture notebook paths
# =============================================================================

NOTEBOOK_00 = $(NOTEBOOK_DIR)/00-introduction/introduction.ipynb
NOTEBOOK_01 = $(NOTEBOOK_DIR)/01-numpy/numpy.ipynb
NOTEBOOK_02 = $(NOTEBOOK_DIR)/02-pandas-intro/pandas-intro.ipynb
NOTEBOOK_03 = $(NOTEBOOK_DIR)/03-intermediate-pandas/intermediate-pandas.ipynb
NOTEBOOK_04 = $(NOTEBOOK_DIR)/04-feature-engineering/feature-engineering.ipynb
NOTEBOOK_05 = $(NOTEBOOK_DIR)/05-dimensionality-reduction/dimensionality-reduction.ipynb
NOTEBOOK_06 = $(NOTEBOOK_DIR)/06-linear-regression/linear-regression.ipynb
NOTEBOOK_07 = $(NOTEBOOK_DIR)/07-classification/classification.ipynb
NOTEBOOK_08 = $(NOTEBOOK_DIR)/08-regularization-model-selection/regularization-model-selection.ipynb
NOTEBOOK_09 = $(NOTEBOOK_DIR)/09-nonlinear-methods/nonlinear-methods.ipynb
NOTEBOOK_10 = $(NOTEBOOK_DIR)/10-ensemble-methods/ensemble-methods.ipynb
NOTEBOOK_11 = $(NOTEBOOK_DIR)/11-clustering/clustering.ipynb
NOTEBOOK_12 = $(NOTEBOOK_DIR)/12-uncertainty-quantification/uncertainty-quantification.ipynb
NOTEBOOK_13 = $(NOTEBOOK_DIR)/13-model-interpretability/model-interpretability.ipynb

# All lecture notebooks in order
ALL_NOTEBOOKS = $(NOTEBOOK_00) $(NOTEBOOK_01) $(NOTEBOOK_02) $(NOTEBOOK_03) \
                $(NOTEBOOK_04) $(NOTEBOOK_05) $(NOTEBOOK_06) $(NOTEBOOK_07) \
                $(NOTEBOOK_08) $(NOTEBOOK_09) $(NOTEBOOK_10) $(NOTEBOOK_11) \
                $(NOTEBOOK_12) $(NOTEBOOK_13)

# =============================================================================
# Homework notebook paths
# =============================================================================

HW_DIR = $(NOTEBOOK_DIR)/assignments

HW_01 = $(HW_DIR)/hw01-numpy.ipynb
HW_02 = $(HW_DIR)/hw02-pandas-intro.ipynb
HW_03 = $(HW_DIR)/hw03-intermediate-pandas.ipynb
HW_04 = $(HW_DIR)/hw04-feature-engineering.ipynb
HW_05 = $(HW_DIR)/hw05-dimensionality-reduction.ipynb
HW_06 = $(HW_DIR)/hw06-linear-regression.ipynb
HW_07 = $(HW_DIR)/hw07-classification.ipynb
HW_08 = $(HW_DIR)/hw08-regularization.ipynb
HW_09 = $(HW_DIR)/hw09-nonlinear-methods.ipynb
HW_10 = $(HW_DIR)/hw10-ensemble-methods.ipynb
HW_11 = $(HW_DIR)/hw11-clustering.ipynb
HW_12 = $(HW_DIR)/hw12-uncertainty-quantification.ipynb
HW_13 = $(HW_DIR)/hw13-model-interpretability.ipynb
HW_PROJECT = $(HW_DIR)/project.ipynb

ALL_HOMEWORK = $(HW_01) $(HW_02) $(HW_03) $(HW_04) $(HW_05) $(HW_06) $(HW_07) \
               $(HW_08) $(HW_09) $(HW_10) $(HW_11) $(HW_12) $(HW_13) $(HW_PROJECT)

# =============================================================================
# Phony targets (targets that don't represent files)
# =============================================================================

.PHONY: all run-lectures run-homework help clean build-book sync \
        run-00 run-01 run-02 run-03 run-04 run-05 run-06 run-07 \
        run-08 run-09 run-10 run-11 run-12 run-13 \
        hw-01 hw-02 hw-03 hw-04 hw-05 hw-06 hw-07 \
        hw-08 hw-09 hw-10 hw-11 hw-12 hw-13 hw-project

# =============================================================================
# Main targets
# =============================================================================

# Default target: run all lecture notebooks
all: run-lectures

# Run all lecture notebooks
run-lectures: run-00 run-01 run-02 run-03 run-04 run-05 run-06 run-07 \
              run-08 run-09 run-10 run-11 run-12 run-13
	@echo "All lecture notebooks executed successfully!"

# =============================================================================
# Individual notebook targets
# =============================================================================

run-00:
	@echo "Running: $(NOTEBOOK_00)"
	$(JUPYTER_EXEC) $(NOTEBOOK_00)

run-01:
	@echo "Running: $(NOTEBOOK_01)"
	$(JUPYTER_EXEC) $(NOTEBOOK_01)

run-02:
	@echo "Running: $(NOTEBOOK_02)"
	$(JUPYTER_EXEC) $(NOTEBOOK_02)

run-03:
	@echo "Running: $(NOTEBOOK_03)"
	$(JUPYTER_EXEC) $(NOTEBOOK_03)

run-04:
	@echo "Running: $(NOTEBOOK_04)"
	$(JUPYTER_EXEC) $(NOTEBOOK_04)

run-05:
	@echo "Running: $(NOTEBOOK_05)"
	$(JUPYTER_EXEC) $(NOTEBOOK_05)

run-06:
	@echo "Running: $(NOTEBOOK_06)"
	$(JUPYTER_EXEC) $(NOTEBOOK_06)

run-07:
	@echo "Running: $(NOTEBOOK_07)"
	$(JUPYTER_EXEC) $(NOTEBOOK_07)

run-08:
	@echo "Running: $(NOTEBOOK_08)"
	$(JUPYTER_EXEC) $(NOTEBOOK_08)

run-09:
	@echo "Running: $(NOTEBOOK_09)"
	$(JUPYTER_EXEC) $(NOTEBOOK_09)

run-10:
	@echo "Running: $(NOTEBOOK_10)"
	$(JUPYTER_EXEC) $(NOTEBOOK_10)

run-11:
	@echo "Running: $(NOTEBOOK_11)"
	$(JUPYTER_EXEC) $(NOTEBOOK_11)

run-12:
	@echo "Running: $(NOTEBOOK_12)"
	$(JUPYTER_EXEC) $(NOTEBOOK_12)

run-13:
	@echo "Running: $(NOTEBOOK_13)"
	$(JUPYTER_EXEC) $(NOTEBOOK_13)

# =============================================================================
# Homework notebook targets
# =============================================================================

# Run all homework notebooks
run-homework: hw-01 hw-02 hw-03 hw-04 hw-05 hw-06 hw-07 \
              hw-08 hw-09 hw-10 hw-11 hw-12 hw-13 hw-project
	@echo "All homework notebooks executed successfully!"

hw-01:
	@echo "Running: $(HW_01)"
	$(JUPYTER_EXEC) $(HW_01)

hw-02:
	@echo "Running: $(HW_02)"
	$(JUPYTER_EXEC) $(HW_02)

hw-03:
	@echo "Running: $(HW_03)"
	$(JUPYTER_EXEC) $(HW_03)

hw-04:
	@echo "Running: $(HW_04)"
	$(JUPYTER_EXEC) $(HW_04)

hw-05:
	@echo "Running: $(HW_05)"
	$(JUPYTER_EXEC) $(HW_05)

hw-06:
	@echo "Running: $(HW_06)"
	$(JUPYTER_EXEC) $(HW_06)

hw-07:
	@echo "Running: $(HW_07)"
	$(JUPYTER_EXEC) $(HW_07)

hw-08:
	@echo "Running: $(HW_08)"
	$(JUPYTER_EXEC) $(HW_08)

hw-09:
	@echo "Running: $(HW_09)"
	$(JUPYTER_EXEC) $(HW_09)

hw-10:
	@echo "Running: $(HW_10)"
	$(JUPYTER_EXEC) $(HW_10)

hw-11:
	@echo "Running: $(HW_11)"
	$(JUPYTER_EXEC) $(HW_11)

hw-12:
	@echo "Running: $(HW_12)"
	$(JUPYTER_EXEC) $(HW_12)

hw-13:
	@echo "Running: $(HW_13)"
	$(JUPYTER_EXEC) $(HW_13)

hw-project:
	@echo "Running: $(HW_PROJECT)"
	$(JUPYTER_EXEC) $(HW_PROJECT)

# =============================================================================
# Setup targets
# =============================================================================

# Install/sync dependencies with uv
sync:
	@echo "Installing dependencies with uv..."
	uv sync --no-install-project
	@echo "Dependencies installed!"

# =============================================================================
# Build targets
# =============================================================================

# Build the Jupyter Book
build-book:
	@echo "Building Jupyter Book..."
	$(VENV_BIN)/jupyter-book build $(NOTEBOOK_DIR)
	@echo "Jupyter Book built successfully!"
	@echo "Open $(NOTEBOOK_DIR)/_build/html/index.html to view the book."

# =============================================================================
# Clean targets
# =============================================================================

# Clean up build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf $(NOTEBOOK_DIR)/_build
	rm -rf .ipynb_checkpoints
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"

# =============================================================================
# Help target
# =============================================================================

help:
	@echo "Makefile for running lecture notebooks and building the Jupyter Book"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Setup:"
	@echo "  sync          Install dependencies with uv"
	@echo ""
	@echo "Main targets:"
	@echo "  all           Run all lecture notebooks (default)"
	@echo "  run-lectures  Run all lecture notebooks"
	@echo "  run-homework  Run all homework notebooks"
	@echo "  build-book    Build the Jupyter Book"
	@echo "  clean         Clean up build artifacts"
	@echo "  help          Show this help message"
	@echo ""
	@echo "Lecture notebook targets:"
	@echo "  run-00        Run 00-introduction/introduction.ipynb"
	@echo "  run-01        Run 01-numpy/numpy.ipynb"
	@echo "  run-02        Run 02-pandas-intro/pandas-intro.ipynb"
	@echo "  run-03        Run 03-intermediate-pandas/intermediate-pandas.ipynb"
	@echo "  run-04        Run 04-feature-engineering/feature-engineering.ipynb"
	@echo "  run-05        Run 05-dimensionality-reduction/dimensionality-reduction.ipynb"
	@echo "  run-06        Run 06-linear-regression/linear-regression.ipynb"
	@echo "  run-07        Run 07-classification/classification.ipynb"
	@echo "  run-08        Run 08-regularization-model-selection/regularization-model-selection.ipynb"
	@echo "  run-09        Run 09-nonlinear-methods/nonlinear-methods.ipynb"
	@echo "  run-10        Run 10-ensemble-methods/ensemble-methods.ipynb"
	@echo "  run-11        Run 11-clustering/clustering.ipynb"
	@echo "  run-12        Run 12-uncertainty-quantification/uncertainty-quantification.ipynb"
	@echo "  run-13        Run 13-model-interpretability/model-interpretability.ipynb"
	@echo ""
	@echo "Homework notebook targets:"
	@echo "  hw-01         Run hw01-numpy.ipynb"
	@echo "  hw-02         Run hw02-pandas-intro.ipynb"
	@echo "  hw-03         Run hw03-intermediate-pandas.ipynb"
	@echo "  hw-04         Run hw04-feature-engineering.ipynb"
	@echo "  hw-05         Run hw05-dimensionality-reduction.ipynb"
	@echo "  hw-06         Run hw06-linear-regression.ipynb"
	@echo "  hw-07         Run hw07-classification.ipynb"
	@echo "  hw-08         Run hw08-regularization.ipynb"
	@echo "  hw-09         Run hw09-nonlinear-methods.ipynb"
	@echo "  hw-10         Run hw10-ensemble-methods.ipynb"
	@echo "  hw-11         Run hw11-clustering.ipynb"
	@echo "  hw-12         Run hw12-uncertainty-quantification.ipynb"
	@echo "  hw-13         Run hw13-model-interpretability.ipynb"
	@echo "  hw-project    Run project.ipynb"
