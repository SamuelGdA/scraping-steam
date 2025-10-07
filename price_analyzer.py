# price_analyzer.py - Versão Final Simplificada
# Esta função não é mais necessária, pois o steam_scraper fará tudo.
# Mantemos o arquivo para não quebrar a estrutura do main.py.

def get_price_history_from_steam(steam_data):
    """
    Extrai o preço histórico do dicionário de dados já coletado pelo steam_scraper.
    """
    if steam_data and 'lowest_price' in steam_data:
        return {
            "lowest_price": steam_data['lowest_price'],
            "analysis": steam_data['analysis']
        }
    return {"lowest_price": "Não encontrado", "analysis": "Extensão não carregou os dados"}