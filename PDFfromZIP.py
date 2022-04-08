import os
import zipfile
import shutil

global need_extension, target_extension
need_extension = '.pdf'
target_extension = ".zip"

if not "./extract_files/":
    os.mkdir("./extract_files/")

def openzip(name):                                                      #展開関数
    my_zip = zipfile.ZipFile(f'target_files/{name}', mode="r")
    my_zip.extractall("target_files")
    print(f"{name}を展開しました")
    check(my_zip, my_zip.namelist())
    my_zip.close()

def check(my_zip, namelist):                                            #中身閲覧関数
    for file in namelist:
        print(f"{file}をチェックしています")
        if my_zip.getinfo(file).filename.endswith(need_extension):      #目当ての拡張子ならextractフォルダへ
            shutil.move(file, "./extract_files/")
            print(f"{file}をextractへ")
        elif my_zip.getinfo(file).filename.endswith(target_extension):  #zipファイルならもう一度展開
            print(f"{file}はzipなので")            
            openzip(file)
        else:
            print(f"これには何もしません")
            None
    
def main():
    name = "target.zip"
    openzip(name)

if __name__ == "__main__":
    main()
