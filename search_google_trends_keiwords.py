from pytrends.request import TrendReq
import sys

# 検索キーワード
print("検索したいキーワードを入力してください。")
inputKeyword = input()
kw_list = [inputKeyword]

# GoogleTrands
google_trend_list = []

# 検索する期間（n日）
print("検索したい期間を選択してください。\n1：過去1日間\n2：過去7日間\n3：過去1ヶ月間\n4：過去3ヶ月間\nその他の数字／文字列：過去5年間")

selectTime = input()
if 1 == selectTime:
    inputTime = 'now 1-d'
elif 2 == selectTime:
    inputTime = 'now 7-d'
elif 3 == selectTime:
    inputTime = 'today 1-m'
elif 4 == selectTime:
    inputTime = 'today 3-m'
else:
    inputTime = 'today 5-y'

# 検索開始
pytrends = TrendReq(hl='ja-JP', tz=360)
pytrends.build_payload(kw_list, cat=0, timeframe=inputTime, geo='JP', gprop='')
trends = pytrends.related_queries()

trends_values = trends[inputKeyword]['top'].values.tolist()

# 検索結果整形
for value in trends_values:
    item = str(value[0]).strip(inputKeyword)
    item = item.replace('　', '')
    item = item.replace(' ', '')
    google_trend_list.append(item)

# 検索結果表示
print(inputKeyword + 'に関連するトレンドは' + str(google_trend_list) + 'です。')
