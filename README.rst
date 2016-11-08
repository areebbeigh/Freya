Freya
=====

Freya is a virtual assistant written in Python for Windows. 

I started working on Freya as a personal project (who doesn't want a Jarvis of his/her own??) and
currently it's only in its initial stages. It may not be as efficient as the other assistants
available out there such as W.I.L.L or Athena yet, but it "gets stuff done".

It (She?) uses the Microsoft Speech API (SAPI) for speech recognition and synthesis.
Why? Because I wanted her to work offline.
I tried other speech recognition libraries like CMU Sphinx but they weren't so accurate.
I went with SAPI because it is easy to use in Python
(`winspeech module <https://github.com/areebbeigh/winspeech>`_) and the one awesome feature Windows
Speech Recognition has is that you can "train" it to understand you better. So it's ideal for a
personal assistant like Freya.

Videos
------
| **YouTube Demo:** Pending
| **YouTube Setup Tutorial**: Pending

Dependencies
------------

- `winspeech <https://pypi.python.org/pypi/winspeech>`_
- `pywin32 <https://sourceforge.net/projects/pywin32/files/pywin32/>`_
- `feedparser <https://pypi.python.org/pypi/feedparser/5.2.1>`_
- `comtypes <http://pypi.python.org/pypi/comtypes>`_

Setup
-----

Once you've installed all the dependencies above you should be able to run ``freya.py`` without any
problems. You might want to change the default configuration though.

-------------
Configuration
-------------

Example config:
::

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
        "NEWS_FEED": ["http://rss.cnn.com/rss/edition.rss", "http://rss.cnn.com/rss/edition_world.rss"],
      }
    }

So what the heck is that? We'll see it part by part, the configuration is in JSON. 

-------
Phrases
-------

The ``phrases`` configuration goes like this:

[callback_method name]:[list of trigger phrases]. 

All the callback methods are defined in ``callbacks.callbacks``.

The trigger phrases that begin with an asterisk `*` are triggered both independently and when the ``TRIGGER_KEYWORD`` is said before.
For example in the configuration above the method ``play_music()`` will be triggered by both phrases "play music" and "freya play music".

**NOTE: Some of the in-built commands in the configuration require certain values to be defined in preferences.**

-----------
Preferences
-----------

Here you can somewhat customize Freya.


+--------------------------+--------------------------------------------+------------------------+
| Preference               | Summary                                    | Values                 |
+==========================+============================================+========================+
| TRIGGER_KEYWORD          | Essentially the assistant's name.          | Any string             |
+--------------------------+--------------------------------------------+------------------------+
| PRIND_COMMANDS_ON_START  |  Whether to print a list of available      | True/False             |
|                          |  commands on start.                        |                        |
+--------------------------+--------------------------------------------+------------------------+
| PRIND_SUBTITLES          | Whether or not to print whatever Freya     | True/False             |
|                          | says.                                      |                        |
+--------------------------+--------------------------------------------+------------------------+
| GENDER                   | Your gender.                               | Male/Female            |
+--------------------------+--------------------------------------------+------------------------+
| GENDER                   | Your gender.                               | Male/Female            |
+--------------------------+--------------------------------------------+------------------------+
| MUSIC_DIRECTORY          | The directory you want to play music files | A valid directory      |
|                          | from.                                      |                        |
+--------------------------+--------------------------------------------+------------------------+
| NEWS_FEED                | Any feed online resource compatible with   | Any feed resource      |
|                          | feedparser that'll be read aloud when      |                        |
|                          | newscaster() is called.                    |                        |
+--------------------------+--------------------------------------------+------------------------+

-------------------------------------
Training Microsoft Speech Recognition
-------------------------------------

Ok so you configured Freya and now you're ready to go! But wait if you haven't already trained Microsoft Speech Recognition Freya will probably fail everytime you say a command to her. It's easy to train Microsoft Speech Recognition.

Here are a few tutorials:

- `Make Windows better understand your voice using Speech Recognition Voice Training: <http://www.thewindowsclub.com/windows-speech-recognition-voice-training>`_
- `How to Get Started With Speech Recognition on Windows 7 or 8 (Windows 10 as well): <http://www.howtogeek.com/177539/how-to-get-started-with-speech-recognition-on-windows-7-or-8/>`_

---------------------
The Speech Dictionary
---------------------

Now you've setup Speech Recognition. Unless computers love your accent, you'll have to add a few words to your Windows **Speech Dictionary**. Sometimes when you say a phrase Speech Recognition doesn't recognize it correctly even after training it. For this you can record a pronunciation of that word in the Speech Dictionary.

Here's how I do it:

1. Open Speech Recognition.
#. Say "Open Speech Dictionary".
#. A window should pop up with a few options, select "Add a new word".
#. Type in the word and press Next.
#. Check "Record a pronunciation on finish".
#. Record a pronunciation of the word.

----------------------
Adding Custom Commands
----------------------
You can add custom commands to Freya, all you have to do is define a call back method in
``callbacks.callbacks`` and add it to the configuration like the rest.

Let's add a commands "foo" and "foo bar" to Freya which result in the same action.

Every command executes a callback method in callbacks.callbacks and every callback method takes two argumets
(see `the winspeech documentation <https://pythonhosted.org/winspeech/>`_)

- phrase - The phrase that triggered the callback
- listener - A listener object

Most of the times you wont need to work with them so they're just dummies.

We'll call our callback ``bar``. We'll add this to ``callbacks.callbacks``:

::

    ...
    def bar(p, l):
      print("It works!")


Now we add the following to the ``phrases`` in ``config.json``:

::

    ...
    "bar": [
      "foo",
      "foo bar"
    ]

That's it. You added your first custom command to Freya :smile:.


Contributing
------------
Got something of your own to add? Found a bug? something to improve? or just a typo? -> Fork, code/correct and PR! I'll be waiting!

Additional Info
---------------
| **Developer**: Areeb Beigh <areebbeigh@gmail.com>
| **GitHub Repo:** https://github.com/areebbeigh/Freya
