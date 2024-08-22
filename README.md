# script

### convertUTMtoECEF.py
```
python3 convertUTMtoECEF.py
```
指定したUTM座標系をECEF座標系に変換して出力するスクリプト

### csv_input.py
```
python3 csv_input.py
```
/vectornav/gnssから得た値をcsvファイルに保存するスクリプト

### vectornav_sim.py
```
python3 vectornav_sim.py
```
/odomに一定のオフセットをかけてECEF座標系の/vectornav/poseとしてパブリッシュするスクリプト

### autonomous.sh
```
./autonomous.sh
```
bool型の/autonomousをtrueでパブリッシュするシェル

### csv_clean.py
```
python3 csv_clean.py
```
入力したcsvを小数点第6位で四捨五入して新しいcsvファイルに保存するスクリプト

### csv_input_soft.py
```
python3 csv_input_soft.py
```
/vectornav/gnssから得た値を10回に1回csvファイルに保存するスクリプト
