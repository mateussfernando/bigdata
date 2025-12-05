import requests


class Extract: 

    def __init__(self): #Método Construtor
        pass

    def extract_data(self, country):
        """
        Método responsável por acessar a API e retornar os dados.
        """
        url = f"http://universities.hipolabs.com/search?country={country}"
        
        response = requests.get(url)
        response.raise_for_status()  
        universities = response.json()
        
        return universities