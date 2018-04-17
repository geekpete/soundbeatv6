from soundbeat6 import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Soundbeat6 normally
        """
        self.render_config_template(
            path=os.path.abspath(self.working_dir) + "/log/*"
        )

        soundbeat6_proc = self.start_beat()
        self.wait_until(lambda: self.log_contains("soundbeat6 is running"))
        exit_code = soundbeat6_proc.kill_and_wait()
        assert exit_code == 0
