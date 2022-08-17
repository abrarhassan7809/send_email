import pymsgbox
import notify2
import timesched
from plyer import notification


class work_time:

    def message_is(self):
        notification.notify(
            title="Title is here",
            message="It's working time",
            # displaying time
            timeout=3
        )

    def start_time(self, time_is):
        s = timesched.Scheduler()
        # s.repeat(time_is, 1, work_time, 1)

        s.repeat_on_days('MTWTFss', time_is, 0, self.message_is)

        # pymsgbox.alert(f"This is a message box and start in {self.time_is}", title="Alarm")
        s.run()
