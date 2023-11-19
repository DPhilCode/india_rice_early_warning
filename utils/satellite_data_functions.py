import os

def set_directories_and_api():
    """
    Set up the working directory and API url

    """
    inDir  = r'C:\Users\djava\OneDrive\Documents\Oxford\Projects\india_rice_early_warning'
    outDir = r'C:\Users\djava\OneDrive\Documents\Oxford\Projects\india_rice_early_warning\4_data\RAW_DATA'
    os.chdir(inDir)
    api_login = 'https://appeears.earthdatacloud.nasa.gov/api/login'
    api = api = 'https://appeears.earthdatacloud.nasa.gov/api/'

    return inDir, outDir, api_login, api