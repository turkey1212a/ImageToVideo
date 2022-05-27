import cv2
import glob
import numpy as	np
import sys

import utils

def image_to_video(img: np.ndarray, seconds: int, fpath: str):
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 30
    height, width = img.shape[:2]
    writer = cv2.VideoWriter(fpath, fmt, fps, (width, height))

    for second in range(seconds):
        for frame_no in range(fps):
            writer.write(img)
        print(f'{second} / {seconds}s')

    print('')
    writer.release()


def image_to_video_files(src_dir: str, dst_dir: str, seconds: int):
    file_list = glob.glob(f'{src_dir}/*')
    print(f'{len(file_list)} files')
    for file in file_list:
        print(f'{file}')
        ret = utils.is_image_file(file)
        if not ret:
            print(' : not image file')
            print('')
            continue
        dst_fname = f'{dst_dir}/{utils.filename_without_extention(file)}.mp4'
        print(f'-> {dst_fname}')
        img = cv2.imread(file)
        image_to_video(img, seconds, dst_fname)


if __name__ == '__main__':
    args = sys.argv
    src_dir = args[1]
    dst_dir = args[2]
    seconds = int(args[3])
    utils.makedir_if_absent(dst_dir)
    image_to_video_files(src_dir, dst_dir, seconds)
