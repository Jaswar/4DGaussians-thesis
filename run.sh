python train.py -s ego_exo_data/all_saves/gopro/georgiatech_covid_03_4 --port 6017 --expname "ego_exo/with_val_set/gopro/georgiatech_covid_03_4" --configs arguments/ego_exo/default.py
python train.py -s ego_exo_data/all_saves/camera-rgb/georgiatech_covid_03_4 --port 6017 --expname "ego_exo/with_val_set/camera-rgb/georgiatech_covid_03_4" --configs arguments/ego_exo/default.py

python train.py -s ego_exo_data/all_saves/gopro/iiith_cooking_58_2 --port 6017 --expname "ego_exo/with_val_set/gopro/iiith_cooking_58_2" --configs arguments/ego_exo/default.py
python train.py -s ego_exo_data/all_saves/camera-rgb/iiith_cooking_58_2 --port 6017 --expname "ego_exo/with_val_set/camera-rgb/iiith_cooking_58_2" --configs arguments/ego_exo/default.py

python train.py -s ego_exo_data/all_saves/gopro/unc_basketball_03-31-23_01_17 --port 6017 --expname "ego_exo/with_val_set/gopro/unc_basketball_03-31-23_01_17" --configs arguments/ego_exo/default.py
python train.py -s ego_exo_data/all_saves/camera-rgb/unc_basketball_03-31-23_01_17 --port 6017 --expname "ego_exo/with_val_set/camera-rgb/unc_basketball_03-31-23_01_17" --configs arguments/ego_exo/default.py


python render.py -m output/ego_exo/with_val_set/gopro/georgiatech_covid_03_4 --configs arguments/ego_exo/default.py --eval
python render.py -m output/ego_exo/with_val_set/camera-rgb/georgiatech_covid_03_4 --configs arguments/ego_exo/default.py --eval

python render.py -m output/ego_exo/with_val_set/gopro/iiith_cooking_58_2 --configs arguments/ego_exo/default.py --eval
python render.py -m output/ego_exo/with_val_set/camera-rgb/iiith_cooking_58_2 --configs arguments/ego_exo/default.py --eval

python render.py -m output/ego_exo/with_val_set/gopro/unc_basketball_03-31-23_01_17 --configs arguments/ego_exo/default.py --eval
python render.py -m output/ego_exo/with_val_set/camera-rgb/unc_basketball_03-31-23_01_17 --configs arguments/ego_exo/default.py --eval
