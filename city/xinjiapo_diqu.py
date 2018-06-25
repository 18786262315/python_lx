import pymysql



diqu = [
    {'name': "D1",
     'keys': ['Cecil',
              'Marina',
              'RafflesPlace',
              "People'sPark",
              'BoatQuay',
              'Marina']
     },


    {'name': "D2",
     'keys': ["AnsonRoad",
              "TanjongPagar",
              "Chinatown"]},


    {'name': "D3",
     'keys': ["Queenstown",
              "TiongBahru",
              "Alexandra",
              "Commonwealth"]},


    {'name': "D4",
     'keys': ["TelokBlangah",
              "MountFaber",
              "Harbourfront",
              "Sentosa"]},

    {

        'name': "D5",
        'keys': ["Clementi",
                 "PasirPanjang",
                 "WestCoast",
                 "Dover",
                 "BuonaVista"]},


    {
        'name': "D6",
        'keys': ["HighStreet",
                 "BeachRoad",
                 "Cityhall",
                 "ClarkeQuay"]},


    {
        'name': "D7",
        'keys': ["GoldenMile",
                 "MiddleRoad",
                 "BeachRoad",
                 "Bugis",
                 "Rochor"]},



    {'name': "D8",
     'keys': ["LittleIndia",
              "FarrerPark",
              "SerangoonRd"]},



    {'name': "D9",
     'keys': ["OrchardRoad",
              "RiverValley",
              "Cairnhill"]},



    {'name': "D10",
     'keys': ["TanglinRoad",
              "Farrer",
              "Holland",
              "BukitTimah",
              "Ardmore"]
     },


    {'name': "D11",
     'keys': ["Thomson",
              "WattenEstate",
              "Novena",
              "Newton"]
     },

    {
        'name': "D12",
        'keys': ["Serangoon",
                 "ToaPayoh",
                 "Balestier"]
    },


    {'name': "D13",
     'keys': ["Braddell",
              "Macpherson",
              "PotongPasir"]},



    {'name': "D14",
     'keys': ["Sims",
              "PayaLebar",
              "Geylang",
              "Eunos"]},


    {
        'name': "D15",
        'keys': ["TanjongRhu",
                 "Meyer",
                 "MarineParade",
                 "Katong",
                 "AmberRoad",
                 "JooChiat",
                 "EastCoast"]},



    {'name': "D16",
     'keys': ["KewDrive",
              "UpperEastCoastRoad",
              "Eastwood",
              "Bedok",
              "Siglap",
              "Bayshore"]},



    {'name': "D17",
     'keys': ["Flora",
              "Loyang",
              "Changi",
              "ChangiAirport",
              "ChangiVillage"]},


    {
        'name': "D18",
        'keys': ["Simei",
                 "Tampines",
                 "PasirRis"]},



    {'name': "D19",
     'keys': ["Hougang",
              "Punggol",
              "Sengkang",
              "Serangoon"]
     },

    {
        'name': "D20",
        'keys': ["MeiHwan",
                 "Thomson",
                 "AngMoKio",
                 "Bishan",
                 "Braddell"]},



    {'name': "D21",
     'keys': ["UpperBukitTimah",
              "UluPandan",
              "ClementiPark"]
     },

    {
        'name': "D22",
        'keys': ["Lakeside",
                 "Jurong",
                 "BoonLay",
                 "Tuas"]},



    {'name': "D23",
     'keys': ["ChoaChuKang",
              "BukitBatok",
              "DairyFarm",
              "Hillview",
              "BukitPanjang"]},


    {
        'name': "D24",
        'keys': ["LimChuKang",
                 "ChoaChuKang",
                 "Tengah"]},



    {'name': "D25",
     'keys': ["Woodgrove",
              "Kranji",
              "Woodlands"]},


    {
        'name': "D26",
        'keys': ["UpperThomson",
                 "Springleaf",
                 "Mandai"]},


    {'name': "D27",
     'keys': ["Sembawang",
              "Yishun"]},


    {'name': "D28",
     'keys': ['Seletar',
              'Yio Chu Kang']}
]

text1 = open('keys.sql','a',encoding='utf-8') 


# sql = "INSERT INTO mr_circles (code,name,citycode) VALUES ("+"'"+str(code)+"','"+str(i['name'])+"','"+str(110011)+"');"


code = 10000
for i in diqu:
  code+=100
  code_i =code
  sql = "INSERT INTO mr_district (code,name,citycode) VALUES ("+"'"+str(code)+"','"+str(i['name'])+"','"+str(10000)+"');"
  print('\n',sql)
  text1.write(sql+'\n')
  for m in i['keys'] :
    code_i+=1
    sql = "INSERT INTO mr_circles (code,name,districtcode) VALUES ("+"'"+str(code_i)+"','"+str(m)+"','"+str(code)+"');"
    print(sql)
    text1.write(sql+'\n')
