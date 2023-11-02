import numpy as np
import cv2
import os
class FileManagerKPDS:
  def saveDS(savepath, imgName, des, method):
    path = os.path.join(savepath, 'descriptors', method, imgName)
    np.save(path, des)
    return

  def saveKP(savepath, imgName, kp, method):
    num_keypoints = len(kp)
    keypoint_array = np.zeros((num_keypoints, 7), dtype=np.float32)

    # Fill the NumPy array with SIFT keypoints
    for i, keypoint in enumerate(kp):
      keypoint_array[i, 0] = keypoint.pt[0]      # x-coordinate
      keypoint_array[i, 1] = keypoint.pt[1]      # y-coordinate
      keypoint_array[i, 2] = keypoint.size      # size
      keypoint_array[i, 3] = keypoint.angle     # angle
      keypoint_array[i, 4] = keypoint.response  # response
      keypoint_array[i, 5] = keypoint.octave    # octave
      keypoint_array[i, 6] = keypoint.class_id  # class_id
    
    path = os.path.join(savepath, 'keypoints', method, imgName)
    np.save(path, keypoint_array)
    return

  def loadDS(savepath, imgName, method):
    path = os.path.join(savepath, 'descriptors', method, imgName)
    des = np.load(path + '.npy')
    return des

  def loadKP(savepath, imgName, method):
    path = os.path.join(savepath, 'keypoints', method, imgName)
    keypoint_array = np.load(path + '.npy')
    keypoints = []

    for row in keypoint_array:
      keypoints.append(cv2.KeyPoint(x=row[0], y=row[1], size=row[2], angle=row[3],
                                    response=row[4], octave=int(row[5]), class_id=int(row[6])))
    return keypoints

