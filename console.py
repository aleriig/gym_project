import pdb

from models.sport_class import Sport_class
import repositories.sport_class_repository as sport_class_repository

from models.member import Member
import repositories.member_repository as member_repository

member_1 = Member("Michael Robinson", 40, "4 Hannover Street", "0799678567")

sport_class_1 = Sport_class("TRX", "24/04/2022", 20 )