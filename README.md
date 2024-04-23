# Sololearn Bot
The Sololearn Bot is a python program used to farm bits and XP.  
Currently it can farm about 175 bits and over 350 xp every 10 minutes.

## Installation & Setup
Install the required dependencies:
```bash
python3 -m pip install -r requirements.txt
```
Be sure to put your username and password in `config.py`.  

> [!IMPORTANT]  
Before using this program, make sure you have started the introduction to python course, otherwise it will not work. It needs to be visible on your profile in the 'Courses Progress' section.

## Usage
After you have followed the previous steps, you can run the script with:
```bash
python3 main.py
```

## To do
- Add more reliable ways of verifying successful element interactions
- Check for the daily streak button presence after the lesson is complete
- Automatically add 'introduction to python' to courses in progress
- Replace selectors with more reliable ones
- Add tests