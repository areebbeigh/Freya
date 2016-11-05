# Freya
Freya is a virtual assistant written in Python for Windows.

##Previews
**YouTube Demo:** Coming soon <br>
**YouTube Setup Tutorial**: Coming soon

##Dependencies
<ul>
<li><a href="https://pypi.python.org/pypi/winspeech">winspeech</a></li>
<li><a href="https://sourceforge.net/projects/pywin32/files/pywin32/">pywin32</a></li>
<li><a href="https://pypi.python.org/pypi/feedparser/5.2.1">feedparser</a></li>
</ul>

##Setup
Once you've isntalled all the dependencies above you should be able to run `freya.py` without any problems. You might want to change the
default configuration though.

###Configuration
Example config:
```
{
  "phrases": {
    "play_music": [
      "*play music",
      "*let's have some music"
    ],
    "say_time": [
      "*tell me the time",
      "*what's the time",
      "*what is the time"
    ],
    "mute_pc": [
      "freya mute"
    ],
    "unmute_pc": [
      "freya unmute"
    ],
    "reduce_volume": [
      "*reduce volume",
      "*volume down"
    ],
    "increase_volume": [
      "*increase volume",
      "*volume up"
    ],
    "newscaster": [
      "*news"
    ],
    "stop_talking": [
      "*stop talking"
    ]
  },

  "preferences": {
    "TRIGGER_KEYWORD": "freya",
    "PRINT_COMMANDS_ON_START": "True",
    "PRINT_SUBTITLES": "True",
    "GENDER": "male",
    "MUSIC_DIRECTORY": "C:\\Users\\Areeb\\Desktop\\Music",
    "NEWS_FEED": ["C:/Users/Areeb/Desktop/tech_feed.xml", "C:/Users/Areeb/Desktop/news_feed.xml"],
    "ZIPCODE": 190005
  }
}
```

So what the heck is that? We'll see it part by part, the configuration is in JSON. 

####Phrases
The `phrases` configuration goes like this:

[callback_method]:[list of trigger phrases]. 

All the callback methods are defined in `callback.callback`.

The trigger phrases that begin with an asterisk `*` are triggered both independently and when the `TRIGGER_KEYWORD` is said before. For example in the configuration above the method `play_music()` will be triggered by both phrases "play music" and "freya play music".

**NOTE: Some of the in-built commands in the configuration require certain values to be defined in <a href="#preferences">preferences</a>.**

###Adding Custom Commands
You can add custom commands to Freya, all you have to do is define a call back method in `callback.callback` and add it to the configuration like the rest.
