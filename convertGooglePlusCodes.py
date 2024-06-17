from openlocationcode import openlocationcode as olc 
import pandas as pd

df1 = pd.read_csv("data\臺南110＿內部中心點.csv", encoding="big5")
# df2 = pd.DataFrame([df1.iloc['WKT'].str.split()], columns=["Latitude", "Longitude"])

# print(df1['WKT'])
print("--------------------")
df1[['lon', 'lat']] = df1['WKT'].str.split(' ', expand=True)

#轉換padnas資料型態
# df1[['lon', 'lat']].convert_objects(convert_numeric=True).dtypes - 無法執行
df1['lon'] = pd.to_numeric(df1['lon'], errors='coerce')
df1['lat'] = pd.to_numeric(df1['lat'], errors='coerce')
# df1[['lon', 'lat']].astype(float).fillna(0.0)
print(df1[['lon', 'lat']])
print("--------------------")
print(type(df1.iloc[1]['lon']))
print("--------------------")


invalid_rows = df1[df1[['lon', 'lat']].isnull().any(axis=1)]
if not invalid_rows.empty:
    print("以下行包含無效的經緯度值，無法轉換為浮點數:")
    print(invalid_rows)
else:
    print("欄位座標轉換完成，沒有無效的經緯度數值")

# 移除包含 NaN 的行
df1 = df1.dropna(subset=['lon', 'lat'])

df1["googlePlus"] = df1.apply(lambda row: olc.encode(row['lat'], row['lon']), 'columns')
# df1["googlePlus"] =  olc.encode(df1['lat'], df1['lon'])
print(df1["googlePlus"])
# olc.encode(1.2867970586693043, 103.85451499941605)

#output to csv
df1.to_csv("data\\output\\GPC_Tainan110.csv", encoding="UTF-8")
