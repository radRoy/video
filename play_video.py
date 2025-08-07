import cv2
import argparse
import sys

def play_video(filename, loop=False):
    cap = cv2.VideoCapture(filename)

    if not cap.isOpened():
        print(f"Error: Cannot open video file '{filename}'")
        sys.exit(1)

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # rewind to start
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video Playback (press Q to exit)', frame)

            if cv2.waitKey(250) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return

        if not loop:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play a .mp4 video using OpenCV.")
    parser.add_argument("filename", help="Path to the .mp4 video file.")
    parser.add_argument("--loop", action="store_true", help="Loop the video playback.")
    args = parser.parse_args()

    play_video(args.filename, args.loop)
