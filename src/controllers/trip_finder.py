from typing import Dict

class TripFinder:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository
    
    def find_trip_details(self, trip_id) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip: raise Exception("No such trip")
            
            return {
                "body": {
                    "trip":{
                        "id": trip[0],
                        "destination": trip[1],
                        "start_date": trip[2],
                        "end_date": trip[3],
                        "status": trip[6]  # 0: pending, 1: confirmed, 2: canceled, 3: completed
                    }
                },

                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message" : str(exception)},
                "status_code": 400
            }