import configparser

config = configparser.ConfigParser()
config.read("./years.ini")
years = config.sections()

def cargar_anio(year):
    year_config = config[year]
    return year_config['f']