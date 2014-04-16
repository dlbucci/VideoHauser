<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Welcome to VideoHauser</title>
    <style>
      body {
        background: #333;
        font-family: sans-serif;
        font-weight: bold;
        margin: 0;
        padding: 0;
      }
      
      h1.site-title {
        background: #f90;
        box-shadow: 0 2px #c60;
        height: 42px;
        left: 0;
        line-height: 42px;
        margin: 0;
        padding: 0 0 0 50px;
        position: fixed;
        right: 0;
        top: 0;
      }
      .svg-wrapper {
        height: 42px;
        left: 4px;
        position: absolute;
        top: 0;
        width: 42px;
      }
      svg {
        display: block;
      }
      .site-title > .video {
        color: #ff0;
      }
      .site-title > .hauser {
        color: #fff;
      }
      
      .upload-form {
        background: #f90;
        border-radius: 4px;
        box-shadow: inset 0 2px #fc3,
                    inset 0 -2px #c60;
        color: #fff;
        margin: 200px auto 0;
        padding: 10px;
        width: 320px;
      }
      .upload-form-title {
        margin: 0 0 10px;
        padding: 0;
        text-align: center;
      }
      #file {
        background: #555;
        border-radius: 2px;
        box-shadow: inset 0 2px #444,
                    inset 0 -2px #666;
        box-sizing: border-box;
        margin: 10px 0;
        padding: 5px;
      }
      #submit {
        margin: 10px 0 0;
      }
      input[type="file"], input[type="submit"] {
        display: block;
        width: 100%;
      }
      
      footer {
        bottom: 0;
        color: #fff;
        left: 0;
        position: fixed;
        right: 0;
      }
      p.footer-text {
        margin: 0;
        padding: .2em .5em;
      }
    </style>
  </head>
  <body>
    <h1 class="site-title">
      <div class="svg-wrapper">
        <svg width="100%" height="100%" viewBox="0 0 42 42">
          <polygon points="27,6 33,6 33,12 27,12"
                   fill="#cc6600" />
          <polygon points="3,18 12,9 30,9 39,18"
                   fill="#333333" />
          <polygon points="6,18 36,18 36,36 6,36"
                   fill="#cc6600" />
          <polygon points="12,21 21,27 12,33"
                   fill="#000000" />
          <polygon points="15,23 18,25 15,27"
                   fill="#ffffff" />
          <polygon points="21,21 24,21 24,33 21,33" 
                   fill="#000000" />
          <polygon points="27,21 30,21 30,33 27,33"
                   fill="#000000" />
          <polygon points="24,25.5 27,25.5 27,28.5 24,28.5"
                   fill="#ffffff" />
        </svg>
      </div>
      <span class="video">Video</span><span class="hauser">Hauser</span>
    </h1>
    <form action="upload" method="post" enctype="multipart/form-data">
      <div class="upload-form">
        <h2 class="upload-form-title">Upload Your Video</h2>
        <input type="file" name="video" id="file">
        <input type="submit" name="submit" id="submit" value="Submit">
      </div>
    </form>
    <footer><p class="footer-text">Copyright Team Pelicans 2014.</p></footer>
  </body>
</html>