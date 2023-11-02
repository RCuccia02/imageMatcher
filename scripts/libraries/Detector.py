import cv2
ORB_HARRIS_SCORE = 0
class Detector:
  def defineDetector(detectorName):
    if detectorName == "SIFT":
      detector = cv2.SIFT_create(
        nfeatures=0,
        nOctaveLayers=3,
        contrastThreshold=0.04,
        edgeThreshold=10,
        sigma=1.6
      )
    elif detectorName == "ORB":
      detector = cv2.ORB_create(
        nfeatures=19049,
        scaleFactor=1.2,
        nlevels=8,
        edgeThreshold=31,
        firstLevel=0,
        WTA_K=2,
        scoreType = ORB_HARRIS_SCORE,
        patchSize=31,
        fastThreshold=20
      )
    return detector