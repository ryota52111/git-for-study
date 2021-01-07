# BeautifulSoup4を使用したスクレイピング
import requests, bs4

# ファンド情報クラス
class FundInfo:
    def __init__(self):
        self.name = ''
        self.company = ''
        self.category = ''
        self.baseprice = ''
        self.assets = 0
        self.allotment = 0
        self.commision = ''
        self.cost = 0

# 楽天証券
def GetRakutenFund(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    fundinfo = FundInfo()
    # ファンド名、分類
    fundinfo.name = soup.select_one('.fund-name').text
    fundinfo.company = '楽天'
    fundinfo.category = soup.select_one('.fund-type').text
    # 基準価額、純資産、直近分配金
    fundsummary = soup.find("table", attrs={"class", "tbl-fund-summary"})
    elemnt = fundsummary.select_one('.value-01')
    fundinfo.baseprice = elemnt.text + elemnt.nextSibling
    elements = fundsummary.find_all("span", attrs={"class", "value-02"})
    fundinfo.assets = elements[0].text
    fundinfo.allotment = elements[1].text
    # 買付手数料、信託報酬等の管理費
    fundinfo.commision = soup.select_one('.no-fee').text
    costs = soup.find("li", attrs={"class", "trust-fee"})
    elements = costs.find_all("td")
    fundinfo.cost = elements[0].text

    return fundinfo