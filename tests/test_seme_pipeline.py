from src.seme.pipeline import run_pipeline


def test_pipeline_core():
    result = run_pipeline("Fast API SEME")

    assert result["seme"] == "fast api seme"
    assert result["final"] == "FAST API SEME"
