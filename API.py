import requests
import pandas as pd

response_API = requests.get('https://db.ygoprodeck.com/api/v2/cardinfo.php')

df = pd.DataFrame(response_API)
df.head()