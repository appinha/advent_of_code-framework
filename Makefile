# Usage examples:
#   make day=01
#   make day=12 part=1
#   make new day=01

SOLVER = solver/solve_day.py

all:
	@PYTHONPATH=.:$PYTHONPATH python $(SOLVER) $(day) "input.txt" $(part)

test:
	@PYTHONPATH=".:$PYTHONPATH" python $(SOLVER) $(day) "input_test.txt" $(part)

new:
	@[ ! -d ../day_$(day)/ ] && cp -R day_template ../day_$(day)/
