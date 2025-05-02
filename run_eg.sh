# python train.py -s ek_eg_no_sub/P03_03 --port 6017 --expname "eg/ek_eg_1_ex_no_sub" --configs arguments/eg/default.py --eval
# python render.py -m output/ek/ek_eg_1_ex_no_sub --configs arguments/eg/default.py --eval

# python train.py -s ek_eg_no_sub/P17_01 --port 6017 --expname "eg/ek_eg_2_ex_no_sub" --configs arguments/eg/default.py --eval
# python render.py -m output/ek/ek_eg_2_ex_no_sub --configs arguments/eg/default.py --eval

# python train.py -s ek_eg_no_sub/P18_06 --port 6017 --expname "eg/ek_eg_3_ex_no_sub" --configs arguments/eg/default.py --eval
# python render.py -m output/ek/ek_eg_3_ex_no_sub --configs arguments/eg/default.py --eval

# python train.py -s ek_eg_no_sub/P32_01 --port 6017 --expname "eg/ek_eg_4_ex_no_sub" --configs arguments/eg/default.py --eval
# python render.py -m output/ek/ek_eg_4_ex_no_sub --configs arguments/eg/default.py --eval


# python train.py -s hoi4d_eg_no_sub/Video1 --port 6017 --expname "hoi4d/hoi4d_eg_1_ex_no_sub" --configs arguments/eg/default.py --eval
python render.py -m output/hoi4d/hoi4d_eg_1_ex_no_sub --configs arguments/eg/default.py --eval

# python train.py -s hoi4d_eg_no_sub/Video2 --port 6017 --expname "hoi4d/hoi4d_eg_2_ex_no_sub" --configs arguments/eg/default.py --eval
python render.py -m output/hoi4d/hoi4d_eg_2_ex_no_sub --configs arguments/eg/default.py --eval

python train.py -s hoi4d_eg_no_sub/Video3 --port 6017 --expname "hoi4d/hoi4d_eg_3_ex_no_sub" --configs arguments/eg/default.py --eval
python render.py -m output/hoi4d/hoi4d_eg_3_ex_no_sub --configs arguments/eg/default.py --eval

python train.py -s hoi4d_eg_no_sub/Video4 --port 6017 --expname "hoi4d/hoi4d_eg_4_ex_no_sub" --configs arguments/eg/default.py --eval
python render.py -m output/hoi4d/hoi4d_eg_4_ex_no_sub --configs arguments/eg/default.py --eval

python train.py -s hoi4d_eg_no_sub/Video5 --port 6017 --expname "hoi4d/hoi4d_eg_5_ex_no_sub" --configs arguments/eg/default.py --eval
python render.py -m output/hoi4d/hoi4d_eg_5_ex_no_sub --configs arguments/eg/default.py --eval