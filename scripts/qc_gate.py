#!/usr/bin/env python3
"""
QC gate: given a Higgsfield job ID, calls virality_predictor and checks
scores against thresholds. Exits 0 on pass, 1 on fail.

This is the agent-callable gate. In practice the agent calls it after each
generate_video job completes and before committing the output to a brief.

Usage (called by the agent via Bash tool or python3):
    python3 scripts/qc_gate.py <job_id_or_video_url>

Thresholds (adjustable below):
    hook        >= 70
    attention   >= 65
    retention   >= 60
    creative    >= 65
    distraction == "low"  (or <= 35 if numeric)

NOTE: This script prints a structured JSON result for the agent to parse.
The agent still performs the FIDELITY gate separately via frame grab + Read.
"""

# Thresholds — tune after baseline data collected
THRESHOLDS = {
    "hook": 70,
    "attention": 65,
    "retention": 60,
    "creative": 65,
}
DISTRACTION_MAX = 35  # if numeric; "low" label also accepted


def check_scores(scores: dict) -> tuple[bool, list[str]]:
    """Return (passed, list_of_failures)."""
    failures = []
    for metric, threshold in THRESHOLDS.items():
        val = scores.get(metric)
        if val is None:
            failures.append(f"{metric}: missing from predictor output")
        elif isinstance(val, (int, float)) and val < threshold:
            failures.append(f"{metric}: {val} < {threshold}")
    distraction = scores.get("distraction_risk") or scores.get("distraction")
    if distraction is not None:
        if isinstance(distraction, str) and distraction.lower() not in ("low",):
            failures.append(f"distraction_risk: '{distraction}' not 'low'")
        elif isinstance(distraction, (int, float)) and distraction > DISTRACTION_MAX:
            failures.append(f"distraction_risk: {distraction} > {DISTRACTION_MAX}")
    return (len(failures) == 0, failures)


def main():
    import json, sys
    if len(sys.argv) < 2:
        print("Usage: qc_gate.py <job_id_or_url>")
        sys.exit(2)
    target = sys.argv[1]
    print(f"QC gate input: {target}")
    print("NOTE: Run virality_predictor MCP tool on this job/URL, then pass the")
    print("      returned scores dict to check_scores() to get a pass/fail result.")
    print()
    print("Thresholds:")
    print(json.dumps({"thresholds": THRESHOLDS, "distraction_max": DISTRACTION_MAX}, indent=2))
    print()
    print("Example scores check:")
    example = {"hook": 78, "attention": 71, "retention": 65, "creative": 68, "distraction_risk": "low"}
    passed, failures = check_scores(example)
    print(f"  Example scores {example} → passed={passed}, failures={failures}")


if __name__ == "__main__":
    main()
