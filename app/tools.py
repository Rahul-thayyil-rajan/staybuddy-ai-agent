# app/tools.py

HOTELS_DB = {
    "Bangalore": [
        {"hotel_id": 1, "hotel_name": "Taj MG Road", "review_score": 8.7, "checkin": "14:00"},
        {"hotel_id": 2, "hotel_name": "ITC Gardenia", "review_score": 9.2, "checkin": "15:00"},
        {"hotel_id": 3, "hotel_name": "Treebo Trend Inn", "review_score": 7.5, "checkin": "12:00"},
        {"hotel_id": 4, "hotel_name": "OYO Indiranagar Stay", "review_score": 6.8, "checkin": "13:00"},
        {"hotel_id": 5, "hotel_name": "The Oberoi Bangalore", "review_score": 9.4, "checkin": "14:00"},
        {"hotel_id": 6, "hotel_name": "Bloomrooms Whitefield", "review_score": 8.1, "checkin": "13:00"},
        {"hotel_id": 7, "hotel_name": "Zostel Bangalore", "review_score": 7.9, "checkin": "12:00"},
    ],

    "Chennai": [
        {"hotel_id": 8, "hotel_name": "Taj Coromandel", "review_score": 9.0, "checkin": "14:00"},
        {"hotel_id": 9, "hotel_name": "The Leela Palace Chennai", "review_score": 9.5, "checkin": "15:00"},
        {"hotel_id": 10, "hotel_name": "Radisson Blu Chennai", "review_score": 8.3, "checkin": "14:00"},
        {"hotel_id": 11, "hotel_name": "FabHotel Prime", "review_score": 7.2, "checkin": "12:00"},
        {"hotel_id": 12, "hotel_name": "OYO T Nagar Stay", "review_score": 6.5, "checkin": "13:00"},
        {"hotel_id": 13, "hotel_name": "Trident Chennai", "review_score": 8.8, "checkin": "14:00"},
        {"hotel_id": 14, "hotel_name": "The Residency Towers", "review_score": 8.0, "checkin": "13:00"},
    ],

    "Hyderabad": [
        {"hotel_id": 15, "hotel_name": "Taj Krishna", "review_score": 8.8, "checkin": "14:00"},
        {"hotel_id": 16, "hotel_name": "ITC Kohenur", "review_score": 9.1, "checkin": "15:00"},
        {"hotel_id": 17, "hotel_name": "Treebo Elite", "review_score": 7.4, "checkin": "12:00"},
        {"hotel_id": 18, "hotel_name": "OYO Banjara Hills", "review_score": 6.7, "checkin": "13:00"},
        {"hotel_id": 19, "hotel_name": "Novotel Hyderabad", "review_score": 8.5, "checkin": "14:00"},
    ],

    "Mumbai": [
        {"hotel_id": 20, "hotel_name": "The Taj Mahal Palace", "review_score": 9.6, "checkin": "14:00"},
        {"hotel_id": 21, "hotel_name": "Trident Nariman Point", "review_score": 9.1, "checkin": "14:00"},
        {"hotel_id": 22, "hotel_name": "The Lalit Mumbai", "review_score": 8.4, "checkin": "15:00"},
        {"hotel_id": 23, "hotel_name": "OYO Andheri Stay", "review_score": 6.4, "checkin": "12:00"},
        {"hotel_id": 24, "hotel_name": "Zostel Mumbai", "review_score": 7.8, "checkin": "11:00"},
    ],

    "Delhi": [
        {"hotel_id": 25, "hotel_name": "The Leela Palace Delhi", "review_score": 9.5, "checkin": "14:00"},
        {"hotel_id": 26, "hotel_name": "ITC Maurya", "review_score": 9.3, "checkin": "15:00"},
        {"hotel_id": 27, "hotel_name": "Radisson Blu Dwarka", "review_score": 8.2, "checkin": "14:00"},
        {"hotel_id": 28, "hotel_name": "FabHotel Connaught Place", "review_score": 7.3, "checkin": "12:00"},
        {"hotel_id": 29, "hotel_name": "OYO Karol Bagh Stay", "review_score": 6.6, "checkin": "13:00"},
    ]
}


def search_hotels(city):
    city = city.title()
    return HOTELS_DB.get(city, [])


def get_checkin(hotel_id):
    for hotels in HOTELS_DB.values():
        for h in hotels:
            if h["hotel_id"] == hotel_id:
                return h.get("checkin", "14:00")
    return "14:00"