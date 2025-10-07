# steam_tag_scraper.py
import requests
from bs4 import BeautifulSoup
import json

def create_tag_map():
    """
    Visita a página de busca da Steam, extrai todas as tags e seus IDs,
    e salva em um arquivo JSON para uso futuro.
    """
    print("Iniciando a criação do mapa de tags da Steam...")
    try:
        url = "https://store.steampowered.com/search/"
        headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'pt-BR,pt;q=0.9'}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        tag_map = {}
        
        # Encontra a div que contém todos os filtros de tag
        tag_container = soup.find('div', id='TagFilter_Container')
        if not tag_container:
            print("ERRO: Não foi possível encontrar o container de tags na página da Steam.")
            return

        # Encontra todas as linhas de tag dentro do container
        tag_rows = tag_container.find_all('div', class_='tab_filter_control_row')
        
        for row in tag_rows:
            tag_name_element = row.find('span', class_='tab_filter_control_label')
            if tag_name_element and row.has_attr('data-value'):
                tag_name = tag_name_element.text.strip()
                tag_id = row['data-value']
                if tag_name and tag_id:
                    tag_map[tag_name] = tag_id
        
        if not tag_map:
            print("ERRO: Nenhuma tag foi encontrada. O HTML da Steam pode ter mudado.")
            return

        # Salva o dicionário em um arquivo JSON
        with open('steam_tags.json', 'w', encoding='utf-8') as f:
            json.dump(tag_map, f, indent=4, ensure_ascii=False)
            
        print(f"Sucesso! Mapa com {len(tag_map)} tags foi salvo em 'steam_tags.json'.")

    except Exception as e:
        print(f"Ocorreu um erro ao criar o mapa de tags: {e}")

if __name__ == "__main__":
    create_tag_map()