

class ValidationMixin:
    def _validate_game_time(self,session_id: str, start_time: Optional[str], end_time: Optional[str]):
        if start_time:
            start_time = get_date_time_obj(start_time)
        if end_time:
            end_time = get_date_time_obj(end_time)

        if start_time:
            if start_time <= utc_date_time_now():
                raise Exception("Invalid StartTime")

        if end_time and session_id:
            game_session = self.storage.get_game_session(session_id=session_id)
            if not start_time:
                start_time = game_session.start_time

            if end_time < start_time:
                raise Exception("Invalid Endtime")

        if start_time and end_time:
            if start_time >= end_time:
                raise Exception("Invalid session time")

