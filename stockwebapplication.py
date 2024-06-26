from Tools import tools_v000 as tools
import os
from os.path import dirname


# -19 for the name of this project StockWebApplication
save_path = dirname(__file__)[ : -19]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'StockWebApplication', 'user_text=')
