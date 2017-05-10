import cv2


class VideoCapture(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.last_frame = None
        pass

    def start(self):
        if not self.cap.isOpened():
            self.cap.open()

        while self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret:
                frame = cv2.flip(frame, 1)

                if self.last_frame is None:
                    new_frame = frame
                    self.last_frame = frame
                else:
                    new_frame = self.last_frame + frame
                    self.last_frame = frame

                # print(frame)

                # Applying edge detectors
                # frame = cv2.Laplacian(frame, cv2.CV_64F)
                # frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=1)
                # frame = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=1)

                cv2.imshow('frame', new_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    def release(self):
        """
        Release the capture and destroy all windows
        :return:
        """
        self.cap.release()
        cv2.destroyAllWindows()
