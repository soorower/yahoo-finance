import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding" :"gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "APID=UP18c9e674-b273-11eb-8a07-06f3135cb947; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiVFo1NEZBMzY3TVFVTkJUNUFGV1Q2UU1XQUEiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJyV3JSTXRIOVNhYlMifX0.rIdAFL3eBa8hVv9oOJt88IMyVhKyQo9io2vMl6fR-V5rIA7xuE5Cqs1vldxPyGP-09aDnLhxUxFCjNZh4x531AbMZZ3hcwCdfIvEHAVGp9P6jxh2MCJrHBde_lfgLqXUsFDzPfQNXAhOs8cxSajL8TSnRG2iN52V99PvJxXk9kQ; T=af=JnRzPTE2MjA4OTY2MjImcHM9a0pXcjlyRTJQemk1eDZUUGVxdGRoUS0t&d=bnMBeWFob28BZwFUWjU0RkEzNjdNUVVOQlQ1QUZXVDZRTVdBQQFhYwFBSlRVT3N4VwFhbAFiYW5nbGFib2tib2s0MjBAZ21haWwuY29tAXNjAW1icl9yZWdpc3RyYXRpb24BZnMBTEtHUVl0WmduT3R1AXp6AXV0T25nQkE3RQFhAVFBRQFsYXQBdXRPbmdCAW51ATA-&sk=DAAyd67GsMG5zw&ks=EAAC2rh85fz20wZ6YR2V8Fv.w--~G&kt=EAAlyLEcdMyg2P_uNXy64wv4w--~I&ku=FAAu460.eM4iyAAuGd_dVCNs5GHPbiDuuEeIcBke_7s0Cdkx340tc6DcI8cNUUxYcVPjfuU6am16Z2D0XiwBuFo3qCIvnS67f1rf2VXGM0cdk4aB2fr6Bwvfx6AQeuYBOniKCwT55wEayD8U1YPoV2UtF.mRl3BYFErkLEV_kYl7wY-~D; F=d=mruvCOo9vKLBPPAxL1BM10PJKuxIzYUxeSxFmq2VWMI1fSudTMrDpW16_Pk.; PH=fn=ACVo.qgZgTvcdA--&l=en-US; Y=v=1&n=13kku963h6o0d&l=43aws19nx1aev4acvxv8x4ukvbenkodnxh8o45v2/o&p=n34vvbd00000000&r=18h&intl=us; A1=d=AQABBKpxkmACELUCnen7-O4mNVnip0PRZigFEgEABAI3nmB5YdxXxyMA_eMAAAcIqnGSYEPRZigIDzYg5FLW_g5hdyye64FSZwkBBwoBLg&S=AQAAAr8FGftd9qd2SgIcRzPJ-Ok; A3=d=AQABBKpxkmACELUCnen7-O4mNVnip0PRZigFEgEABAI3nmB5YdxXxyMA_eMAAAcIqnGSYEPRZigIDzYg5FLW_g5hdyye64FSZwkBBwoBLg&S=AQAAAr8FGftd9qd2SgIcRzPJ-Ok; B=2gpmh8dg94sda&b=4&d=B239rExtYFlEzrllOdgW&s=ot&i=NiDkUtb.DmF3LJ7rgVJn; GUC=AQEABAJgnjdheUIfegSH; PRF=t%3DMSFT%252BAMGO.L%252BBRCK.L%252BALM.L%252BGSEO.L%252BAEWU.L%252BESKN.L%252BASIT.L%252BAAPL%252BAGD.AX%252BSQ%252B14D.AX%252BAGX1.AX%252BAFT.AX%252BACQ.AX; A1S=d=AQABBKpxkmACELUCnen7-O4mNVnip0PRZigFEgEABAI3nmB5YdxXxyMA_eMAAAcIqnGSYEPRZigIDzYg5FLW_g5hdyye64FSZwkBBwoBLg&S=AQAAAr8FGftd9qd2SgIcRzPJ-Ok&j=WORLD; APIDTS=1621047388; cmp=t=1621058175&j=0&v=18",
    "sec-ch-ua": "Not A;Brand;v='99', 'Chromium';v='90', 'Google Chrome';v='90'",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}


def scrape_whole():
    starts = []
    ends = []
    lenth = len(pd.read_csv('Symbols.csv')['Symbol'].tolist())
    def scrape_first_500():
        start = 0
        starts.append(start)
        end = 500
        ends.append(end)

    def scrape_next_500():
        start = 500
        starts.append(start)
        end = 1001
        ends.append(end)

    def scrape_all():
        start = 0
        starts.append(start)
        end = lenth
        ends.append(end)

    def let_me_pick():
        start = int(input('start from: '))-1
        starts.append(start)
        end = int(input('end at: '))
        ends.append(end)

    def submenu():
        print('\n')
        print('1. scrape first 500 symbols')
        print(f'2. scrape next 500 symbols')
        print(f'3. scrape for all symbols')
        print('4. Let me select, manually...')
        selection = int(input('Enter Choice: '))
        if selection == 1:
            scrape_first_500()
        elif selection == 2:
            scrape_next_500()
        elif selection == 3:
            scrape_all()
        elif selection == 4:
            let_me_pick()
        else:
            print("Invalid Choice. Inter 1-4")
            submenu()

    submenu()
    symbols = pd.read_csv('Symbols.csv')['Symbol'].tolist()[int(f'{starts[-1]}'):int(f'{ends[-1]}')]

    lists = []
    data = {}
    counter = 1
    print("Collecting data from API's")
    for symbol in symbols:
        print(counter)
        counter = counter + 1
        symbol1 = symbol.replace('.','').replace(',','').replace('?','')
        symbol = symbol1[:-1]+'.'+symbol1[-1:]
        CMP = symbol
        print(CMP)
        url3 = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"+ CMP + "?lang=en-GB&region=GB&symbol="+ CMP + "&padTimeSeries=true&type=trailingTotalRevenue%2CtrailingCostOfRevenue%2CtrailingGrossProfit%2CtrailingResearchAndDevelopment%2CtrailingSellingGeneralAndAdministration%2CtrailingOperatingExpense%2CtrailingOperatingIncome%2CtrailingInterestExpense%2CtrailingOtherIncomeExpense%2CtrailingTaxProvision%2CtrailingNetIncomeContinuousOperations%2CtrailingNetIncome&merge=false&period1=493590046&period2=1621080893&corsDomain=uk.finance.yahoo.com"
        url4 = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"+ CMP + "?lang=en-GB&region=GB&symbol="+ CMP + "&padTimeSeries=true&type=quarterlyStockholdersEquity%2CtrailingStockholdersEquity%2CquarterlyTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CquarterlyTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CquarterlyCurrentLiabilities%2CquarterlyCurrentAssets%2CtrailingCurrentAssets%2CquarterlyOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CquarterlyInventory%2CtrailingInventory%2CquarterlyAccountsReceivable%2CtrailingAccountsReceivable%2CquarterlyCashCashEquivalentsAndShortTermInvestments%2CtrailingCashCashEquivalentsAndShortTermInvestments%2CquarterlyOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CquarterlyCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1620929816&corsDomain=uk.finance.yahoo.com"
        url5 = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"+ CMP + "?lang=en-GB&region=GB&symbol="+ CMP + "&padTimeSeries=true&type=quarterlyFreeCashFlow%2CtrailingFreeCashFlow%2CquarterlyCashDividendsPaid%2CtrailingCashDividendsPaid&merge=false&period1=493590046&period2=1620990246&corsDomain=uk.finance.yahoo.com"
        try:   
            page3 = requests.get(url3, headers=headers)
            m = json.loads(page3.content)

            with open('yahoo_finance.json', 'w') as outfile:
                json.dump(m, outfile)
            with open('yahoo_finance.json','r') as file:
                data = json.load(file)
        #         try:
            balance_json = data.get('timeseries').get('result')
            for ba_json in balance_json:
                if 'trailingNetIncome' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        net_income = int(str(ba_json.get('trailingNetIncome')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        net_income = '-'
                if 'trailingTotalRevenue' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        total_rev = int(str(ba_json.get('trailingTotalRevenue')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        total_rev = '-'
                if 'trailingCostOfRevenue' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        cost_rev = int(str(ba_json.get('trailingCostOfRevenue')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        cost_rev = '-'

                if 'trailingGrossProfit' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        gross_prof = int(str(ba_json.get('trailingGrossProfit')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        gross_prof = '-'
                if 'trailingResearchAndDevelopment' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        research_dev = int(str(ba_json.get('trailingResearchAndDevelopment')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        research_dev = '-'
                if 'trailingSellingGeneralAndAdministration' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        selling_gen_admin = int(str(ba_json.get('trailingSellingGeneralAndAdministration')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        selling_gen_admin = '-'
                if 'trailingOperatingExpense' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        total_operate_expense = int(str(ba_json.get('trailingOperatingExpense')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        total_operate_expense = '-'
                if 'trailingOperatingIncome' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        operate_income_loss = int(str(ba_json.get('trailingOperatingIncome')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        operate_income_loss = '-'
                if 'trailingInterestExpense' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        interest_expense = int(str(ba_json.get('trailingInterestExpense')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        interest_expense = '-'
                if 'trailingOtherIncomeExpense' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        total_other_income_ex = int(str(ba_json.get('trailingOtherIncomeExpense')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        total_other_income_ex = '-'
                if 'trailingTaxProvision' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        income_tax_ex = int(str(ba_json.get('trailingTaxProvision')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        income_tax_ex = '-'
                if 'trailingNetIncomeContinuousOperations' in str(ba_json.get('meta').get('type')[0]):
                    try:
                        income_continuing_operation = int(str(ba_json.get('trailingNetIncomeContinuousOperations')[-1].get('reportedValue').get('raw'))[:-2])
                    except:
                        income_continuing_operation = '-'

            # print(net_income)
            page4 = requests.get(url4, headers=headers)
            m = json.loads(page4.content)

            with open('yahoo_finance.json', 'w') as outfile:
                json.dump(m, outfile)
            with open('yahoo_finance.json','r') as file:
                data = json.load(file)
            try:
                balance_json = data.get('timeseries').get('result')
                for ba_json in balance_json:
                    if 'quarterlyCashAndCashEquivalents' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            cash_cash_equiv = int(str(ba_json.get('quarterlyCashAndCashEquivalents')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            cash_cash_equiv = '-'
                    if 'quarterlyOtherShortTermInvestments' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            other_short_invest = int(str(ba_json.get('quarterlyOtherShortTermInvestments')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            other_short_invest = '-'

                    if 'quarterlyCashCashEquivalentsAndShortTermInvestments' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_cashs = int(str(ba_json.get('quarterlyCashCashEquivalentsAndShortTermInvestments')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_cashs = '-'
                    if 'quarterlyAccountsReceivable' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            net_receivables = int(str(ba_json.get('quarterlyAccountsReceivable')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            net_receivables = '-'
                    if 'quarterlyInventory' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            inventory = int(str(ba_json.get('quarterlyInventory')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            inventory = '-'
                    if 'quarterlyOtherCurrentAssets' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            other_current_asset = int(str(ba_json.get('quarterlyOtherCurrentAssets')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            other_current_asset = '-'
                    if 'quarterlyCurrentAssets' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_current_asset = int(str(ba_json.get('quarterlyCurrentAssets')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_current_asset = '-'
                    if 'quarterlyCurrentLiabilities' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_current_liability = int(str(ba_json.get('quarterlyCurrentLiabilities')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_current_liability = '-'
                    if 'quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_non_current_liability = int(str(ba_json.get('quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_non_current_liability = '-'
                    if 'quarterlyTotalLiabilitiesNetMinorityInterest' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_liability = int(str(ba_json.get('quarterlyTotalLiabilitiesNetMinorityInterest')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_liability = '-'
                    if 'quarterlyStockholdersEquity' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            total_stockholders = int(str(ba_json.get('quarterlyStockholdersEquity')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            total_stockholders = '-'

            except:
                cash_cash_equiv = '-'
                other_short_invest = '-'
                total_cashs = '-'
                net_receivables = '-'
                inventory = '-'
                other_current_asset = '-'
                total_current_asset = '-'
                total_current_liability = '-'
                total_non_current_liability = '-'
                total_liability = '-'
                total_stockholders = '-'

            page5 = requests.get(url5, headers=headers)
            k = json.loads(page5.content)

            with open('yahoo_finance.json', 'w') as outfile:
                json.dump(k, outfile)
            with open('yahoo_finance.json','r') as file:
                data5 = json.load(file)
            try:
                balance_json5 = data5.get('timeseries').get('result')
                for ba_json in balance_json5:
                    if 'trailingCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid1 = int(str(ba_json.get('trailingCashDividendsPaid')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid1 = '-'
                    if 'trailingFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow1 = int(str(ba_json.get('trailingFreeCashFlow')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow1 = '-'
                    if 'quarterlyCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid2 = int(str(ba_json.get('quarterlyCashDividendsPaid')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid2 = '-'
                    if 'quarterlyCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid3 = int(str(ba_json.get('quarterlyCashDividendsPaid')[-2].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid3 = '-'
                    if 'quarterlyCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid4 = int(str(ba_json.get('quarterlyCashDividendsPaid')[-3].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid4 = '-'
                    if 'quarterlyCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid5 = int(str(ba_json.get('quarterlyCashDividendsPaid')[-4].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid5 = '-'
                    if 'quarterlyCashDividendsPaid' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            dividends_paid6 = int(str(ba_json.get('quarterlyCashDividendsPaid')[-5].get('reportedValue').get('raw'))[:-2])
                        except:
                            dividends_paid6 = '-'
                    if 'quarterlyFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow2 = int(str(ba_json.get('quarterlyFreeCashFlow')[-1].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow2 = '-'
                    if 'quarterlyFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow3 = int(str(ba_json.get('quarterlyFreeCashFlow')[-2].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow3 = '-'
                    if 'quarterlyFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow4 = int(str(ba_json.get('quarterlyFreeCashFlow')[-3].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow4 = '-'
                    if 'quarterlyFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow5 = int(str(ba_json.get('quarterlyFreeCashFlow')[-4].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow5 = '-'
                    if 'quarterlyFreeCashFlow' in str(ba_json.get('meta').get('type')[0]):
                        try:
                            free_cash_flow6 = int(str(ba_json.get('quarterlyFreeCashFlow')[-5].get('reportedValue').get('raw'))[:-2])
                        except:
                            free_cash_flow6 = '-'
            except:
                dividends_paid1 = '-'
                dividends_paid2 = '-'
                dividends_paid3 = '-'
                dividends_paid4 = '-'
                dividends_paid5 = '-'
                dividends_paid6 = '-'
                free_cash_flow1 = '-'
                free_cash_flow2 = '-'
                free_cash_flow3 = '-'
                free_cash_flow4 = '-'
                free_cash_flow5 = '-'
                free_cash_flow6 = '-'
        except:
            print('sleeping to avoid block')
            total_rev = '-'
            cost_rev = '-'
            gross_prof = '-'
            research_dev = '-'
            selling_gen_admin = '-'
            total_operate_expense = '-'
            operate_income_loss = '-'
            interest_expense = '-'
            total_other_income_ex = '-'
            income_tax_ex = '-'
            income_continuing_operation = '-'
            net_income = '-'
            cash_cash_equiv = '-'
            other_short_invest = '-'
            total_cashs = '-'
            net_receivables = '-'
            inventory = '-'
            other_current_asset = '-'
            total_current_asset = '-'
            total_current_liability = '-'
            total_non_current_liability = '-'
            total_liability = '-'
            total_stockholders = '-'
            dividends_paid1 = '-'
            dividends_paid2 = '-'
            dividends_paid3 = '-'
            dividends_paid4 = '-'
            dividends_paid5 = '-'
            dividends_paid6 = '-'
            free_cash_flow1 = '-'
            free_cash_flow2 = '-'
            free_cash_flow3 = '-'
            free_cash_flow4 = '-'
            free_cash_flow5 = '-'
            free_cash_flow6 = '-'
            sleep(100)
        data = {
            
            'Total Revenue': total_rev,
            'Cost Per Revenue': cost_rev,
            'Gross Profit': gross_prof,
            'Research Development': research_dev,
            'Selling general and administrative': selling_gen_admin,
            'Total operating expenses': total_operate_expense,
            'Operating income or loss': operate_income_loss,
            'Interest expense': interest_expense,
            'Total other income/expenses net': total_other_income_ex,
            'Income tax expense': income_tax_ex,
            'Income from continuing operations':income_continuing_operation,
            'Net Income': net_income,
            'Cash and Cash Equivalents': cash_cash_equiv,
            'Other short-term investments': other_short_invest,
            'Total Cash': total_cashs,
            'Net Recievables': net_receivables,
            'Inventory': inventory,
            'Other Current Assets': other_current_asset,
            'Total Current Assets': total_current_asset,
            'Total Current Liabilities': total_current_liability,
            'Total non-current liabilities': total_non_current_liability,
            'Total liabilities': total_liability,
            'Total stockholders equity': total_stockholders,
            'Dividend Paid 1': dividends_paid1,
            'Dividend Paid 2': dividends_paid2,
            'Dividend Paid 3': dividends_paid3,
            'Dividend Paid 4': dividends_paid4,
            'Dividend Paid 5': dividends_paid5,
            'Dividend Paid 6': dividends_paid6,
            'Free Cash Flow 1': free_cash_flow1,
            'Free Cash Flow 2': free_cash_flow2,
            'Free Cash Flow 3': free_cash_flow3,
            'Free Cash Flow 4': free_cash_flow4,
            'Free Cash Flow 5': free_cash_flow5,
            'Free Cash Flow 6': free_cash_flow6

        }
        lists.append(data)
        
    df1 = pd.DataFrame(lists)
    df = df1.reset_index(drop=True)
    df.to_csv('yf_test.csv',encoding='utf-8', index=False)

    sleep(2)

    apis = pd.read_csv('yf_test.csv')
    total_rev = apis['Total Revenue'].tolist()
    cost_rev = apis['Cost Per Revenue'].tolist()
    gross_prof = apis['Gross Profit'].tolist()
    research_dev = apis['Research Development'].tolist()
    selling_gen_admin = apis['Selling general and administrative'].tolist()
    total_operate_expense = apis['Total operating expenses'].tolist()
    operate_income_loss = apis['Operating income or loss'].tolist()
    interest_expense = apis['Interest expense'].tolist()
    total_other_income_ex = apis['Total other income/expenses net'].tolist()
    income_tax_ex = apis['Income tax expense'].tolist()
    income_continuing_operation = apis['Income from continuing operations'].tolist()

    net_income = apis['Net Income'].tolist()
    cash_cash_equiv = apis['Cash and Cash Equivalents'].tolist()
    other_short_invest= apis['Other short-term investments'].tolist()
    total_cashs = apis['Total Cash'].tolist()
    net_receivables = apis['Net Recievables'].tolist()
    inventory = apis['Inventory'].tolist()
    other_current_asset = apis['Other Current Assets'].tolist()
    total_current_asset = apis['Total Current Assets'].tolist()

    total_current_liability = apis['Total Current Liabilities'].tolist()
    total_non_current_liability = apis['Total non-current liabilities'].tolist()
    total_liability = apis['Total liabilities'].tolist()
    total_stockholders = apis['Total stockholders equity'].tolist()
    dividends_paid1= apis['Dividend Paid 1'].tolist()
    dividends_paid2= apis['Dividend Paid 2'].tolist()
    dividends_paid3= apis['Dividend Paid 3'].tolist()
    dividends_paid4 = apis['Dividend Paid 4'].tolist()
    dividends_paid5= apis['Dividend Paid 5'].tolist()
    dividends_paid6= apis['Dividend Paid 6'].tolist()
    free_cash_flow1 = apis['Free Cash Flow 1'].tolist()
    free_cash_flow2 = apis['Free Cash Flow 2'].tolist()
    free_cash_flow3 = apis['Free Cash Flow 3'].tolist()
    free_cash_flow4 = apis['Free Cash Flow 4'].tolist()
    free_cash_flow5= apis['Free Cash Flow 5'].tolist()
    free_cash_flow6 = apis['Free Cash Flow 6'].tolist()


    print('Collecting Data from Direct links')
    res1 = []
    res2 = []
    for symbol in symbols:
        symbol1 = symbol.replace('.','').replace(',','').replace('?','')
        symbol = symbol1[:-1]+'.'+symbol1[-1:]
        CMP = symbol
        print(CMP)
        try:
            url1 = "https://uk.finance.yahoo.com/quote/" + CMP + "/profile?p=" + CMP
            page1 = requests.get(url1, headers=headers).content
        except:
            page1 = '-'
        res1.append(page1)
        try:
            url2 = "https://uk.finance.yahoo.com/quote/" + CMP + "/key-statistics?p=" + CMP
            page2 = requests.get(url2, headers=headers).content
        except:
            page2 = '-'
        res2.append(page2)

    print('Almost Done!')

    lists = []
    data = {}
    for symbol,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,a2,a3,a4,a5,a6,a7,a8,a9,result1,result2 in zip(symbols,total_rev,cost_rev,gross_prof,research_dev,selling_gen_admin,total_operate_expense,operate_income_loss,interest_expense,total_other_income_ex,income_tax_ex,income_continuing_operation,net_income,cash_cash_equiv,other_short_invest,total_cashs,net_receivables,inventory,other_current_asset,total_current_asset,total_current_liability,total_non_current_liability,total_liability,total_stockholders,dividends_paid1,dividends_paid2,dividends_paid3,dividends_paid4,dividends_paid5,dividends_paid6,free_cash_flow1,free_cash_flow2,free_cash_flow3,free_cash_flow4,free_cash_flow5,free_cash_flow6,res1,res2):
        total_rev = a
        cost_rev = b
        gross_prof = c
        research_dev = d
        selling_gen_admin = e
        total_operate_expense = f
        operate_income_loss = g
        interest_expense = h
        total_other_income_ex = i
        income_tax_ex = j
        income_continuing_operation = k

        net_income = l
        cash_cash_equiv = m
        other_short_invest= n
        total_cashs = o
        net_receivables = p
        inventory = q
        other_current_asset = r
        total_current_asset = s

        total_current_liability = t
        total_non_current_liability = u
        total_liability = v
        total_stockholders =w
        dividends_paid1= x
        dividends_paid2= y
        dividends_paid3=z
        dividends_paid4 = a1
        dividends_paid5= a2
        dividends_paid6= a3
        free_cash_flow1 = a4
        free_cash_flow2 = a5
        free_cash_flow3 = a6
        free_cash_flow4 = a7
        free_cash_flow5= a8
        free_cash_flow6 = a9
        

        symbol1 = symbol.replace('.','').replace(',','').replace('?','')
        CMP = symbol1[:-1]+'.'+symbol1[-1:]
        
        soup1 = BeautifulSoup(result1, 'html.parser')
        try:
            right_side = soup1.find('p',attrs = {'class':'D(ib) Va(t)'}).findAll('span')
            if 'Sector(s)' in right_side[0].text:
                try:
                    sector = right_side[1].text
                except:
                    sector = '-'
            if 'Industry' in right_side[2].text:
                try:
                    industry = right_side[3].text
                except:
                    industry = '-'
            if 'Full-time employees' in right_side[4]:
                try:
                    full_time_employee = right_side[5].find('span').text
                except:
                    full_time_employee = '-'
            websites = soup1.findAll('a',attrs = {'class':'C($linkColor)'})[-1]
            if "http" in websites.text:
                try:
                    website = websites['href']
                except:
                    website = '-'
            sector = sector 
            industry = industry
            full_time_employee = full_time_employee
            website = website
        except:
            sector = '-'
            industry = '-'
            full_time_employee = '-'
            website = '-'
        
        try:
            stats = soup1.findAll('a',attrs = {'role':'tab'})[3].find('span').text
            if 'Statistics' in stats:
                soup2 = BeautifulSoup(result2, 'html.parser')

                alldata2 = soup2.find_all("tbody")
                table1 = alldata2[0].find_all("tr")
                table2 = alldata2[1].find_all("tr")
                table3 = alldata2[2].find_all("tr")
                table4 = alldata2[3].find_all("tr")
                table5 = alldata2[4].find_all("tr")
                table6 = alldata2[5].find_all("tr")
                table7 = alldata2[6].find_all("tr")
                table8 = alldata2[7].find_all("tr")
                table9 = alldata2[8].find_all("tr")
                table10= alldata2[9].find_all("tr")

                #------------------Valuation Measures------------------------------------------------------------------   
                market_cap_intraday = table1[0].find_all("td")[1].text.replace('N/A','-')
                enterprise_val = table1[1].find_all("td")[1].text.replace('N/A','-')
                trailing_pe = table1[2].find_all("td")[1].text.replace('N/A','-')
                forward_pe = table1[3].find_all("td")[1].text.replace('N/A','-')
                peg_ratio_5y = table1[4].find_all("td")[1].text.replace('N/A','-')
                price_sales = table1[5].find_all("td")[1].text.replace('N/A','-')
                price_book = table1[6].find_all("td")[1].text.replace('N/A','-')
                enterprise_val_rev = table1[7].find_all("td")[1].text.replace('N/A','-')
                enterprise_val_ebit = table1[8].find_all("td")[1].text.replace('N/A','-')

                #-----------------Stock Price History-------------------------------------------------------------------
                beta_5y_mon = table2[0].find_all("td")[1].text.replace('N/A','-')
                f_two_week_change = table2[1].find_all("td")[1].text.replace('N/A','-')
                sp500_52_week_change = table2[2].find_all("td")[1].text.replace('N/A','-')
                f_two_week_high = table2[3].find_all("td")[1].text.replace('N/A','-')
                f_two_week_low = table2[4].find_all("td")[1].text.replace('N/A','-')
                f_day_moving_avg = table2[5].find_all("td")[1].text.replace('N/A','-')
                t_hundred_day_moving_avg = table2[6].find_all("td")[1].text.replace('N/A','-')

                #------------------Share Statistics---------------------------------------------------------------------   
                avg_vol_3_mon = table3[0].find_all("td")[1].text.replace('N/A','-')
                avg_vol_10_day = table3[1].find_all("td")[1].text.replace('N/A','-')
                share_outstanding = table3[2].find_all("td")[1].text.replace('N/A','-')
                implied_share_outstanding = table3[3].find_all("td")[1].text.replace('N/A','-')
                float_s = table3[4].find_all("td")[1].text.replace('N/A','-')
                held_by_insiders = table3[5].find_all("td")[1].text.replace('N/A','-')
                held_by_institution = table3[6].find_all("td")[1].text.replace('N/A','-')
                shares_short = table3[7].find_all("td")[1].text.replace('N/A','-')
                short_ratio = table3[8].find_all("td")[1].text.replace('N/A','-')
                short_of_float = table3[9].find_all("td")[1].text.replace('N/A','-')
                short_of_shares_outstanding = table3[10].find_all("td")[1].text.replace('N/A','-')
                shares_short_prior_mon = table3[10].find_all("td")[1].text.replace('N/A','-')

                #-----------------Dividends and Splits------------------------------------------------------------------
                forward_annual_dividend_rate = table4[0].find_all("td")[1].text.replace('N/A','-')
                forward_annual_dividend_yeild = table4[1].find_all("td")[1].text.replace('N/A','-')
                trailing_annual_dividend_rate = table4[2].find_all("td")[1].text.replace('N/A','-')
                trailing_annual_dividend_yeild = table4[3].find_all("td")[1].text.replace('N/A','-')
                fiv_y_avg_dividend_yeild = table4[4].find_all("td")[1].text.replace('N/A','-')
                payout_ratio = table4[5].find_all("td")[1].text.replace('N/A','-')
                dividend_date = table4[6].find_all("td")[1].text.replace('N/A','-')
                ex_dividend_date = table4[7].find_all("td")[1].text.replace('N/A','-')
                last_split_factor = table4[8].find_all("td")[1].text.replace('N/A','-')
                last_split_date = table4[9].find_all("td")[1].text.replace('N/A','-')


                #-----------------Fiscal Year--------------------------------------------------------------------
                fiscal_year = table5[0].find_all("td")[1].text.replace('N/A','-')
                most_recent_quarter = table5[1].find_all("td")[1].text.replace('N/A','-')   

                #-----------------Profitability--------------------------------------------------------------------       
                profit_margin = table6[0].find_all("td")[1].text.replace('N/A','-')
                operating_margin = table6[1].find_all("td")[1].text.replace('N/A','-')  

                #-----------------Management Effectiveness---------------------------------------------------------       
                return_on_assets = table7[0].find_all("td")[1].text.replace('N/A','-')
                return_on_equity = table7[1].find_all("td")[1].text.replace('N/A','-')    

                #-----------------Income Statement------------------------------------------------------------------
                revenue = table8[0].find_all("td")[1].text.replace('N/A','-')
                revenue_per_share = table8[1].find_all("td")[1].text.replace('N/A','-')
                quarterly_rev_growth = table8[2].find_all("td")[1].text.replace('N/A','-')
                gross_prof = table8[3].find_all("td")[1].text.replace('N/A','-')
                ebitda = table8[4].find_all("td")[1].text.replace('N/A','-')
                net_income_avi_common = table8[5].find_all("td")[1].text.replace('N/A','-')
                diluted_eps = table8[6].find_all("td")[1].text.replace('N/A','-')
                quarterly_earnings_growth = table8[7].find_all("td")[1].text.replace('N/A','-')

                #-----------------Balance Sheet--------------------------------------------------------------------
                total_cash = table9[0].find_all("td")[1].text.replace('N/A','-')
                total_cash_per_share = table9[1].find_all("td")[1].text.replace('N/A','-')
                total_debt = table9[2].find_all("td")[1].text.replace('N/A','-')
                total_debt_equity = table9[3].find_all("td")[1].text.replace('N/A','-')
                current_ratio = table9[4].find_all("td")[1].text.replace('N/A','-')
                book_value_per_share = table9[5].find_all("td")[1].text.replace('N/A','-')

                #-----------------Cash Flow Statement--------------------------------------------------------------
                operating_cash_flow = table10[0].find_all("td")[1].text.replace('N/A','-')
                levered_free_cash_flow = table10[1].find_all("td")[1].text.replace('N/A','-')
            else:
                market_cap_intraday = '-'
        except:
            market_cap_intraday = '-'
            enterprise_val = '-'
            trailing_pe = '-'
            forward_pe = '-'
            peg_ratio_5y = '-'
            price_sales = '-'
            price_book = '-'
            enterprise_val_rev ='-'
            enterprise_val_ebit = '-'

            beta_5y_mon = '-'
            f_two_week_change = '-'
            sp500_52_week_change = '-'
            f_two_week_high = '-'
            f_two_week_low = '-'
            f_day_moving_avg = '-'
            t_hundred_day_moving_avg = '-'

            avg_vol_3_mon = '-'
            avg_vol_10_day = '-'
            share_outstanding = '-'
            implied_share_outstanding = '-'
            float_s = '-'
            held_by_insiders = '-'
            held_by_institution = '-'
            shares_short = '-'
            short_ratio = '-'
            short_of_float = '-'
            short_of_shares_outstanding = '-'
            shares_short_prior_mon = '-'

            forward_annual_dividend_rate ='-'
            forward_annual_dividend_yeild = '-'
            trailing_annual_dividend_rate = '-'
            trailing_annual_dividend_yeild = '-'
            fiv_y_avg_dividend_yeild = '-'
            payout_ratio ='-'
            dividend_date = '-'
            ex_dividend_date = '-'
            last_split_factor = '-'
            last_split_date = '-'

            fiscal_year = '-'
            most_recent_quarter = '-'  

            profit_margin = '-'
            operating_margin = '-'

            return_on_assets = '-'
            return_on_equity = '-'

            revenue = '-'
            revenue_per_share = '-'
            quarterly_rev_growth = '-'
            gross_prof = '-'
            ebitda = '-'
            net_income_avi_common = '-'
            diluted_eps = '-'
            quarterly_earnings_growth = '-'

            total_cash = '-'
            total_cash_per_share = '-'
            total_debt = '-'
            total_debt_equity = '-'
            current_ratio = '-'
            book_value_per_share = '-'

            operating_cash_flow = '-'
            levered_free_cash_flow = '-'



        data = {
            'Symbol': CMP,
            'Sector': sector,
            'Industry': industry,
            'Full Time Employees': full_time_employee,
            'Website': website,
            'Market Cap (intraday) 5': market_cap_intraday,
            'Enterprise Value 3': enterprise_val,
            'Trailing P/E': trailing_pe,
            'Forward P/E 1': forward_pe,
            'PEG Ratio(5 yr expected) 1': peg_ratio_5y,
            'Price/Sales (ttm)': price_sales,
            'Price/Book (mrq)': price_book,
            'Enterprise Value/Revenue 3': enterprise_val_rev,
            'Enterprise Value/EBITDA 7': enterprise_val_ebit,
            'Beta(5Y Monthly)': beta_5y_mon,
            '52-Week Change 3': f_two_week_change,
            'S&P500 52-Week Change 3': sp500_52_week_change,
            '52 Week High 3': f_two_week_high,
            '52 Week Low 3': f_two_week_low,
            '50-Day Moving Average 3': f_day_moving_avg,
            '200-Day Moving Average 3': t_hundred_day_moving_avg,
            'Avg Vol(3 month) 3': avg_vol_3_mon,
            'Avg Vol (10 day) 3': avg_vol_10_day,
            'Shares Outstanding 5':share_outstanding,
            'Implied Shares Outstanding 6':implied_share_outstanding,
            'Float': float_s,
            '% Held by Insiders 1': held_by_insiders,
            '% Held by Institutions 1': held_by_institution,
            'Shares Short 4': shares_short,
            'Short Ratio 4': short_ratio,
            'Short % of Float 4': short_of_float,
            'Short % of Shares Outstanding 4': short_of_shares_outstanding,
            'Shares Short(prior month ) 4': shares_short_prior_mon,
            'Forward Annual Dividend Rate 4': forward_annual_dividend_rate,
            'Forward Annual Dividend Yield 4': forward_annual_dividend_yeild,
            'Trailing Annual Dividend Rate 3': trailing_annual_dividend_rate,
            'Trailing Annual Dividend Yield 3': trailing_annual_dividend_yeild,
            '5 Year Average Dividend Yield 4': fiv_y_avg_dividend_yeild,
            'Payout Ratio 4': payout_ratio,
            'Dividend Date 3': dividend_date,
            'Ex-Dividend Date 4': ex_dividend_date,
            'Last Split Factor 2': last_split_factor,
            'Last Split Date 3': last_split_date,
            'Fiscal Year Ends': fiscal_year,
            'Most Recent Quarter (mrq)': most_recent_quarter,
            'Profit Margin': profit_margin,
            'Operating Margin (ttm)': operating_margin,
            'Return on Assets (ttm)': return_on_assets,
            'Return on Equity (ttm)': return_on_equity,
            'Revenue (ttm)': revenue,
            'Revenue Per Share (ttm)': revenue_per_share,
            'Quarterly Revenue Growth(yoy)': quarterly_rev_growth,
            'Gross Profit (ttm)': gross_prof,
            'EBITDA': ebitda,
            'Net Income Avi to Common (ttm)': net_income_avi_common,
            'Diluted EPS (ttm)': diluted_eps,
            'Quarterly Earnings Growth (yoy)': quarterly_earnings_growth,
            'Total Cash (mrq)': total_cash,
            'Total Cash Per Share (mrq)': total_cash_per_share,
            'Total Debt (mrq)': total_debt,
            'Total Debt/Equity (mrq)': total_debt_equity,
            'Current Ratio (mrq)': current_ratio,
            'Book Value Per Share (mrq)': book_value_per_share,
            'Operating Cash Flow (ttm)': operating_cash_flow,
            'Levered Free Cash Flow (ttm)': levered_free_cash_flow,
            'Total Revenue': total_rev,
            'Cost of Revenue': cost_rev,
            'Gross Profit': gross_prof,
            'Research Development': research_dev,
            'Selling General and Administrative': selling_gen_admin,
            'Total Operation Expense': total_operate_expense,
            'Operating Income or Loss': operate_income_loss,
            'Interest Expense': interest_expense,
            'Total Other Income/Expense Net': total_other_income_ex,
            'Income Tax Expense': income_tax_ex,
            'Income From Continuing Operations': income_continuing_operation,
            'Net Income': net_income,
            'Cash and Cash Equivalents': cash_cash_equiv,
            'Other short-term investments': other_short_invest,
            'Total Cash': total_cashs,
            'Net Recievables': net_receivables,
            'Inventory': inventory,
            'Other Current Assets': other_current_asset,
            'Total Current Assets': total_current_asset,
            'Total Current Liabilities': total_current_liability,
            'Total non-current liabilities': total_non_current_liability,
            'Total liabilities': total_liability,
            'Total stockholders equity': total_stockholders,
            'Dividend Paid 1': dividends_paid1,
            'Dividend Paid 2': dividends_paid2,
            'Dividend Paid 3': dividends_paid3,
            'Dividend Paid 4': dividends_paid4,
            'Dividend Paid 5': dividends_paid5,
            'Dividend Paid 6': dividends_paid6,
            'Free Cash Flow 1': free_cash_flow1,
            'Free Cash Flow 2': free_cash_flow2,
            'Free Cash Flow 3': free_cash_flow3,
            'Free Cash Flow 4': free_cash_flow4,
            'Free Cash Flow 5': free_cash_flow5,
            'Free Cash Flow 6': free_cash_flow6

        }
        lists.append(data)

    output_file_name = 'yahoo_finance_final'
    df1 = pd.DataFrame(lists)
    df = df1.reset_index(drop=True)
    df.to_csv('yahoo_finance_final.csv',encoding='utf-8', index=False)
    print(f'check the output file in same direcotry named as: {output_file_name}')

def mainmenu():
    print('\n')
    print('1. Continue scraping..')
    print('2. No, exit program')
    selection = int(input('Enter Choice: '))
    if selection == 1:
        scrape_whole()
    elif selection == 2:
        exit()
    else:
        print("Invalid Choice. Inter 1-3")
        mainmenu()


mainmenu()