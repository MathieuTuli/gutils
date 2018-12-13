'''UseOpenCV'''

import cv2
import os
import sys

from datetime import datetime
from Logger import Logger


class UseOpenCV():
    '''Interface for OpenCV in use cases I frequently have
    '''
    def __init__(self,
                 media_format: str='video',
                 source: str='webcam',
                 output_path: str='output.avi',
                 output_fps: float=20.0):
        '''Constructor
        @param media_format: str
            @default: video
            @option: video
            @option: photo
        @param source: str | video/photo source -> use 'cam?' for camera other than
            internal webcam
            @default: webcam
        @param output_path: str
            @default: output.avi
        @param output_fps: float
            @default: 20.0
        '''
        self.logger = Logger(logger_type='local',
                             loglevel='debug')

        self.logger.debug('Media Format: {}'.format(media_format))
        self.logger.debug('Source: {}'.format(source))

        if source == 'webcam':
            source = 0
        elif 'cam' in source:
            try:
                source = int(source.replace('cam', ''))
            except Exception as e:
                self.logger.debug("'cam?' formatting was incorrect due to {}".format(e))
        else:
            if not os.path.isfile(source):
                raise ValueError('{} is not a valid source'.format(source))

        if media_format == 'video':
            self.capture = cv2.VideoCapture(source)
            self.frame_dims = [int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                               int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))]
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_writer = cv2.VideoWriter('output.avi',
                                                fourcc,
                                                output_fps,
                                                (self.frame_dims[0],
                                                 self.frame_dims[1]))
        elif media_format == 'photo':
            pass
        else:
            raise ValueError("Media format is unknown")

    def show_image(self,
                   image: str,
                   from_path: bool=False) -> None:
        '''Display the image given by 'image_path'
        @param image: str | absolute image path
        @param from_path: bool
            @default: False
        '''
        try:
            if from_path:
                if not os.path.isfile(image):
                    raise ValueError("image is not a valid path")
                image = cv2.imread(image)
            cv2.imshow("image", image)
            key = cv2.waitKey(0)
            if key == 0xFF & ord("q"):
                sys.exit(0)
        finally:
            cv2.destroyAllWindows()

    def stream(self,
               save_video: bool=False) -> None:
        '''Start
        @param save_video: bool
            @default: False
        '''
        while True:
            start_time = datetime.now()
            r, frame = self.capture.read()
            if not r:
                self.close()
                break
            cv2.imshow('frame', frame)
            print("FPS: {}".format(1 / (datetime.now() - start_time).total_seconds()))
            if save_video:
                self.save_video(frame)
            key = cv2.waitKey(1)
            if key == 0xFF & ord("q"):
                self.close()
                break

    def save_video(self, frame) -> None:
        '''Write opencv frame to file
        @param frame: numpy.ndarray
        '''
        try:
            self.video_writer.write(frame)
        except Exception as e:
            self.logger.debug("Couldn't save video due to: {}'.format(e)")

    def close(self):
        '''Deconstructor
        '''
        self.capture.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
