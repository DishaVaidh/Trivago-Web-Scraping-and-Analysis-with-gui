def function(city,sd_str,st,ac):

    from datetime import datetime,date,timedelta
    import time
    import datetime
    import pandas as pd
    import numpy as np
    import os
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException  

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    
    if not os.path.exists("C:\\trivago_data"):
        os.makedirs("C:\\trivago_data")
    start_url = "https://www.trivago.in/"
    try:
        driver.get(start_url)
    except:
        time.sleep(1)
        driver.get(start_url)

    time.sleep(0.5)

    #city=input("Enter location")
    #city="jaipur"
    E1 = ""
    try:
        E1 = driver.find_element_by_xpath("//input[@type='search']").send_keys(city,Keys.ENTER)
    except:
        E1 = driver.find_element_by_xpath("//input[@type='search']").send_keys(city,Keys.ENTER)
    a = ActionChains(driver)
    """cross=driver.find_element_by_xpath("//button[@class='df_overlay_close_wrap overlay__close']")
    a.click(cross).perform()"""
    time.sleep(3)

    a = ActionChains(driver)
    search = ""
    try:
        search = driver.find_element_by_xpath("//button[@class='btn btn--primary btn--regular search-button js-search-button']")
    except:
        search = driver.find_element_by_xpath("//button[@class='btn btn--primary btn--regular search-button js-search-button']")
    a.click(search).perform()
    time.sleep(1)

    curr_url=driver.current_url
    #sd_str = input("Enter checkin date in YYYY-MM-DD format")
    #ed_str=input("Enter checkout date in YYYY-MM-DD format")


    sd=datetime.datetime.strptime(sd_str, '%Y-%m-%d').date()
    ed=sd+timedelta(1)
    #ed=datetime.datetime.strptime(ed_str, '%Y-%m-%d').date()

    #days=(ed-sd).days

    curr_url=curr_url.replace(curr_url[44:54],str(sd),1)
    curr_url=curr_url.replace(curr_url[75:85],str(ed),1)

    try:
        driver.get(curr_url)
    except:
        time.sleep(3)
        driver.get(curr_url)
    a = ActionChains(driver)
    filters = ""
    try:
        filters = driver.find_element_by_xpath("//li[@class='toolbar-list__item toolbar-list__item--more js-toolbar__item--more js-toolbar-more']")
    except:
        filters = driver.find_element_by_xpath("//li[@class='toolbar-list__item toolbar-list__item--more js-toolbar__item--more js-toolbar-more']")
    a.move_to_element(filters).perform()

    a = ActionChains(driver)
    #st=int(input("Enter stars"))
    stars = ""
    try:
        if(st==1):
            stars=driver.find_element_by_xpath("//button[@title='1-star hotels']")
            a.click(stars).perform()
        elif(st==2):
            stars=driver.find_element_by_xpath("//button[@title='2-star hotels']")
            a.click(stars).perform()
        elif(st==3):
            stars=driver.find_element_by_xpath("//button[@title='3-star hotels']")
            a.click(stars).perform()
        elif(st==4):
            stars=driver.find_element_by_xpath("//button[@title='4-star hotels']")
            a.click(stars).perform()
        elif(st==5):
            stars=driver.find_element_by_xpath("//button[@title='5-star hotels']")
            a.click(stars).perform()
        else:
            print("Not available")
    except:
        if(st==1):
            stars=driver.find_element_by_xpath("//button[@title='1-star hotels']")
            a.click(stars).perform()
        elif(st==2):
            stars=driver.find_element_by_xpath("//button[@title='2-star hotels']")
            a.click(stars).perform()
        elif(st==3):
            stars=driver.find_element_by_xpath("//button[@title='3-star hotels']")
            a.click(stars).perform()
        elif(st==4):
            stars=driver.find_element_by_xpath("//button[@title='4-star hotels']")
            a.click(stars).perform()
        elif(st==5):
            stars=driver.find_element_by_xpath("//button[@title='5-star hotels']")
            a.click(stars).perform()
        else:
            st=0
            print("Not available")
    time.sleep(4)

    a = ActionChains(driver)
    #ac=int(input("Enter 1 if you want ac"))
    AC = ""

    try:
        if(ac==1):
            AC = ""
            try:
                AC=driver.find_element_by_xpath("//input[@id='86/300-5']")
            except:
                try:
                    AC = driver.find_element_by_xpath("//input[@id='86/300-6']")
                except:
                    try:
                        AC = driver.find_element_by_xpath("//input[@id='86/300-7']")
                    except:
                        try:
                            AC = driver.find_element_by_xpath("//input[@id='86/300-4']")
                        except:
                            try:
                                AC = driver.find_element_by_xpath("//input[@id='86/300-3']")
                            except:
                                try:
                                    AC = driver.find_element_by_xpath("//input[@id='86/300-8']")
                                except:
                                    try:
                                        AC = driver.find_element_by_xpath("//input[@id='86/300-9']")
                                    except:
                                        try:
                                            AC = driver.find_element_by_xpath("//input[@id='86/300-10']")
                                        except:
                                            try:
                                                AC = driver.find_element_by_xpath("//input[@id='86/300-1']")
                                            except:
                                                try:
                                                    AC = driver.find_element_by_xpath("//input[@id='86/300-2']")
                                                except:
                                                    try:
                                                        AC = driver.find_element_by_xpath("//input[@id='86/300-11']")
                                                    except:
                                                        try:
                                                            AC = driver.find_element_by_xpath("//input[@id='86/300-12']")
                                                        except:
                                                            try:
                                                                AC = driver.find_element_by_xpath("//input[@id='86/300-13']")
                                                            except:
                                                                try:
                                                                    AC = driver.find_element_by_xpath("//input[@id='86/300-14']")
                                                                except:
                                                                    AC = driver.find_element_by_xpath("//input[@id='86/300-15']")
                                        
            a.click(AC).perform()
            a = ActionChains(driver)
            try:
                done=driver.find_element_by_xpath("//button[@id='filter-popover-done-button']")  
                a.click(done).perform() 
            except:
                pass
    except:
        if(ac==1):
            AC=driver.find_element_by_xpath("//input[@id='86/300-5']")
            a.click(AC).perform()
            a = ActionChains(driver)
            try:
                done=driver.find_element_by_xpath("//button[@id='filter-popover-done-button']")  
                a.click(done).perform() 
            except:
                pass

    Hotel_Name=[]
    Distance=[]
    Distance_in_km=[]
    Rate=[]
    checkin=[]
    checkout=[]
    booking_site=[]

    #url = "https://www.trivago.in/?aDateRange%5Barr%5D="+str(sd)+"&aDateRange%5Bdep%5D="+str(ed)+"&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=64989%2F200%2C2%2F101&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode=roomsDropdown"
    url=driver.current_url

    def rreplace(s, old, new):
        return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    for i in range(365-((sd-datetime.date.today()).days)):
        n=True
        first_page_url=url
        while(n==True):
            try:
                driver.get(url)
            except:
                time.sleep(1)
                driver.get(url)
            time.sleep(1)
            '''hotels = driver.find_elements_by_xpath("//span[@class='item-link name__copytext']")
            distances=driver.find_elements_by_xpath("//div[@class='item-link']")
            rates=driver.find_elements_by_xpath("//strong[@class='accommodation-list__price--3230a']")'''
            hotels = ""
            distances = ""
            rates = ""
            booking_sites = ""
            try:
                hotels = driver.find_elements_by_xpath("//span[@data-qa='item-name']")
                distances=driver.find_elements_by_xpath("//div[@class='item-link']")
                rates=driver.find_elements_by_xpath("//strong[@data-qa='recommended-price']")
                booking_sites=driver.find_elements_by_xpath("//span[@data-qa='recommended-price-partner']")
            except:
                driver.get(url)
                time.sleep(1)
                hotels = driver.find_elements_by_xpath("//span[@data-qa='item-name']")
                distances=driver.find_elements_by_xpath("//div[@class='item-link']")
                rates=driver.find_elements_by_xpath("//strong[@data-qa='recommended-price']")
                booking_sites=driver.find_elements_by_xpath("//span[@data-qa='recommended-price-partner']")
            p,q,r,s=len(hotels),len(distances),len(rates),len(booking_sites)
            set1={p,q,r,s}
            if len(set1)!=1 or set1=={0} or p<7:
                driver.get(url)
                time.sleep(3.5)
                hotels = driver.find_elements_by_xpath("//span[@data-qa='item-name']")
                distances=driver.find_elements_by_xpath("//div[@class='item-link']")
                rates=driver.find_elements_by_xpath("//strong[@data-qa='recommended-price']")
                booking_sites=driver.find_elements_by_xpath("//span[@data-qa='recommended-price-partner']")

                
            print(len(hotels),len(distances),len(rates),len(booking_sites), sd)

            for i,j,k,l in zip(hotels,distances,rates,booking_sites):
                #print("Hotel:"+ i.text,"\tDistance:"+j.text,"\tRate:"+k.text)
                try:
                    Hotel_Name.append(i.text)
                except:
                    Hotel_Name.append(np.nan)

                try:
                    Distance.append(j.text)
                except:
                    Distance.append(np.nan)

                try:
                    x=j.text.split()
                    Distance_in_km.append(float(x[0]))
                except:
                    Distance_in_km.append(0.0)

                try:
                    Rate.append(int(k.text.replace(",","")[1:]))
                except:
                    Rate.append(0)

                try:
                    booking_site.append(l.text)
                except:
                    booking_site.append(np.nan)

                checkin.append(sd)
                checkout.append(ed)

            a = ActionChains(driver)
            n = ""
            try:
                n=check_exists_by_xpath("//button[@class='btn btn--pagination btn--small btn--page-arrow btn--next']")
                if(n==True):
                    next1=driver.find_element_by_xpath("//button[@class='btn btn--pagination btn--small btn--page-arrow btn--next']")
                    a.click(next1).perform()
                    url=driver.current_url
                else:
                    url=first_page_url
            except:
                n=check_exists_by_xpath("//button[@class='btn btn--pagination btn--small btn--page-arrow btn--next']")
                if(n==True):
                    next1=driver.find_element_by_xpath("//button[@class='btn btn--pagination btn--small btn--page-arrow btn--next']")
                    a.click(next1).perform()
                    url=driver.current_url
                else:
                    url=first_page_url

        sd=ed
        #ed=ed+timedelta(days)
        ed=ed+timedelta(1)
        #url=driver.current_url
        url=url.replace(url[44:54],str(sd),1)
        url=rreplace(url, url[75:85], str(ed))
    print("\n\nScraping Completed...\nSaving to file...\n")
    df=pd.DataFrame({"Hotel_Name":Hotel_Name,"Distance_from_city_centre":Distance_in_km,"Rate":Rate,"checkin":checkin,"checkout":checkout,"booking_site":booking_site}) 
    #print(df.info())
    df=df.dropna().reset_index()
    print(st,type(st))
    print(str(st),type(str(st)))
    df.to_csv("C:\\trivago_data\\"+city+str(st)+"star"+".csv")
    #df.to_csv(city+".csv")

    #print("File saved at location : "+city+".csv")
    print("File saved at location : C:\\trivago_data\\"+city+str(st)+"star"+".csv")
