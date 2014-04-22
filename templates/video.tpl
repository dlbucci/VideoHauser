<!DOCTYPE html>
<html>
  <head>
    <title>VideoHauser</title>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="/favicon.png">
    
    <style type="text/css">
      * {
        display: block;
        margin: 0;
        padding: 0;
      }
      
      body {
        background: #000;
      }
      
      #video-wrapper {
        /** set this to 28px for an always-on control bar **/
        bottom: 28px;
        left: 0;
        position: fixed;
        top: 0;
        right: 0;
        transition: bottom .3s;
      }
      
      #video-player-wrapper:hover > #video-wrapper {
        bottom: 28px;
      }
      
      video {
        height: 100%;
        left: 0;
        position: absolute;
        top: 0;
        width: 100%;
      }
      
      #control-wrapper {
        background: #f90;
        /** set this to 0 for an always-on control bar **/
        bottom: 0px;
        height: 28px;
        left: 0;
        padding: 0;
        position: fixed;
        right: 0;
        transition: bottom .3s;
      }
      
      #video-player-wrapper:hover > #control-wrapper {
        bottom: 0;
      }
      
      button {
        background: none;
        border: none;
        display: block;
        height: 28px;
        margin: 0;
        padding: 0;
        position: absolute;
        top: 0;
        width: 28px;
      }
      
      button:hover {
        background: rgba(255, 255, 255, .5);
      }
      
      button:active {
        background: rgba(0, 0, 0, .5);
      }
      
      div.button-svg-wrapper {
        top: 0;
        left: 0;
        margin: 0;
        padding: 0;
        position: absolute;
        height: 28px;
        width: 28px;
        z-index: 20;
      }
      
      #play-button {
        left: 0;
      }
      
      #sound-button {
        left: 28px;
      }
      
      #time-bar-wrapper {
        background: #c60;
        border: 10px solid #f90;
        display: block;
        float: left;
        margin: 0;
        padding: 0;
        position: absolute;
        left: 56px;
        right: 140px;
        top: 0;
        height: 8px;
      }
      #time-bar-seeker {
        height: 12px;
        left: 0;
        margin: -2px 0 0 -6px;
        position: absolute;
        top: 0;
        width: 12px;
      }
      #time-bar-seeker > svg {
        overflow: visible;
      }
      
      #time-text {
        font-family: sans-serif;
        font-weight: bold;
        position: absolute;
        line-height: 28px;
        bottom: 0;
        right: 28px;
        text-align: center;
        width: 112px;
      }
      
      #size-button {
        right: 0;
      }
    </style>
  </head>
  
  <body>
    <div id="video-player-wrapper">
      <div id="video-wrapper">
        <video id="player" src="{{ video_path }}" type="video/webm" preload="none"></video>
      </div>

      <div id="control-wrapper">
        <button type="button" id="play-button" tabindex="-1">
          <div class="button-svg-wrapper">
            <svg width="100%" height="100%" viewBox="0 0 14 14">
              <polygon points="2,2 12,7 2,12" fill="#000000" />
            </svg>
          </div>
        </button>

        <button type="button" id="sound-button" tabindex="-1">
          <div class="button-svg-wrapper">
            <svg width="100%" height="100%" viewBox="0 0 14 14">
              <polygon points="2,5 7,5 7,9 2,9" fill="#000000" />
              <path d="M 5 7 L 10 2
                       A 7 7, 90, 0, 1, 10 12
                       L 5 7 z" fill="#000000" />
            </svg>
          </div>
        </button>

        <div id="time-bar-wrapper">
          <svg width="100%" height="100%" viewBox="0 0 100 1" preserveAspectRatio="none">
            <rect id="load-bar" x="0" y="0" width="0" height="1" fill="#666666"></rect>
            <rect id="time-bar" x="0" y="0" width="0" height="1" fill="#000000"></rect>
          </svg>
          <div id="time-bar-seeker">
            <svg width="100%" height="100%" viewBox="0 0 6 6">
              <circle cx="3" cy="3" r="3" fill="#f90" stroke="#fff" stroke-width="1"></circle>
            </svg>
          </div>
        </div>

        <div id="time-text">0:00 / 0:00</div>
        
        <button type="button" id="size-button" tabindex="-1">
          <div class="button-svg-wrapper">
            <svg width="100%" height="100%" viewBox="0 0 14 14">
              <polygon points="2,2 6,2 5,3 7,5 9,3 8,2 12,2 12,6 11,5 9,7 11,9 12,8 12,12 8,12 9,11 7,9 5,11 6,12 2,12 2,8 3,9 5,7 3,5 2,6"
                       fill="#000000" />
            </svg>
          </div>
        </button>
      </div>
    </div>
    
    <script id="play-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,2 12,7 2,12" fill="#000000" />
        </svg>
      </div>
    </script>
    
    <script id="pause-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,2 6,2 6,12 2,12" fill="#000000" />
          <polygon points="8,2 12,2 12,12 8,12" fill="#000000" />
        </svg>
      </div>
    </script>
    
    <script id="sound-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,5 7,5 7,9 2,9" fill="#000000" />
          <path d="M 5 7 L 10 2
                   A 7 7, 90, 0, 1, 10 12
                   L 5 7 z" fill="#000000" />
        </svg>
      </div>
    </script>
    
    <script id="mute-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,5 7,5 7,9 2,9" fill="#000000" />
          <path d="M 5 7 L 10 2
                   A 7 7, 90, 0, 1, 10 12
                   L 5 7 z" fill="#000000" />
          <polygon points="2,4 4,2 12,10 10,12" fill="#ff0000" />
          <polygon points="2,10 10,2 12,4 4,12" fill="#ff0000" />
        </svg>
      </div>
    </script>
    
    <script id="expand-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,2 6,2 5,3 7,5 9,3 8,2 12,2 12,6 11,5 9,7 11,9 12,8 12,12 8,12 9,11 7,9 5,11 6,12 2,12 2,8 3,9 5,7 3,5 2,6"
                   fill="#000000" />
        </svg>
      </div>
    </script>
    
    <script id="collapse-svg" type="text/x-template">
      <div class="button-svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 14 14">
          <polygon points="2,4 4,2 5,3 6,2 6,6 2,6 3,5" fill="#000000" />
          <polygon points="10,2 12,4 11,5 12,6 8,6 8,2 9,3" fill="#000000" />
          <polygon points="12,10 10,12 9,11 8,12 8,8 12,8 11,9" fill="#000000" />
          <polygon points="2,10 3,9 2,8 6,8 6,12 5,11 4,12" fill="#000000" />
        </svg>
      </div>
    </script>
    
    <script type="text/javascript" src="/scripts/video.js"></script>
  </body>
</html>
