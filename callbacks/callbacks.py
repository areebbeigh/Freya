"""
Callback functions for voice commands - the real thing! And also a few other supporting functions

   Copyright 2016 Areeb Beigh

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import random
import feedparser
import time
import webbrowser
from urllib.parse import urlencode

import winspeech

from utils import configreader
from utils import volume
from utils.htmlparsers import NewsFeedParser

BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOLUME_RANGE = volume.get_volume_range()
MIN_VOLUME = VOLUME_RANGE[0]
MAX_VOLUME = VOLUME_RANGE[1]

preferences = configreader.get_preferences()
title = preferences.get_user_title()
previous_volume = None


def _get_all_files(directory, extensions):
    """
    Returns a list of all the files from a directory and it's
    sub-directories with a specific extension

    Parameters:
            directory:
                The directory to scan.

            extensions:
                A list containing the file extensions
                to scan for.
                Example: [".png", ".jpg"]
     """

    files = []

    for file in os.listdir(directory):
        file = os.path.join(directory, file)
        if os.path.isdir(file):
            files.extend(_get_all_files(file, extensions))
        elif os.path.splitext(file)[1].lower() in extensions:
            files.append(file)

    return files


def _get_positive_response():
    """ Returns a random string with a positive response """
    i = random.randint(0, 5 * 3)

    if i <= 5:
        response = "sure thing,"
    elif i <= 10:
        response = "alright,"
    else:
        response = "ok,"

    return response


def respond(phrase, prepend_positive_response=False, override_subtitle=False, say_wait=False):
    """
    Call this method to make Freya respond

    Parameters:
            phrase: The phrase to say.
            prepend_positive_response: A boolean denoting whether or not to prepend a positive response to the phrase. False by default.
            override_subtitle: If true the subtitle will be printed not matter what the preference is set to. Use it wisely.
            say_wait: Will use the customized winspeech module's say_wait() method instead of say()
    """
    if prepend_positive_response:
        phrase = _get_positive_response() + " " + phrase
    phrase = phrase.lower().capitalize()  # Fix stuff
    if preferences.get_print_subtitle():
        print("Freya: " + phrase + "\n")
    if say_wait:
        winspeech.say_wait(phrase)
        return
    winspeech.say(phrase)


def default_listener(input_phrase, listener):
    """
    Default callback for Freya, this will should mostly contain interactive speech responses
    This also calls other listeners for variable commands with variable inputs
    e.g
        "lookup <some phrase>" will launch the search_engine callback
    """

    # Very crude at the moment
    input_phrase = input_phrase.lower()
    #print("DEBUG:", input_phrase)

    responses = {
        ("hey freya", "hello freya", "good evening freya", "good morning freya"): ("hello " + title,),
        ("freya",): ("yes {}?".format(title),),
    }

    redirect_callbacks = {
        ("lookup", "google"): web_search,
        # ("open", "freya open"): open_website,
    }

    for phrase_list in redirect_callbacks.keys():
        for phrase_ in phrase_list:
            if phrase_ in input_phrase:
                # Remove the trigger phrase from the input_phrase for further operation
                operate_on = input_phrase.replace(phrase_, "").strip()
                if operate_on:
                    redirect_callbacks[phrase_list](operate_on)
                    return

    default_response = "I couldn't understand you, please try again"
    response = None

    for phrase_list in responses.keys():
        for phrase_ in phrase_list:
            if input_phrase == phrase_:
                response = random.choice(responses[phrase_list])

    if not response and preferences.get_trigger_keyword() in input_phrase:
        respond(default_response)
    if response:
        respond(response)


def stop_talking(p, l):
    winspeech.stop_talking()
    respond(_get_positive_response())


def web_search(phrase):
    """ Simple Google lookup opened in the default browser """
    respond("looking up " + phrase)
    # Simple google lookup
    webbrowser.open("https://google.com/search?" + urlencode({"q": phrase}))


def play_music(p, l):
    """ Plays music """
    respond("playing music", prepend_positive_response=True)
    playlist = os.path.join(BASE_DIRECTORY, 'playlist.m3u')

    extensions = [
        ".mp3",
        ".m4a",
        ".ogg",
        ".flac",
    ]

    music_files = _get_all_files(preferences.get_music_dir(), extensions)

    with open(playlist, 'w') as f:
        for file in music_files:
            f.write(file + "\n")

    os.startfile(playlist)


def open_website(p, l):
    print("Open website")


def reduce_volume(p, l):
    """ Reduces the system master volume """
    current_volume = volume.get_current_volume()

    if current_volume > 0 or current_volume == 0:
        new_volume = -15  # If the volume is full then we reduce it by ~ half, just my personal preference
    elif current_volume < 0:
        new_volume = current_volume - 5

    if current_volume == MIN_VOLUME:
        return

    if new_volume > MAX_VOLUME:
        new_volume = MAX_VOLUME
    elif new_volume < MIN_VOLUME:
        new_volume = MIN_VOLUME

    print("Current volume:", current_volume)
    print("New volume:", new_volume)

    volume.set_volume(new_volume)


def increase_volume(p, l):
    """ Increases the master volume """
    current_volume = volume.get_current_volume()

    if current_volume - MIN_VOLUME < 2:
        new_volume = -15  # If the volume is very low then we increase it by ~ half, just my personal preference
    elif current_volume < MAX_VOLUME:
        new_volume = current_volume + 5

    if current_volume == MAX_VOLUME:
        return

    if new_volume > MAX_VOLUME:
        new_volume = MAX_VOLUME
    elif new_volume < MIN_VOLUME:
        new_volume = MIN_VOLUME

    print("Current volume:", current_volume)
    print("New volume:", new_volume)

    volume.set_volume(new_volume)


def mute_pc(p, l):
    """ Sets the system volume to the minimum """
    global previous_volume
    respond("PC muted", say_wait=True)
    previous_volume = volume.get_current_volume()
    volume.set_volume(volume.get_volume_range()[0])


def unmute_pc(p, l):
    """ Restores the previous volume (if any) else just set it to -25 """
    m = "PC un-muted"
    if previous_volume and previous_volume > volume.get_volume_range()[0]:
        volume.set_volume(previous_volume)
        respond(m)
        return

    volume.set_volume(-25)
    respond(m)


def say_time(p, l):
    """ Says the current time """
    respond("It's " + time.strftime("%I:%M %p"))


def newscaster(p, l):
    """ Dictate the latest news (which are essentially entries in the RSS feed) """
    respond("fetching news", prepend_positive_response=True)
    feeds = [feedparser.parse(url) for url in preferences.get_news_feed_urls()]
    counter = 1

    for feed in feeds:
        for entry in feed.entries:
            data = []
            parser = NewsFeedParser(data)
            try:
                description = entry.description
            except AttributeError:
                description = "None given"
            parser.feed(description)
            news = "News #" + str(counter) + ": title: " + entry.title + ". description: " + " ".join(data)
            respond(news, override_subtitle=True)
            counter += 1
