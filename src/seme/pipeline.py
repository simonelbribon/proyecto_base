def run_pipeline(text: str) -> dict:
    """
    Pipeline SEME puro.
    No depende de FastAPI, ni request, ni HTTP.
    """

    if not text:
        return {
            "seme": "",
            "final": ""
        }

    # 🔹 Etapa SEME (transformación intermedia)
    seme = text.lower().strip()

    # 🔹 Etapa FINAL (resultado procesado)
    final = seme.upper()

    return {
        "seme": seme,
        "final": final
    }
