#!/usr/bin/env python
import os, subprocess

def webm_extension(file_name):
  return '%s.webm' % (os.path.splitext(file_name)[0])

def webm(tmp_path, save_path, file_name):
  cmd0 = os.environ.get('OPENSHIFT_BUILD_DEPENDENCIES_DIR')
  if (cmd0):
    cmd0 = os.path.join(cmd0, 'ffmpeg')
  else:
    cmd0 = 'ffmpeg'
    
  input_file = os.path.join(tmp_path, file_name)
  output_file = os.path.join(save_path, webm_extension(file_name))
  
  cmd = [cmd0,
  '-i', input_file,
  '-acodec','libvorbis',
  '-ac','2',
  '-ab','96k',
  '-ar','44100',
  '-b:v','345k',
  '-s','640x360',
  output_file]

  try:
    print(' '.join(cmd))
    process = subprocess.Popen(cmd)
    process.wait()
  finally:
    os.remove(input_file)