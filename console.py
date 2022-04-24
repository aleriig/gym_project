import pdb

from models.booking_list import Booking_list
import repositories.booking_list_repository as booking_list_repository

from models.sport_class import Sport_class
import repositories.sport_class_repository as sport_class_repository

from models.member import Member
import repositories.member_repository as member_repository

booking_list_repository.select_all()
sport_class_repository.select_all()
member_repository.select_all


member_1 = Member("Michael Robinson", 40, "4 Hannover Street", "0799678567")
member_repository.save(member_1)

member_2 = Member("Katie Perry", 26, "13 Princess Street", "089345234")
member_repository.save(member_2)

member_3 = Member("John Fogerty", 59, "9 Andrew Square", "0788578567")
member_repository.save(member_3)

member_4 = Member("Clare Daines", 36, "1 Princess Street", "0988575488")
member_repository.save(member_4)

member_5 = Member("Peter Smith", 18, "13 Royal Mile", "0832879142")
member_repository.save(member_5)

sport_class_1 = Sport_class("TRX", "24/04/2022", 20 )
sport_class_repository.save(sport_class_1)

sport_class_2 = Sport_class("Body-building", "24/04/2022", 60 )
sport_class_repository.save(sport_class_2)

sport_class_3 = Sport_class("HIIT", "28/04/2022", 20 )
sport_class_repository.save(sport_class_3)

sport_class_4 = Sport_class("Spinning", "28/04/2022", 45 )
sport_class_repository.save(sport_class_4)

sport_class_5 = Sport_class("Yoga", "01/05/2022", 50 )
sport_class_repository.save(sport_class_5)

booking_list_1 = Booking_list(member_2, sport_class_3)
booking_list_repository.save(booking_list_1)

booking_list_2 = Booking_list(member_5, sport_class_5)
booking_list_repository.save(booking_list_2)


