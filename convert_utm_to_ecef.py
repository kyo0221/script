import pyproj

# UTM座標 (EPSG:32654)
utm_x = 408335.218
utm_y = 3997006.045

# UTM座標系 (EPSG:32654) から地理座標系 (EPSG:4326) への変換
utm_proj = pyproj.Proj('EPSG:32654')
wgs84_proj = pyproj.Proj('EPSG:4326')
longitude, latitude = pyproj.transform(utm_proj, wgs84_proj, utm_x, utm_y)

# 地理座標系 (EPSG:4326) から ECEF座標系 (EPSG:4978) への変換
ecef_proj = pyproj.Proj('EPSG:4978')
x, y, z = pyproj.transform(wgs84_proj, ecef_proj, longitude, latitude, 0)

print(f"ECEF座標: X={x}, Y={y}, Z={z}")
