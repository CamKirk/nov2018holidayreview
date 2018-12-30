import requests
import pandas as pd

def calc_stats(json):
    df = pd.DataFrame(json)
    
    reli_mode = df["religion"].mode()
    agree_mean = df["agreeableness"].mean()
    neuro_range = df["neuroticism"].max()- df["neuroticism"].min()
    
    return [reli_mode, agree_mean, neuro_range]

def randsample():
    """
        makes a request to the pplapi, calculates mode, mean, and range of some of
        the response information.
    """
    
    res=requests.get("http://pplapi.com/batch/5/country/us/sample.json")
    resjson = res.json()
    
    if res.status_code != 200:
        raise requests.exceptions.HTTPError("too many requests too fast!")
        
    stats = calc_stats(resjson)
    
    return [stats,resjson]

