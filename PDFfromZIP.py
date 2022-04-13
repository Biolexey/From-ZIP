import os
import zipfile
import shutil

"""
Uncomment the "print" functions if you want to check the behavior of this code !

"""

global need_extension, target_extension                                 #拡張子をグローバル宣言
need_extension = '.pdf'                                                 #求める拡張子
target_extension = ".zip"                                               #抽出元拡張子

if not "./extract_files/":                                              #抽出ファイル格納フォルダ作成
    os.mkdir("./extract_files")

def openzip(name):                                                      #展開関数
    with zipfile.ZipFile(f'target_files/{name}', mode="r") as my_zip:
        my_zip.extractall("target_files")
        #print(f"{name}を展開しました")
        check(my_zip, my_zip.namelist())                                #check関数

def check(my_zip, namelist):                                            #中身閲覧関数
    for file in namelist:
        #print(f"{file}をチェックしています")
        if my_zip.getinfo(file).filename.endswith(need_extension):      #目当ての拡張子ならextractフォルダへ
            shutil.move(f"./target_files/{file}", "./extract_files/")
            #print(f"{file}をextractへ")
        elif my_zip.getinfo(file).filename.endswith(target_extension):  #zipファイルならもう一度展開
            #print(f"{file}はzipなので")            
            openzip(file)
        else:
            #print(f"これには何もしません")
            None
    
def main():
    name = "2022_0Y_30812_select_assignment_status_88802"+".zip"                                              #targetフォルダの中に格納した目当てのzipファイル名を"target"へ
    openzip(name)

if __name__ == "__main__":
    main()