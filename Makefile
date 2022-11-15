# Usage examples:
#   make day=01
#   make day=04 part=1
#   make test day=08
#   make test day=12 part=2
#   make new day=01

SOLVER = solver/solve_day.py

all:
	@PYTHONPATH=.:$PYTHONPATH python $(SOLVER) not_testing $(day) $(part)

test:
	@PYTHONPATH=".:$PYTHONPATH" python $(SOLVER) testing $(day) $(part)

new:
	@[ ! -d ../day_$(day)/ ] && cp -R day_template ../day_$(day)/
