## web_fuzzer.py:



### Web fuzzing as technique:



Web fuzzing is a technique used to map pages on websites. The ides is pretty simple - the script uses a list of names, and check for each name if there is a page with this name on the website. That way, the one who running the web fuzzing can learn what pages exist on the website. This technique is used many times by attackers, and therefore it is very important to know it. Although it's used by attackers, the idea of web fuzzing is not necessarily malicious, but only a tool for reconnaissance. Running web fuzzing on a website does not hurt the website (maybe just give it some struggle).



### The tool web_fuzzer.py:



web_fuzzer.py is a demonstration for web fuzzing tool. web_fuzzer.py uses the "web pages names.txt" file as a list of possible webpages names, and checks for each name in the text file if a webpage with that name exists. All the HTTP communication with the web server is done using the module requests.



By default, web_fuzzer.py maps github's website (www.github.com), but this can be changed by modifying the constant variable that holds the name of the website to map. Furthermore, names can be added or removed from "web pages names.txt" freely, just pay attention that each name has it's own line.





### WARNING:



This tool was written for **educational purposes only!** Any misuse of the tool is in your responsibility only, and considers a cyber crime. Please, use this tool for legitimate purposes:



- don't map too many webpages in order to avoid putting a load on the web server.
- run this script only on strong websites like GitHub.
- Do not, and i repeat - DO NOT use this tool as reconnaissance for a cyber attack. This is a crime and on your hands only.

