import requests
from bs4 import BeautifulSoup


def get_bs_obj() :
    url = "https://finance.daum.net/domestic/sectors"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup



def get_cospi_uplst() :  
    # 코스피 등락률 상/하위의 테이블 소스코드가 출력되면 좋겠습니다.
    soup = get_bs_obj()
    table_b = soup.find("div",{"class":"tableB half mr"})
    
    
    return {"tableB_half_mr":table_b}

    
    

csp_up = get_cospi_uplst()
print(csp_up)
