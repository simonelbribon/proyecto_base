from src.seme.pipeline import run_pipeline


def test_event_generation():
    result = run_pipeline("SALE-001")

    assert result["seme"] == "sale-001"
    assert result["final"] == "SALE-001"
