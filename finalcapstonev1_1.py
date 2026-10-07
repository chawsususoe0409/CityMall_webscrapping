import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib.parse
import pandas as pd
from datetime import datetime

#create BSoup4 object
def create_webdata(webURL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(webURL, headers=headers)
    #print(response)
    statuscode = response.status_code
    #print (statuscode)

    if statuscode == 200:
        webdata = response.text
        #print(webdata)
    bfobj = BeautifulSoup (webdata,"html.parser")
    #print(bfobj)
    return bfobj

#create page list
def create_pageURLlist(webURL):
    mainbfobj = create_webdata(webURL)
    pagecount = 7
    pageURL_list = []
    for pagenum in range(0,pagecount+1):
        pageURL = webURL + "?q=%3Arelevance&page=" + str(pagenum) + "#"
        pageURL_list.append(pageURL)
    return pageURL_list

#extract product
def extract_productname(pd_taglist):
    pdnametag = pd_taglist.find("a",class_="name")
    pdname = pdnametag.text.replace("\n","").replace("							","")
    return pdname
   

#extract price
def extract_productprice(pd_taglist):
    #catch if price not display 
    try:
        pdpricetag = pd_taglist.find("span", class_="product-sale-price") #check promotion price tag data
        if pdpricetag == None:
            pdpricetag = pd_taglist.find("p",class_="product-price mt-1") #check normal price tag data
        #pdprice = (float)(pdpricetag.text)    
        pdprice = float(pdpricetag.text.replace(",","").replace("Ks",""))
        #print(pdprice)
        return pdprice

    except:
      return "Price may not Specified"

#extract Seller
def extract_productseller(pd_taglist):
    #catch product seller data may not exist
    try:
        pdsellertag = pd_taglist.find("p",class_="product-seller")
        pdseller = pdsellertag.text
        return pdseller
    except:
        return "Seller not display"
    
#extract URL link
def extract_productlink(pd_taglist):
    pdlink = pd_taglist.find("a",class_="name")
    pdurl = pdlink.get("href")
    decodeurl = urllib.parse.unquote(pdurl)
    mainurl = "https://www.citymall.com.mm"
    fullurl = mainurl + decodeurl
    #print(fullurl)
    return fullurl

#extract exportexcel
def exportexcel(namelist, pricelist, sellerlist, URLlist):
    #catch opening file or something exported issue
    try:
        dframe = pd.DataFrame({ "Product Name":namelist,
                            "Product Price":pricelist,
                            "Seller":sellerlist,
                            "Product URL":URLlist})
        
    #datetime add in file name
        extracttime = datetime.now()
        extracttime = extracttime.strftime("%Y-%m-%d %H-%M-%S")

        dframe.to_excel("CMProduct_Computeraccessories_update.xlsx")
        dframe.to_excel(f"CMtimelyproduct {extracttime}.xlsx",index =False)
        
        print("Product information was successful exported")
        return None

    except Exception as e:
        print(f"Export Error: {e}")
 

##################################### Main ############################################################################################
def main():
    #Citiy Mall web URL
    citym_url = "https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/Computer-Components-%26-Accessories/c/id05011003"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    #Create webpage list
    pagelist = create_pageURLlist(citym_url)


    productnamelist = []
    productpricelist = []
    productsellerlist = []
    productURLlist = []  
      
    for pages in tqdm(pagelist):
        #create pageBS4 from web page
        pages_bfobj = create_webdata(pages)
        #extract product tag use with Find method
        pdtag = pages_bfobj.find_all("div",class_="product-info")     

    #extract all data from product tag
        for pdlist in pdtag:
        
            #extract product name
            productname = extract_productname(pdlist)
            productnamelist.append(productname)
                    
            #extract price
            price = extract_productprice(pdlist)
            productpricelist.append(price)
            
            #extract Seller
            seller = extract_productseller(pdlist)
            productsellerlist.append(seller)
            
            #extract URL link
            URLlink = extract_productlink(pdlist)
            productURLlist.append(URLlink )
            
    #export excel 
    exportexcel(namelist=productnamelist, 
                pricelist = productpricelist,
                sellerlist = productsellerlist ,
                URLlist = productURLlist )
            

if __name__ == "__main__":
    main()







    




