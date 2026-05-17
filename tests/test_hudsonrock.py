from src.services.hudsonrock_service import check_email


def test_hudsonrock_api():

    response = check_email(
        "naoexiste987654321@proton.me"
    )

    assert response is not None

    assert "stealers" in response