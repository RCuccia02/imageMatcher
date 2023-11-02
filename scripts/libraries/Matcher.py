import cv2
import matplotlib.pyplot as plt
FLANN_INDEX_KDTREE = 1
FLANN_INDEX_LSH = 6
class Matcher:
  def getMatches(des1, des2, method):
    if(method == "SIFT"):
      index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    if(method == "ORB"):
      index_params = dict(algorithm = FLANN_INDEX_LSH, table_number = 6, key_size = 12, multi_probe_level = 1)
    search_params = dict(checks=50) # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2) 
    return matches

  def lowe(matches, ratio):
    matchesMask = [[0,0] for i in range(len(matches))]
    good = []
    for i, match in enumerate(matches):
      if len(match) >= 2:
        m, n = match
        if m.distance < ratio*n.distance:
          good.append(m)
          matchesMask[i]=[1,0]
      elif (len(match) == 1):
        good.append(match[0])
        matchesMask[i]=[1,0]
    return good, matchesMask

  def showMatches(img1,kp1,img2,kp2,matches, matchesMask):
    draw_params = dict(matchColor = (0,255,0),
      singlePointColor = (255,0,0),
      matchesMask = matchesMask,
      flags = cv2.DrawMatchesFlags_DEFAULT)
    # Enlarge cv2 plot
    plt.rcParams['figure.figsize'] = [16, 8]
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    plt.imshow(img3,)
    plt.show()

