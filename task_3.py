experiments_data = [
    {"method": "Euler", "iteration": 1, "error": 0.15, "time_ms": 1.2},
    {"method": "Runge-Kutta", "iteration": 1, "error": 0.01, "time_ms": 3.5},
    {"method": "Euler", "iteration": 2, "error": 0.18, "time_ms": 1.3},
    {"method": "Runge-Kutta", "iteration": 2, "error": 0.008, "time_ms": 3.6},
    {"method": "Euler", "iteration": 3, "error": 0.22, "time_ms": 1.2},
    {"method": "Newton", "iteration": 1, "error": 0.05, "time_ms": 2.1}
]
def analyze_methods(data):
    report = {}
    for entry in data:
        method = entry["method"]
        error = entry["error"]
        time_ms = entry["time_ms"]
        if method not in report:
            report[method] = {
            "max_error" : 0,
            "total_time_ms" : 0,
            "iterations_count":0 }
        stats = report[method]
        stats["max_error"] = max(stats["max_error"], error)
        stats["total_time_ms"] += time_ms
        stats["iterations_count"] += 1
    return report
final_report = analyze_methods(experiments_data)
print("Звіт")
for method in final_report:
    print(f"• {method:12} | {final_report[method]}")










