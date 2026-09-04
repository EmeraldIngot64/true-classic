import numpy as np
import cv2
import argparse

# Finds the closest frame to `target_frame` in `video` and saves it to `output_frame` 

parser = argparse.ArgumentParser()
parser.add_argument("video")
parser.add_argument("target_frame")
parser.add_argument("output_frame")

args = parser.parse_args()

SCALED_WIDTH = int(1920/4)
SCALED_HEIGHT = int(1080/4)

def video_to_frames(path):
    cap = cv2.VideoCapture(path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (SCALED_WIDTH, SCALED_HEIGHT), interpolation=cv2.INTER_AREA)
        frames.append(frame)

    cap.release()

    return np.array(frames, dtype=np.float32)

def select_single_frame(path, index):
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, index)
    success, frame = cap.read()

    return frame


frames = video_to_frames(args.video)

def find_closest_frame(target_frame, all_frames):
    mse_per_frame = np.mean((all_frames - target_frame) ** 2, axis=(1, 2, 3))
    best_index = np.argmin(mse_per_frame)
    return best_index, mse_per_frame[best_index]

target_frame = cv2.cvtColor(cv2.imread(args.target_frame), cv2.COLOR_BGR2RGB)
target_frame = cv2.resize(target_frame, (SCALED_WIDTH, SCALED_HEIGHT), interpolation=cv2.INTER_AREA)
target_frame = target_frame.astype(np.float32)

best_index, similarity = find_closest_frame(target_frame, frames)
print(best_index)


match_image = select_single_frame(args.video, best_index)
cv2.imwrite(args.output_frame, match_image)

