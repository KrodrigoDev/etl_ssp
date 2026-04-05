"""
 Testes referente a classe htpp_requester
"""

from .http_requester import HttpRequester


def test_request_from_page():
    """
    Esse test tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT)
    - A: Assert - Garante que A é A
    """
    http_requester = HttpRequester()

    request_reponse = http_requester.request_from_page()

    assert "status_code" in request_reponse
