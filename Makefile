# Usage examples:
#   make day=01
#   make day=04 part=1
#   make test day=08
#   make test day=12 part=2
#   make new day=01

SOLVER = solver/solve_day.py

DAY_ERROR = echo "❌ Error: day must be a number between 1 and 25"
COPY_ERROR = echo "❌ Error: folder already exists"
COPY_SUCCESS = echo "✅ Successfully created day_$(day) folder!"

CHECK_DAY = (($(day) >= 1 && $(day) <= 25))
CHECK_FOLDER = [ ! -d ../day_$(day)/ ]

COPY_TEMPLATE_FOLDER = cp -R day_template ../day_$(day)/ && $(COPY_SUCCESS)

GET_INPUT = python solver/get_input.py $(day)

TRY_TO_COPY_FOLDER_AND_GET_INPUT = if $(CHECK_FOLDER); then $(COPY_TEMPLATE_FOLDER) && $(GET_INPUT); else $(COPY_ERROR); fi

all:
	@python $(SOLVER) not_testing $(day) $(part)

.PHONY: test
test:
	@python $(SOLVER) testing $(day) $(part)

.PHONY: new
new:
	@if $(CHECK_DAY); then $(TRY_TO_COPY_FOLDER_AND_GET_INPUT); else $(DAY_ERROR); fi

.PHONY: input
input:
	@$(GET_INPUT)