<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Welcome to VideoHauser</title>
    <style>
      body {
        background: #000;
        font-family: sans-serif;
        font-weight: bold;
        margin: 0;
        padding: 0;
      }
      
      h1.site-title {
        background: #333;
        box-shadow: inset 0 -2px #111;
        left: 0;
        margin: 0;
        padding: 0 .5em;
        position: fixed;
        right: 0;
        top: 0;
      }
      .site-title > .video {
        color: #ff0;
      }
      .site-title > .hauser {
        color: #fff;
      }
      
      .upload-form {
        background: #333;
        border-radius: 4px;
        box-shadow: inset 0 2px #555,
                    inset 0 -2px #111;
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
    <h1 class="site-title"><span class="video">Video</span><span class="hauser">Hauser</span></h1>
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