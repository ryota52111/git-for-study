import fund, exceloperator

# メイン関数
# ＜購入・換金手数料なし＞ニッセイＴＯＰＩＸインデックスファンド
nam = fund.GetRakutenFund('https://www.rakuten-sec.co.jp/web/fund/detail/?ID=JP90C000BRT6')
# たわらノーロード　先進国株式
am_one = fund.GetRakutenFund('https://www.rakuten-sec.co.jp/web/fund/detail/?ID=JP90C000CMK4')
# ｅＭＡＸＩＳSlim 新興国株式インデックス
emax_emarging = fund.GetRakutenFund('https://www.rakuten-sec.co.jp/web/fund/detail/?ID=JP90C000F7H5')
# ｅＭＡＸＩＳ Ｓｌｉｍ 米国株式（Ｓ＆Ｐ５００）
emax_sp500 = fund.GetRakutenFund('https://www.rakuten-sec.co.jp/web/fund/detail/?ID=JP90C000GKC6')

# EXCELへ書き込み
fund_info_list = [nam, am_one, emax_emarging, emax_sp500]
exceloperator.WriteExcel(fund_info_list)