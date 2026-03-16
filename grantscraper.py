import pandas as pd
from tqdm import tqdm
from scanar_utils import get_fulltext
from gnews import GNews
import time

path=r"C:\Users\c1049033\Documents\ScanDatasets\formatted\womans_health_funding.csv"

def get_link(inp, linktype="gtr"):
    try:
        if linktype=="gtr":
            l="https://gtr.ukri.org/projects?ref="+inp.split("ref=")[1]
            print(l)
            return l
    except:
        print("Error with type {} link: {}".format(linktype, inp))

def scrape_csv(path, linkcol):
    article_scraper = GNews()
    df=pd.read_csv(path).fillna("")
    txts=[]
    for i, row in tqdm(df.iterrows()):
        if i%20==0:
            time.sleep(2)
        lnk=get_link(row[linkcol])
        try:
            txts.append(article_scraper.get_full_article(lnk).text[:25000])
        except:
            txts.append("")
        if i%50 ==0:
            txtdf=pd.DataFrame()
            txtdf["backup"]=txts
            txtdf.to_csv(r"C:\Users\c1049033\PycharmProjects\ncl_medx\data\backup.csv")
    df["Fulltext"]=txts
    df.to_csv(path, index=False)

def postprocess_text(path, textcol):
    prepped=[]
    df=pd.read_csv(path).fillna("")
    for i, row in df.iterrows():
        ft=row[textcol].strip()
        statements=["Abstracts are not currently available in GtR for all funded research. This is normally because the abstract was not required at the time of proposal submission, but may be because it included sensitive information such as personal details."]
        for s in statements:
            ft=ft.replace(s, "").strip()
        if ft.startswith("Abstract\n\nFunding\n\ndetails"):
            #print(ft)
            ft=ft.replace("Abstract\n\nFunding\n\ndetails","").strip()
        ft=ft.replace("\n\n", "\n")
        prepped.append(ft)
    df[textcol]=prepped
    df.to_csv(path)

scrape_csv(path, "GTRProjectUrl")
postprocess_text(path, "Fulltext")

