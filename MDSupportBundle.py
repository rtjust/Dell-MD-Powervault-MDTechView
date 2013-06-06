from MELEvent import MELEvent

class MDSupportBundle(object):
    """Represents an MD support bundle directory and the files within"""
    def __init__(self, bundle_path):
        self.bundle_path = bundle_path
        self.storage_array_profile_path = bundle_path + r'/storageArrayProfile.txt'
        self.major_event_log_path = bundle_path + r'/majorEventLog.txt'
        self.recovery_guru_path = bundle_path + r'/recoveryGuruProcedures.html'
        self.state_capture_data_path = bundle_path + r'/stateCaptureData.txt'
        self.iscsi_sessions_path = bundle_path + r'/iscsiSessionConnections.txt'
        self.parsed_mel = self.parse_mel()

    def get_storage_array_profile(self):
        # New comment, test
        # Load storageArrayProfile into memory and return its contents
        try:
            with open(self.storage_array_profile_path, 'r') as storage_array_profile:
                temp = ''
                for line in storage_array_profile:
                    temp += line
                return temp
        except IOError:
            return 'Storage array profile file doesn\'t exist'
    
    def get_major_event_log(self):
        try:
            with open(self.major_event_log_path, 'r') as major_event_log:
                temp = ''
                for line in major_event_log:
                    temp += line
                return temp
        except IOError:
            return 'Major event log file doesn\'t exist.'

    def get_state_capture_data(self):
        try:
            with open(self.state_capture_data_path, 'r') as state_capture_date:
                temp = ''
                for line in state_capture_date:
                    temp += line
                return temp
        except IOError:
            return 'State capture data file doesn\'t exist.'

    def get_iscsi_sessions(self):
        try:
            with open(self.iscsi_sessions_path, 'r') as iscsi_sessions:
                temp = ''
                for line in iscsi_sessions:
                    temp += line
                return temp
        except IOError:
            return 'iSCSI Sessions file doesn\'t exist.'

    def get_parsed_mel(self):
        pass

    def parse_mel(self):
        mel_event_list = []
        test_line = '1'
        try:
            with open(self.major_event_log_path, 'r') as mel_file:
                while test_line:
                    event = MELEvent()
                    if test_line == '1':
                        event.date_time = mel_file.readline()[11:]
                    else:
                        event.date_time = test_line[11:]
 
                    event.sequence_number = mel_file.readline()[17:]
                    event.event_type = mel_file.readline()[12:]
                    event.event_category = mel_file.readline()[16:]
                    event.priority = mel_file.readline()[10:]
                    test_line = mel_file.readline()

                    if test_line.startswith('E'):
                        event.event_needs_attn = test_line[23:]
                        event.event_send_alert = mel_file.readline()[18:]
                        event.event_visibility = mel_file.readline()[18:]
                        event.description = mel_file.readline()[13:]
                    else:
                        event.description = test_line[13:]
                    
                    event.event_specific_codes = mel_file.readline()[22:]
                    event.component_type = mel_file.readline()[16:]
                    event.component_location = mel_file.readline()[20:]
                    event.logged_by = mel_file.readline()[11:]
                    mel_file.readline() #throw away, blank line
                    mel_file.readline() #throw away, don't need 'Raw data'
                    test_line = mel_file.readline()
                    
                    while test_line != '\n':
                        if test_line == '':
                            break
                        event.raw_data += test_line
                        test_line = mel_file.readline()

                    while test_line == '\n':
                        test_line = mel_file.readline()

                    mel_event_list.append(event)

                return mel_event_list   
        except IOError:
            return 'Major event log file doesn\'t exist.'
        


