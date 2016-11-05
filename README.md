# Freya
Freya is a virtual assistant written in Python for Windows. It (She?) uses the Microsoft Speech API (SAPI) for speech recognition and synthesis. Why? Because I wanted her to work offline. I tried other speech recognition libraries like CMU Sphinx but they weren't so accurate. I went with SAPI because it is easy to use in Python (<a href="https://github.com/areebbeigh/winspeech">winspeech</a>) and the one awesome feature the Speech Recognition has is that you can "train" it to understand you better. So it's ideal for a personal assistant like Freya.

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
  }
}
```

So what the heck is that? We'll see it part by part, the configuration is in JSON. 

####Phrases
The `phrases` configuration goes like this:

[callback_method name]:[list of trigger phrases]. 

All the callback methods are defined in `callback.callback`.

The trigger phrases that begin with an asterisk `*` are triggered both independently and when the `TRIGGER_KEYWORD` is said before. For example in the configuration above the method `play_music()` will be triggered by both phrases "play music" and "freya play music".

**NOTE: Some of the in-built commands in the configuration require certain values to be defined in <a href="#preferences">preferences</a>.**

####Preferences
Here you can somewhat customize Freya.

<table>
<thead><th>Preference</th><th>Summary</th><th>Values</th></thead>
<tr><td>TRIGGER_KEYWORD</td> <td>Essentially the assistant's name.</td> <td>Any string</td></tr>
<tr><td>PRIND_COMMANDS_ON_START</td> <td>Whether to print a list of available commands on start.</td> <td>True/False</td>
<tr><td>PRIND_SUBTITLES</td> <td>Whether or not to print whatever Freya says.</td> <td>True/False</td>
<tr><td>GENDER</td> <td>Your gender.</td> <td>Male/Female</td>
<tr><td>MUSIC_DIRECTORY</td> <td>The directory you want to play music files from when play_music() is called.</td> <td>A valid directory</td>
<tr><td>NEWS_FEED</td> <td>Any feed online resource compatible with feedparser that'll be "casted" when newscaster() is called.</td> <td>Any feed resource</td>
</table>

###Training Microsoft Speech Recognition
Ok so you configured Freya and now you're ready to go! But wait if you haven't already trained Microsoft Speech Recognition you'll probably fail everytime you say a command to Freya. It's easy to train Microsoft Speech Recognition.

Here are a few tutorials:
<ul>
<li><a href="http://www.thewindowsclub.com/windows-speech-recognition-voice-training">Make Windows better understand your voice using Speech Recognition Voice Training</a></li>
<li><a href="http://www.howtogeek.com/177539/how-to-get-started-with-speech-recognition-on-windows-7-or-8/">How to Get Started With Speech Recognition on Windows 7 or 8</a> (Windows 10 as well)</li>
</ul>

###Adding Custom Commands
You can add custom commands to Freya, all you have to do is define a call back method in `callback.callback` and add it to the configuration like the rest.

##Contributing
Fork, code and PR, I'll be waiting!

##Additional Info
**Developers**: Areeb Beigh <areebbeigh@gmail.com>
**GitHub Repo:** https://github.com/areebbeigh/Freya
