"""
written by Perseus06

Name:
web_fuzzer.py

Description:
A web fuzzing tool - script that maps pages in a specific website, and prints the existing pages found on the website.
The script using a .txt file containing possible names for web pages, and check for each name if there is an actual page on the website with this name.
"""

# imports
import requests


# constants
WEBSITE_URL = r"http://www.github.com"
POSSIBLE_WEBPAGES_FILE = r"web pages names.txt"


# function that receives a name and checks if the website contains a page with this name.
def check_webpage_name(file_name, full_output):
    # combine the website and the page name to create the full url.
    webpage_url = f"{WEBSITE_URL}/{file_name}"
    # using requests module, send to the web server an HTTP GET request for the webpage url (we ask from the web server for the HTML code of the webpage).
    # based on the server's response, the script can state if the webpage truly exists or not.
    response_from_website = requests.get(webpage_url)
    # if the status code of the server's response is 200, it means the webpage exists.
    if response_from_website.status_code == 200:
        if full_output == True:
            print(f"{webpage_url} - exists in the website.\n")
        else:
            print(webpage_url, "\n")
        return True
    # if the status code of the server's response is 404, it means the webpage does not exist on the website.
    elif response_from_website.status_code == 404:
        if full_output == True:
            print(f"{webpage_url} - does not exist in the website.\n")
        return False
    # any other status code is a private case, so the script prints the unusual received status code.
    else:
        if full_output == True:
            print(f"Recieved the next status code: {response_from_website.status_code} for the file: {webpage_url}.\n")
        return False
    

def main():
    # for displaying statistics in the end of the web fuzzing.
    existing_pages = 0
    checked_pages = 0

    # check with the user how to display the output of the script - only existing pages, or both existing and non existing.
    choice = input("Would you like to see also the non existing pages found? enter y/n: ")
    if choice == "y":
        full_output = True
    elif choice == "n":
        full_output = False
    else:
        print(f"no such option {choice}, displaying only existing pages found.")
        full_output = False
    print("\nScanning the website:", WEBSITE_URL, "\n\n")
    
    # open the .txt file containing the names of the possible web pages.
    try:
        webpages_file = open(POSSIBLE_WEBPAGES_FILE, "r")
    # handle a case of error while trying to open the .txt file.
    except:
        print(f"could not open the file: {POSSIBLE_WEBPAGES_FILE}.\nIf the file exists in different directory, please move it - this file must be with the script in the same directory (the script using relative path).\n")
    # if the file was opened successfully.
    else:
        # iterate over each name (line) in the file.
        for name in webpages_file.readlines():
            # check the name is valid.
            if name!="":
                if name[-1]=="\n":
                    name = name[:-1]
                # if the name is valid, call check_possible_webpage() in order to see if this page truly exists on the website.
                is_exists = check_webpage_name(name, full_output)
                checked_pages += 1
                if is_exists == True:
                    existing_pages += 1
        # close the .txt file after finishing it's role.
        webpages_file.close()
        print(f"\nfound {existing_pages} existing pages from total of {checked_pages} pages checked by the script.")

if __name__=="__main__":
    main()
