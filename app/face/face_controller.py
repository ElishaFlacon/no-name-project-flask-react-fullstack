# from app.encode.encode import PythonObjectEncoder, as_python_object
# from json import dumps, loads
from app.face.face_service import FaceService
import os


FS = FaceService()


class FaceController():
    @staticmethod
    def face_verify(pictures):
        try:
            # get pictures
            first_pic = pictures['first_pic']
            second_pic = pictures['second_pic']

            # comparing pictures
            result = FaceService.face_verify(
                f'{os.environ.get("UPLOAD_FOLDER_PATH")}/{first_pic}',
                f'{os.environ.get("UPLOAD_FOLDER_PATH")}/{second_pic}'
            )

            # encode so that there are no mistakes
            # result = dumps(result, cls=PythonObjectEncoder)
            # result = loads(result, object_hook=as_python_object)

            # тут напишу на русском, я не пендос все таки
            # переводим в бул потому что данные в верефиде имеют бул_
            # и их нельзя конвертировать в json
            return [bool(result['verified']), result['distance']]
        except Exception as e:
            print(e)
            raise Exception('bad request: 400')

    @staticmethod
    def find_person(picture):
        try:
            result = FaceService.find_person(
                f'{os.environ.get("UPLOAD_FOLDER_PATH")}/{picture}'
            )

            return result
        except Exception as e:
            print(e)
            raise Exception('bad request: 400')
