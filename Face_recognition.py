reachy = ReachySDK(host='127.0.0.1')

import face_recognition as fr
import cv2


def get_player_amount():
  video_capture = reachy.left_camera
  frame = video_capture.last_frame
  rgb_frame = frame[:, :, ::-1]
  face_locations = fr.face_locations(rgb_frame)
  return(len(face_locations))