class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        times = [0] * n
        stack: list[int] = []
        prev_time = 0
        for log in logs:
            f_str, call, time_str = log.split(":")
            f = int(f_str)
            time = int(time_str)
            if call == "start":
                # add the time the function as been running so far
                if stack:
                    times[stack[-1]] += time - prev_time
                stack.append(f)
                prev_time = time
            else:
                prev_f = stack.pop()
                times[prev_f] += time - prev_time + 1
                prev_time = time + 1

        return times
