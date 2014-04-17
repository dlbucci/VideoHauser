#!/usr/bin/env python
import subprocess

def webm_extension(file_name):
  return '%s.webm' % '.'.join(file_name.split('.')[:-1])

def webm(file_name):
  cmd = ['ffmpeg',
  '-i','%s' % file_name,
  '-acodec','libvorbis',
  '-ac','2',
  '-ab','96k',
  '-ar','44100',
  '-b','345k',
  '-s','360x640',
  '%s' % webm_extension(file_name)]

  print(' '.join(cmd))
  process = subprocess.Popen(cmd)
  process.wait()
  
