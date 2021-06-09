# Mainichi Kanji Kakunin

A tkinter based app that helps japanese learner to remember kanji

## How it works?
Based on my reading, people said that if we want to remember something we always need to look and read it. For japanese learner, kanji is one of the hardest part in learning japanese. It is because, japanese use 3 style of writing which is Hiragana, Katakana and Kanji. Kanji very important because, you will need to use it everyday in your life if you want to live at japan.

Nowadays, people always use the computer for online class and work from home, so This App will help user to see and read Kanji **EVERYDAY**.

And to gain more focus when looking and reading kanji, this app will 
**CLOSE OTHER WINDOW UNTIL YOU SOLVE THE QUIZ, YOUR FUKUSHU** 
except windows explorer(only this i know for now)

## Kanji Data

Arigatou, [davidluzgouveia/kanji-data: A JSON kanji dataset with updated JLPT levels and WaniKani information (github.com)](https://github.com/davidluzgouveia/kanji-data)
For sharing this json set of kanji.

> N5 to N1 JLPT level is available in this json dataset. Other kanji(Other thatn JLPT) also available


## How To Use

 - This app will be put in STARTUP FOLDER, to make sure when user open the computer, it will auto open
 - If you want to make it into .exe file by using pyinstaller or anything **please make sure**
	 - 1. To change exe_file at inStartup function to your_exe_name
	 - 2. Please make sure the file name is same 
	 
-Because of OptionPane still not done yet, to change setting of This App , you need to edit config file that contain mainichi_count(how many kanji you want to learn per day), jlpt and strokes by yourselves
	
	- you can change it based on how you want
	- if you want random strokes, please keep the value at 0
	- for now, you can put a range as value for strokes (**Done**)
	- generated kanji can be organize by jlpt level (**Done**)
	- no word examples(**Coming Soon**)

-And for your infomation, generated kanji always random based on jlpt and strokes

## Still Need An Update

 - [ ] **Organize kanji by learned and not**
 - [DONE] **Can choose range for strokes, jlpt and number of kanji per session**
 - [ ] **Star and Favourite feature for kanji**
 - [ ] **Study Mode**
 - [ ] **word examples**
 - [ ] **Make A pyinstaller instruction and icon **
**AND MORE**

***I will always update this app in the future. For any trouble or suggestion, please share with me
YOROSHIKU ONEGAISHIMASU***
