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
print(df1["googlePlus"][1])
print("--------------")
# olc.encode(1.2867970586693043, 103.85451499941605)

#add eid
lut_county_byname = {
    '臺北市': ['A', 'Taipei'],
    '新北市': ['F', 'NewTaipei'],
    '基隆市': ['C', 'Keelung'],
    '桃園市': ['H', 'Taoyuan'],
    '新竹市': ['O', 'Hsinchu'],
    '新竹縣': ['J', 'Hsinchu'],
    '苗栗縣': ['K', 'Miaoli'],
    '臺中市': ['B', 'Taichung'],
    '彰化縣': ['N', 'Changhua'],
    '南投縣': ['M', 'Nantou'],
    '雲林縣': ['P', 'Yunlin'],
    '嘉義縣': ['Q', 'Chiayi'],
    '嘉義市': ['I', 'Chiayi'],
    '臺南市': ['D', 'Tainan'],
    '高雄市': ['E', 'Kaohsiung'],
    '屏東縣': ['T', 'Pingtung'],
    '宜蘭縣': ['G', 'Ilan'],
    '花蓮縣': ['U', 'Hualien'],
    '臺東縣': ['V', 'Taitung'],
    '澎湖縣': ['X', 'Penghu'],
    '金門縣': ['W', 'Jinmen'],
    '連江縣': ['Z', 'Lianjiang']
}

def createEid(inputDF, countyName, year):

    lut_county_byname = {
    '臺北市': ['A', 'Taipei'],
    '新北市': ['F', 'NewTaipei'],
    '基隆市': ['C', 'Keelung'],
    '桃園市': ['H', 'Taoyuan'],
    '新竹市': ['O', 'Hsinchu'],
    '新竹縣': ['J', 'Hsinchu'],
    '苗栗縣': ['K', 'Miaoli'],
    '臺中市': ['B', 'Taichung'],
    '彰化縣': ['N', 'Changhua'],
    '南投縣': ['M', 'Nantou'],
    '雲林縣': ['P', 'Yunlin'],
    '嘉義縣': ['Q', 'Chiayi'],
    '嘉義市': ['I', 'Chiayi'],
    '臺南市': ['D', 'Tainan'],
    '高雄市': ['E', 'Kaohsiung'],
    '屏東縣': ['T', 'Pingtung'],
    '宜蘭縣': ['G', 'Ilan'],
    '花蓮縣': ['U', 'Hualien'],
    '臺東縣': ['V', 'Taitung'],
    '澎湖縣': ['X', 'Penghu'],
    '金門縣': ['W', 'Jinmen'],
    '連江縣': ['Z', 'Lianjiang']
    }

    countyCodeName = lut_county_byname[countyName][0]
    for index,  googlePlus in enumerate(inputDF["googlePlus"]):
        inputDF.at[index, "eid"] = countyCodeName + "-" + year + "-" + str(index+1).zfill(5)
    
    return inputDF

    
df2 = createEid(df1, '臺南市', '110')

print(df2.loc[0:1])
print("-------------")

# #output to csv
# df1.to_csv("data\\output\\GPC_Tainan110.csv", encoding="big5")
