from src.extract import Extract
from src.load import Load


extract = Extract()
load = Load()

brazil = extract.extract_data("Brazil")
load.load_data_sqlite(brazil, "tabela_brazil")

