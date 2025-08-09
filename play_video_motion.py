import cv2
import argparse
import sys
import numpy as np

def play_video_motion(filename, loop=False, fps=30):

    # 8 bit colour depth per channel (0 to 255 pixel values)
    # shape of one frame (numpy.ndarray):
    #   (y, x, c) where y is height, x is width, c is channel (R,G,B probably),
    #   e.g.: <class 'numpy.ndarray'> (720, 1280, 3)
    cap = cv2.VideoCapture(filename)
    delay = 1000 // fps  # delay between frames in milliseconds

    if not cap.isOpened():
        print(f"Error: Cannot open video file '{filename}'")
        sys.exit(1)  # Python error code (program exits with 0 if it is completed)

    while True:
        i = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # rewind to start
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            print(type(frame), frame.shape)
            frame_rgb = np.full((720, 1280, 3), 128)
            frame_gray = np.full((720, 1280, 1), 128)
            frame_rgb = frame[:,:,1]

            if i > 0:
                #print(f"{type(ret), type(frame)}")
                frame_diff = frame - frame_previous
                #frame_diff = frame - frame_rgb_previous

                cv2.imshow('Motion Playback (press Q to exit)', frame_diff)

                if cv2.waitKey(delay=delay) & 0xFF == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    return
            i += 1
            frame_previous = frame
            #frame_rgb_previous = frame_rgb

        if not loop:
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Play the motion in an .mp4 video using OpenCV.")
    parser.add_argument("filename", help="Path to the .mp4 video file.")
    #parser.add_argument("fps", help="Set the speed of the video playback in frames per second.")
    parser.add_argument("--loop", action="store_true", help="Loop the video playback.")
    args = parser.parse_args()

    #play_video_motion(args.filename, args.fps, args.loop)
    play_video_motion(args.filename, args.loop)
