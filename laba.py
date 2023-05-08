import sys
import os
import shutil


images_formats = ["PNG", "JPG", "JPEG", "SVG"]
videos_formats = ["AVI", "MP4", "MOV", "MKV"]
documents_formats = ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"]
audio_formats = ["MP3", "OGG", "WAV", "AMR"]
archives_formats = ["ZIP", "GZ", "TAR"]
folders = ["images", "videos", "documents", "audio", "archives"]

finded_files = {}
finded_formats = []
unknown_formats = []


trash_path = sys.argv[1]



def directory_sort(path):
    files = os.listdir(path)


    for file in files:
        if file not in folders:
            full_file_path = os.path.join(path, file)

            if os.path.isdir(full_file_path):
                directory_sort(full_file_path)
            else:
                full_file_name = full_file_path.split("\\")[-1]
                file_format = full_file_name.split(".")[-1]

                if file_format.upper() in images_formats:
                    image_sort(full_file_path)
                    finded_formats.append(file_format)
                elif file_format.upper() in videos_formats:
                    video_sort(full_file_path)
                    finded_formats.append(file_format)
                elif file_format.upper() in documents_formats:
                    document_sort(full_file_path)
                    finded_formats.append(file_format)
                elif file_format.upper() in audio_formats:
                    audio_sort(full_file_path)
                    finded_formats.append(file_format)
                elif file_format.upper() in archives_formats:
                    archive_sort(full_file_path)
                    finded_formats.append(file_format)
                else:
                    unknown_formats.append(file_format)
    
    for file in files:
        full_file_path = os.path.join(path, file)

        if os.path.isdir(full_file_path):
            if len(os.listdir(full_file_path)) == 0:
                os.rmdir(full_file_path)


def image_sort(file):
    folder_path = os.path.join(trash_path, "images")

    full_file_name = file.split("\\")[-1]
    file_name = full_file_name.split(".")[-2]
    file_name = normalize(file_name) 
    file_format = full_file_name.split(".")[-1]
    full_file_name = file_name + "." + file_format

    file_to_dir = os.path.join(folder_path, full_file_name)

    if not os.path.exists(file_to_dir):
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            finded_files["images"] = []
        
        finded_files["images"].append(full_file_name)
        os.rename(file, file_to_dir)
    else:
        os.remove(file)


def video_sort(file):
    folder_path = os.path.join(trash_path, "videos")

    full_file_name = file.split("\\")[-1]
    file_name = full_file_name.split(".")[-2]
    file_name = normalize(file_name) 
    file_format = full_file_name.split(".")[-1]
    full_file_name = file_name + "." + file_format
    file_to_dir = os.path.join(folder_path, full_file_name)

    if not os.path.exists(file_to_dir):
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            finded_files["videos"] = []
        
        finded_files["videos"].append(full_file_name)
        
        os.rename(file, file_to_dir)
    else:
        os.remove(file)


def document_sort(file):
    folder_path = os.path.join(trash_path, "documents")

    full_file_name = file.split("\\")[-1]
    file_name = full_file_name.split(".")[-2]
    file_name = normalize(file_name) 
    file_format = full_file_name.split(".")[-1]
    full_file_name = file_name + "." + file_format
    file_to_dir = os.path.join(folder_path, full_file_name)

    if not os.path.exists(file_to_dir):
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            finded_files["documents"] = []
        
        finded_files["documents"].append(full_file_name)
        
        os.rename(file, file_to_dir)
    else:
        os.remove(file)


def audio_sort(file):
    folder_path = os.path.join(trash_path, "audio")

    full_file_name = file.split("\\")[-1]
    file_name = full_file_name.split(".")[-2]
    file_name = normalize(file_name) 
    file_format = full_file_name.split(".")[-1]
    full_file_name = file_name + "." + file_format
    file_to_dir = os.path.join(folder_path, full_file_name)

    if not os.path.exists(file_to_dir):
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            finded_files["audio"] = []
        
        finded_files["audio"].append(full_file_name)
        
        os.rename(file, file_to_dir)
    else:
        os.remove(file)


def archive_sort(file):
    folder_path = os.path.join(trash_path, "archives")

    full_file_name = file.split("\\")[-1]
    file_name = full_file_name.split(".")[-2]
    file_name = normalize(file_name) 
    file_format = full_file_name.split(".")[-1]
    full_file_name = file_name + "." + file_format
    file_to_dir = os.path.join(folder_path, full_file_name.split(".")[-2])

    if not os.path.exists(file_to_dir):
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            finded_files["archives"] = []
        
        finded_files["archives"].append(full_file_name)

        os.makedirs(file_to_dir)
        shutil.unpack_archive(file, file_to_dir)
        os.remove(file)
    else:
        os.remove(file)


def info():
    print("Files:")
    for typ in finded_files:
        print(f"-{typ}-")
        for f in finded_files[typ]:
            print(f)
        print()
    
    print("\nFound formats known to the script:")
    for form in finded_formats:
        print(f"-{form}")
    
    print("\nFound formats unknown to the script:")
    for form in unknown_formats:
        print(f"-{form}")

def normalize(name):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    
    result = ''
    for symbol in name:
        if symbol.isalpha():
            if symbol.lower() in translit_dict:
                result +=translit_dict[symbol.lower()].upper() if symbol == symbol.upper()  else translit_dict[symbol.lower()]
            else:
                result += symbol
        elif symbol.isdigit():
            result += symbol
        else:
            result += "_"
    return result

directory_sort(trash_path)
info()