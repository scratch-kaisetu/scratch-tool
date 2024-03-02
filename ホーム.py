import streamlit as st
import secrets
import string

def get_random_password_string(length):
    pass_chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(pass_chars) for x in range(length))
    return password

st.set_page_config("むだtool", "📘")

st.title("無駄tool")

st.header("大量ブロック")
number = st.number_input('ブロックの数',min_value=2)
gazou_seisei = st.container(border=True)
if gazou_seisei.button('画像生成'):
    blocks1 = ""
    blocks2 = ""
    my_bar = gazou_seisei.progress(0, text="生成中...")
    for i in range(number):
        blocks1 += "<"
        my_bar.progress(round(i / number * 100), text=f"生成中...{i+1}/{number}")
    my_bar.empty()
    my_bar = gazou_seisei.progress(0, text="生成中...")
    for j in range(number):
        blocks2 += ">ではない"
        my_bar.progress(round(j / number * 100), text=f"生成中...{j+1}/{number}")
    my_bar.empty()
    
    gazou_seisei.link_button("アクセス","https://scratchblocks.github.io/#?style=scratch3&lang=ja&script="+blocks1+blocks2)

json_seisei = st.container(border=True)
if json_seisei.button('ファイル生成'):
    file_json = '{"targets":[{"isStage":true,"name":"Stage","variables":{"`jEk@4|i[#Fk?(8x)AV.-my variable":["変数",0]},"lists":{},"broadcasts":{},"blocks":{},"comments":{},"currentCostume":0,"costumes":[{"name":"This work by @rennto_ko in scratch is marked with CC0 1.0 Universal ","bitmapResolution":1,"dataFormat":"svg","assetId":"539c5b7c5c2d414424ff31f4c45964ea","md5ext":"539c5b7c5c2d414424ff31f4c45964ea.svg","rotationCenterX":231.75561900976138,"rotationCenterY":-148.0503420203301}],"sounds":[{"name":"project-audio","assetId":"b7f137b6da798d2a15443689546abb06","dataFormat":"mp3","rate":48000,"sampleCount":907800,"md5ext":"b7f137b6da798d2a15443689546abb06.mp3"}],"volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"on","textToSpeechLanguage":null},{"isStage":false,"name":"<>ではないx' + str(number) + '","variables":{},"lists":{},"broadcasts":{},"blocks":{"'
    data_randam_mae = get_random_password_string(20)
    file_json += data_randam_mae + '":{"opcode":"operator_not","next":null,"parent":null,"inputs":{"OPERAND":[2,"'
    data_randam2 = get_random_password_string(20)
    file_json += data_randam2 + '"]},"fields":{},"shadow":false,"topLevel":true,"x":0,"y":0},'
    my_bar = json_seisei.progress(0, text="生成中...")
    for json_generate in range(number-2):
        file_json += '"' + data_randam2 + '":{"opcode":"operator_not","next":null,"parent":"' + data_randam_mae + '","inputs":{"OPERAND":[2,"'
        data_randam2 = get_random_password_string(20)
        file_json += data_randam2 + '"]},"fields":{},"shadow":false,"topLevel":false},'
        data_randam_mae = data_randam2
        my_bar.progress(round(json_generate / (number-2) * 100), text=f"生成中...{json_generate+1}/{number}")
    my_bar.empty()

    
    file_json += '"' + data_randam2 + '":{"opcode":"operator_not","next":null,"parent":"' + data_randam_mae + '","inputs":{},"fields":{},"shadow":false,"topLevel":false}},"comments":{},"currentCostume":0,"costumes":[{"name":"<>ではない","bitmapResolution":1,"dataFormat":"svg","assetId":"d81886cf2d139ff03f4d6b5a2916c2f4","md5ext":"d81886cf2d139ff03f4d6b5a2916c2f4.svg","rotationCenterX":117.25710678118651,"rotationCenterY":32.00000000000003}],"sounds":[],"volume":100,"layerOrder":1,"visible":true,"x":0,"y":0,"size":100,"direction":90,"draggable":false,"rotationStyle":"all around"}],"monitors":[],"extensions":[],"meta":{"semver":"3.0.0","vm":"2.3.0","agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}}'

    json_seisei.download_button('jsonダウンロード', file_json ,file_name='project.json')
    
    json_seisei.link_button("他のファイルをダウンロード","https://www.dropbox.com/scl/fo/szcwloi7suuuzvzlei3i8/h?rlkey=69vis3br8f1qr4yctg3pvln3j&dl=0")







# ブロック::motion
# ブロック::looks
# ブロック::sound
# ブロック::events
# ブロック::control
# ブロック::sensing
# ブロック::operators
# ブロック::variables
# ブロック::list
# ブロック::custom
# ブロック::custom-arg
# ブロック::grey
# ブロック::undefined
# ブロック::#ace600