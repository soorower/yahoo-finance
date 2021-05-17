import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(
    url='https://discord.com/api/webhooks/840041328401842187/Hsw4Ih0CgCUtoIj4DHORY_-UZ_PLIwd9wyJxPntKPkgKkTIIdPWltYTHsgz35PlAiRJt', username="Flippa Scraped File")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
# df = pd.read_csv('https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?access_token=83ff96335c2d45a094df02a206a39ff4')
# df['Ticker'] = df['ASX code'] + ".AX"
# tickers = df['Ticker'].tolist()

tickers = ["AAPL"]
lists = []
data = {}
counter = 1
for ticker in tickers:
    print(counter)
    counter = counter + 1
    CMP = ticker
    print(CMP)
    url1 = "https://uk.finance.yahoo.com/quote/" + CMP + "?p=" + CMP
    url2 = "https://uk.finance.yahoo.com/quote/" + CMP + "/key-statistics?p=" + CMP
    # url3 = "https://finance.yahoo.com/quote/" + CMP + "/financials?p=" + CMP
    # url4 = "https://au.finance.yahoo.com/quote/" + CMP + "/balance-sheet?p=" + CMP
    # url5 = "https://au.finance.yahoo.com/quote/" + CMP + "/cash-flow?p=" + CMP
    # try:
    page1 = requests.get(url1,headers = headers)
    soup = BeautifulSoup(page1.content, 'html.parser')
    alldata = soup.find_all("tbody")
    print(len(alldata))
    if len(alldata)>1:
        table1s = alldata[0].find_all("tr")
        table2s = alldata[1].find_all("tr")

        for i in range(0,len(table1s)):
            table1_td = table1s[i].find_all("td")
            a = table1_td[0].text
            b = table1_td[1].text
            if 'Previous close' in a:
                previous_close = b
            if 'Open' in a:
                op_en = b
            if 'Bid' in a:
                bid = b
            if 'Ask' in a:
                ask = b
            if "Day's range" in a:
                days_range = b
            if '52-week range' in a:
                ftwo_week_range = b
            if 'Volume' in a[:6]:
                volume = b
            if 'Avg. volume' in a:
                avg_volume = b

        for i in range(0,len(table2s)):
            table2_td = table2s[i].find_all("td")
            a = table2_td[0].text
            b = table2_td[1].text
            if 'Market cap' in a:
                market_cap = b
            if 'Beta (5Y monthly)' in a:
                beta_5y_mon = b
            if 'PE ratio (TTM)' in a:
                pe_ratio = b
            if 'EPS (TTM)' in a:
                eps_ttm = b
            if "Earnings date" in a:
                earnings_date = b
            if 'Forward dividend & yield' in a:
                forward_dividend = b
            if 'Ex-dividend date' in a:
                ex_dividend = b
            if '1y target est' in a:
                one_y_target = b
                
        if 'Statistics' in soup.findAll('span',attrs = {'data-reactid':'20'})[1].text:
            page2 = requests.get(url2,headers = headers)
            soup2 = BeautifulSoup(page2.text, 'html.parser')

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
            market_cap_intraday = table1[0].find_all("td")[1].text
            enterprise_val = table1[1].find_all("td")[1].text
            trailing_pe = table1[2].find_all("td")[1].text
            forward_pe = table1[3].find_all("td")[1].text
            peg_ratio_5y = table1[4].find_all("td")[1].text
            price_sales = table1[5].find_all("td")[1].text
            price_book = table1[6].find_all("td")[1].text
            enterprise_val_rev = table1[7].find_all("td")[1].text
            enterprise_val_ebit = table1[8].find_all("td")[1].text

            #-----------------Stock Price History-------------------------------------------------------------------
            beta_5y_mon = table2[0].find_all("td")[1].text
            f_two_week_change = table2[1].find_all("td")[1].text
            sp500_52_week_change = table2[2].find_all("td")[1].text
            f_two_week_high = table2[3].find_all("td")[1].text
            f_two_week_low = table2[4].find_all("td")[1].text
            f_day_moving_avg = table2[5].find_all("td")[1].text
            t_hundred_day_moving_avg = table2[6].find_all("td")[1].text

            #------------------Share Statistics---------------------------------------------------------------------   
            avg_vol_3_mon = table3[0].find_all("td")[1].text
            avg_vol_10_day = table3[1].find_all("td")[1].text
            share_outstanding = table3[2].find_all("td")[1].text
            implied_share_outstanding = table3[3].find_all("td")[1].text
            float_s = table3[4].find_all("td")[1].text
            held_by_insiders = table3[5].find_all("td")[1].text
            held_by_institution = table3[6].find_all("td")[1].text
            shares_short = table3[7].find_all("td")[1].text
            short_ratio = table3[8].find_all("td")[1].text
            short_of_float = table3[9].find_all("td")[1].text
            short_of_shares_outstanding = table3[10].find_all("td")[1].text
            shares_short_prior_mon = table3[10].find_all("td")[1].text

            #-----------------Dividends and Splits------------------------------------------------------------------
            forward_annual_dividend_rate = table4[0].find_all("td")[1].text
            forward_annual_dividend_yeild = table4[1].find_all("td")[1].text
            trailing_annual_dividend_rate = table4[2].find_all("td")[1].text
            trailing_annual_dividend_yeild = table4[3].find_all("td")[1].text
            fiv_y_avg_dividend_yeild = table4[4].find_all("td")[1].text
            payout_ratio = table4[5].find_all("td")[1].text
            dividend_date = table4[6].find_all("td")[1].text
            ex_dividend_date = table4[7].find_all("td")[1].text
            last_split_factor = table4[8].find_all("td")[1].text
            last_split_date = table4[9].find_all("td")[1].text


            #-----------------Fiscal Year--------------------------------------------------------------------
            fiscal_year = table5[0].find_all("td")[1].text
            most_recent_quarter = table5[1].find_all("td")[1].text   

            #-----------------Profitability--------------------------------------------------------------------       
            profit_margin = table6[0].find_all("td")[1].text
            operating_margin = table6[1].find_all("td")[1].text  

            #-----------------Management Effectiveness---------------------------------------------------------       
            return_on_assets = table7[0].find_all("td")[1].text
            return_on_equity = table7[1].find_all("td")[1].text    

            #-----------------Income Statement------------------------------------------------------------------
            revenue = table8[0].find_all("td")[1].text
            revenue_per_share = table8[1].find_all("td")[1].text
            quarterly_rev_growth = table8[2].find_all("td")[1].text
            gross_prof = table8[3].find_all("td")[1].text
            ebitda = table8[4].find_all("td")[1].text
            net_income_avi_common = table8[5].find_all("td")[1].text
            diluted_eps = table8[6].find_all("td")[1].text
            quarterly_earnings_growth = table8[7].find_all("td")[1].text

            #-----------------Balance Sheet--------------------------------------------------------------------
            total_cash = table9[0].find_all("td")[1].text
            total_cash_per_share = table9[1].find_all("td")[1].text
            total_debt = table9[2].find_all("td")[1].text
            total_debt_equity = table9[3].find_all("td")[1].text
            current_ratio = table9[4].find_all("td")[1].text
            book_value_per_share = table9[5].find_all("td")[1].text

            #-----------------Cash Flow Statement--------------------------------------------------------------
            operating_cash_flow = table10[0].find_all("td")[1].text
            levered_free_cash_flow = table10[1].find_all("td")[1].text
        else:
            market_cap_intraday = '-'
    else:
        market_cap = '-'
        market_cap_intraday = '-'
    # except:
    #     market_cap = '-'
        # market_cap_intraday = '-'
    data = {
        'Previous Close': previous_close,
        'Open': op_en,
        'Bid': bid,
        'Ask': ask,
        'Days Range': days_range,
        '52 Week Range': ftwo_week_range,
        'Volume': volume,
        'Average Volume': avg_volume,
        'Market Cap': market_cap,
        'Beta (5Y monthly)': beta_5y_mon,
        'PE Ratio(TTM)': pe_ratio,
        'EPS (TTM)': eps_ttm,
        'Earnings Date': earnings_date,
        'Forward Dividend & Yeild': forward_dividend,
        'Ex-Dividend Date': ex_dividend,
        '1y Target Est': one_y_target,
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
        'Levered Free Cash Flow (ttm)': levered_free_cash_flow
    }
    lists.append(data)
    
    print(f'Previous Close: {previous_close}')
    print(f'Market Cap(intraday): {market_cap_intraday}')
    
df1 = pd.DataFrame(lists)
df = df1.drop_duplicates(subset=['Market Cap','Market Cap (intraday) 5'], keep='first').reset_index(drop=True)
df.to_csv('yahoo_finance_aapl.csv',encoding='utf-8', index=False)

sleep(2)

embed = DiscordEmbed(title='Blaise', description=f'Yahoo Finance')
with open(f'yahoo_finance_aapl.csv', "rb") as f:
    webhook.add_file(file=f.read(), filename=f'Yahoo_finance_aapl.csv')
webhook.add_embed(embed)
response = webhook.execute()



# historical data scrape for fiverr client - yahoo finance
# symbols = ['MSFT']
# print('Collecting HTML data started..')
# res = []
# for symbol in symbols:
#     CMP = symbol
#     print(CMP)
#     url = "https://uk.finance.yahoo.com/quote/" + CMP + "/history?p=" + CMP
#     page = requests.get(url, headers=headers, timeout= 10).content
#     res.append(page)


# counter = 1
# print("Please wait, Almost Done!")
# for symbol,result in zip(symbols,res):
#     lists = []
#     data = {}
#     print(counter)
#     counter = counter + 1
#     CMP = symbol
#     print(CMP)
#     soup = BeautifulSoup(result, 'html.parser')

#     boxs = soup.find('table',attrs={'data-test':'historical-prices'}).find('tbody').findAll('tr')
#     for box in boxs:
#         tds = box.findAll('td')
#         if len(tds)>2:
#             try:
#                 date = tds[0].find('span').text
#             except:
#                 date = 'Not Found'
#             try:
#                 open = tds[1].find('span').text
#             except:
#                 open = 'Not Found'
#             try:
#                 close = tds[4].find('span').text
#             except:
#                 close = 'Not Found'
#             try:
#                 adj_close = tds[5].find('span').text
#             except:
#                 adj_close = 'Not Found'
#             try:
#                 volume = tds[6].find('span').text
#             except:
#                 volume = 'Not Found'
#         else:
#             try:
#                 date = tds[0].find('span').text
#             except:
#                 date = 'Not Found'
#             try:
#                 divindend1 = tds[1].find('strong').text
#                 divindend2 = tds[1].find('span').text
#                 open = f'Dividend: {divindend1} {divindend2}'
#             except:
#                 open = '-'
#             close = '-'
#             adj_close = '-'
#             volume = '-'
#         data = {
#             'Symbol': CMP,
#             'Date': date,
#             'Open': open,
#             'Close': close,
#             'Adj. Close': adj_close,
#             'Volume': volume
#         }
#         lists.append(data)
        
#     df1 = pd.DataFrame(lists)
#     df = df1.reset_index(drop=True)
#     df.to_csv(f'yahoo_historical_{CMP}.csv',encoding='utf-8', index=False)
#     data = {}
#     lists = []