(function (doc) {

/** Load the player and the actual video element **/
var player = doc.getElementById("video-player-wrapper"),
    video = doc.getElementById("player"),
    
/** Load Player Parts **/
    play_button = doc.getElementById("play-button"),
    mute_button = doc.getElementById("sound-button"),
    size_button = doc.getElementById("size-button"),
    load_bar = doc.getElementById("load-bar"),
    time_bar = doc.getElementById("time-bar"),
    time_text = doc.getElementById("time-text"),
    
/** Load SVG for player icons **/
    play_svg_html = doc.getElementById("play-svg").innerHTML,
    pause_svg_html = doc.getElementById("pause-svg").innerHTML,
    sound_svg_html = doc.getElementById("sound-svg").innerHTML,
    mute_svg_html = doc.getElementById("mute-svg").innerHTML,
    expand_svg_html = doc.getElementById("expand-svg").innerHTML,
    collapse_svg_html = doc.getElementById("collapse-svg").innerHTML;

/**
 * called when the play button is clicked.  Either pauses or plays the video.
 *
 * @param  e  the event passed to the click handler
 **/
function PlayButton(e) {
  if (video.paused) {
    play_button.innerHTML = pause_svg_html;
    video.play();
  } else {
    play_button.innerHTML = play_svg_html;
    video.pause();
  }
}
  
/**
 * called when the mutes button is clicked.  Either mutes or unmutes the video.
 *
 * @param  e  the event passed to the click handler
 **/
function MuteButton(e) {
  if (video.muted) {
    mute_button.innerHTML = sound_svg_html;
    video.muted = false;
  } else {
    mute_button.innerHTML = mute_svg_html;
    video.muted = true;
  }
}
  
/**
 * called when the size button is clicked.  Either enters or exits full screen.
 * Pretty sure this works exclusively with Firefox.  Damn browser prefixes.
 *
 * @param  e  the event passed to the click handler
 **/
function SizeButton(e) {
  if (!doc.mozFullScreenElement) {
    size_button.innerHTML = collapse_svg_html;
    player.mozRequestFullScreen();
  } else {
    size_button.innerHTML = expand_svg_html;
    doc.mozCancelFullScreen();
  }
}

/**
 * called when progress is made loading the video.
 *
 * param  e  the event passed to the handler
 **/
function onProgress(e) {
  var end = video.buffered.end(0),
      start = video.buffered.start(0);
  load_bar.setAttribute("width", ((end - start) / video.duration).toString());
}

/**
 * converts the given number of seconds to a time string with format "M:SS".
 * floors the number of seconds if it is a float.
 *
 * @param  t  the nummber of seconds to be converted
 *
 * @return  a time string with format "M:SS"
 **/
function toTimeString(t) {
  if (isNaN(t) || !t) {
    return "0:00";
  } else {
    var seconds = Math.floor(t % 60).toString();
    if (seconds.length == 1) seconds = "0" + seconds;
    return Math.floor(t / 60).toString() + ":" + seconds;
  }
}
  
/**
 * Called when the time of the video changes.  Updates the time when the
 * seconds value changes to prevent excessive redraws.
 *
 * @param  e  the event object passed to the handler
 **/
function onTimeUpdate(e) {
  var newTime = Math.floor(video.currentTime);
  if (newTime != timeInt) {
    timeInt = newTime;
    time_str = toTimeString(timeInt);
    time_text.innerHTML = time_str + dur_str;
    time_bar.setAttribute("width", (video.currentTime / video.duration).toString());
  }
}

/**
 * Called when the duration of the video changes.
 * Updates the duration text as appropriate.
 *
 * @param  e  the event object passed to the handler
 **/
function onDurationChange(e) {
  var newDuration = Math.floor(video.duration);
  if (newDuration != durInt) {
    durInt = newDuration;
    dur_str = " / " + toTimeString(durInt);
    time_text.innerHTML = time_str + dur_str;
    time_bar.setAttribute("width", (video.currentTime / video.duration).toString());
  }
}
  
/**
 * called when the video finishes playing
 **/
function onEnded(e) {
  play_button.innerHTML = play_svg_html;
  time_bar.setAttribute("width", "1");
}

/** Initialize the time stuff **/
var timeInt = Math.floor(video.currentTime),
    durInt = Math.floor(video.duration),
    time_str = toTimeString(video.currentTime), 
    dur_str = toTimeString(video.duration);

/**  Add the button event listeners **/
play_button.addEventListener("click", PlayButton, false);
mute_button.addEventListener("click", MuteButton, false);
size_button.addEventListener("click", SizeButton, false);
  
/**  Add the video event listeners **/
video.addEventListener("progress", onProgress, false);
video.addEventListener("timeupdate", onTimeUpdate, false);
video.addEventListener("durationchange", onDurationChange, false);
video.addEventListener("ended", onEnded, false);

})(document);