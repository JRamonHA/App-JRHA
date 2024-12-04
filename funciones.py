import configparser

config = configparser.ConfigParser()
config.read("./years.ini")
years = config.sections()

def cargar_anio(year):
    """
    Carga la configuración del año especificado.

    Args:
        year (str): El año para el cual se desea cargar la configuración.

    Returns:
        dict: La configuración correspondiente al año especificado.
    """
    year_config = config[year]
    return year_config['f']