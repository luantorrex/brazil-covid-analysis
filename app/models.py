from enum import unique
from app import db
import enum
import json
from dataclasses import dataclass
from flask import jsonify
from sqlalchemy_utils import PhoneNumber, PasswordType



class EmploymentGenderEnum(enum.Enum):
    male = 'male'
    female = 'female'

@dataclass
class User(db.Model):
	#data class thing
	id: int
	full_name: str
	email: str
	password_hash: str
	address : str 
	gender: str

	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(PasswordType(
		schemes=[
		'pbkdf2_sha512',
		'md5_crypt'
		],
		deprecated=['md5_crypt']
	))
	address = db.Column(db.String(120), nullable=False)
	gender = db.Column(db.Enum(EmploymentGenderEnum), nullable=False)
	_phone_number = db.Column(db.Unicode(20))

	phone_number = db.composite(
		PhoneNumber,
		_phone_number,
    	)

	def __repr__(self):
	    return '<User {}>'.format(self.full_name)

@dataclass
class Instituicao(db.Model):
	id: int
	name: str
	email: str
	address : str 
	
	__tablename__ = 'instituicao'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	address = db.Column(db.String(120), nullable=False)

	def __repr__(self):
	    return '<Name {}>'.format(self.name)
