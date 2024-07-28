import os
from os.path import exists, isdir
from txt_to_md import *
from file_manage import filesCopy

#cli ansi colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"



def extract_title(mdfile):
    try:
        f = open(mdfile)
        pass
    except Exception as e:
        print(f"{RED}******* no file named {YELLOW}{mdfile}{RESET} found at current dir ******* {RESET}")
        exit()

    firstLn = f.readline()
    f.close()
    firstLn = firstLn.strip()
    if firstLn.startswith('#') and firstLn.startswith('##'):
        print(f"{RED}*** invalid file with no title block ***{RESET}")
        exit()
    return firstLn.replace('#','').strip()

def generate_pages(from_path , template_path, dest_path):
    if not (os.path.exists(from_path) and os.path.exists(template_path)):
        raise FileNotFoundError
    print(f"*** Generating page from {GREEN}{from_path}{RESET} to {GREEN}{dest_path}{RESET} using {GREEN}{template_path}{RESET} as template ***")

    if os.path.isdir(from_path):
        dir_list = os.listdir(from_path)
        for item in dir_list:
                from_item = f"{from_path}/{item}"
                dest_item = f"{dest_path}/{item}"
                generate_pages(from_path=from_item,template_path=template_path, dest_path= dest_item)
    else:
        f = open(from_path) #opened content file
        mdcontent = f.read()
        f.close()           #closed content file
        html_content = md_to_html_node(mdcontent)
        
        f = open(template_path) #opened template
        template_content = f.read()
        f.close() #closed template

        content_title = extract_title(from_path)
        try :
            template_content = template_content.replace("{{ Title }}",content_title)
            html_content = template_content.replace("{{ Content }}",html_content)
            pass
        except Exception :
            print("*** Invalid Template ***")
            exit()

        if not os.path.exists(dest_path):
            dirs = os.path.dirname(dest_path)
            os.makedirs(dirs,exist_ok=True)

        html_file = open(dest_path, mode='w' ) # opened/created destination file
        html_file.write(html_content)

        html_file.close()

    return 


def main():
    print(f"{GREEN} *** *** *** Wellcome to Static Site Generator *** *** *** {RESET}")

    generate_pages(from_path="content", template_path="template.html", dest_path="static")

    filesCopy("static","public")

    print(f"{GREEN}*** Successfully generated html pages , Run python server at ./public dir to see ***{RESET}")

    return 


main()
