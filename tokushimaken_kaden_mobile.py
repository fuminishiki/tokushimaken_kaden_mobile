import folium

m = folium.Map(location=[33.8480250,134.2431628],zoom_start=9)
m

folium.Marker(location=[34.0792794,134.5069953],popup='エディオン タクト店　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.1180356,134.49918],popup='ヤマダデンキ テックランド徳島藍住店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.1327295,134.5763932],popup='ヤマダデンキ テックランド徳島松茂店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.0871234,134.5497321],popup='ヤマダデンキ Tecc LIFE SELECT 徳島本店　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.1163975,134.5042361],popup='ケーズデンキ 藍住店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.9168551,134.6727495],popup='ケーズデンキ 阿南店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.0497976,134.5524917],popup='ケーズデンキ 沖浜店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.0835757,134.3877096],popup='ケーズデンキ 鴨島店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.0649367,134.1598082],popup='ケーズデンキ 脇町店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.0625099,134.5734905],popup='イオンモバイル 徳島店　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[34.0517457,134.5531494],popup='パソコン工房 徳島店　　　　　　　　　',icon=folium.Icon(color="green")).add_to(m)
m

folium.Marker(location=[34.3481671,134.0515907],popup='マーキュリー 香川営業所　　　　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('tokushimaken_kaden_mobile.html')
