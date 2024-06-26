from pathlib import Path

PROJECT_DIRECTORY = Path(__file__).parent.parent.resolve()
SAMPLE_DIRECTORY = Path.joinpath(PROJECT_DIRECTORY, "samples")
REPORT_DIRECTORY = Path.joinpath(SAMPLE_DIRECTORY, "reports")
