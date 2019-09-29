#!/usr/bin/python3
from hashlib import sha256
from threading import Thread
import face_recognition


def getHash(image_filename):
	hashfcn = sha256()
	try:
		imagearray=face_recognition.api.load_image_file(image_filename)
		hashfcn.update(str(face_recognition.api.face_landmarks(imagearray, model='small')).encode('utf-8'))
		return hashfcn.hexdigest()
	except:
		return "-1"
