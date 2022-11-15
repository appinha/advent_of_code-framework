
import gc
import time


class Timer:
    _start_time: int | None = None
    _stop_time: int | None = None

    def start(self) -> None:
        gc.disable()  # disables garbage collect
        self._start_time = self._get_time()

    def stop(self) -> None:
        self._stop_time = self._get_time()
        gc.enable()  # enables garbage collect

    @property
    def elapsed_nanosec(self) -> int:
        self._validate_times()
        return self._stop_time - self._start_time

    @property
    def elapsed_sec(self) -> float:
        return self.elapsed_nanosec / 1e9

    def _get_time(self) -> int:
        return time.perf_counter_ns()

    def _validate_times(self):
        if self._start_time is None:
            raise ValueError("Timer has not been started.")
        if self._stop_time is None:
            raise ValueError("Timer has not been stopped.")
