# Usage examples:
#   make day=1
#   make day=4 part=1
#   make test day=8
#   make test day=12 part=2
#   make new day=1

NEW_FOLDER = solver/new_folder.py
SOLVER = solver/solve_day.py
GET_INPUT = python solver/get_input.py

all:
	@python $(SOLVER) not_testing $(day) $(part)

.PHONY: test
test:
	@python $(SOLVER) testing $(day) $(part)

.PHONY: new
new:
	@python $(NEW_FOLDER) $(day)

.PHONY: input
input:
	@$(GET_INPUT) $(day)