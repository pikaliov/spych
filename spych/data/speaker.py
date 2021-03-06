import enum


class Gender(enum.Enum):
    MALE = 'm'
    FEMALE = 'f'


class Speaker(object):
    SPEAKER_INFO_GENDER = 'gender'
    SPEAKER_INFO_SYNTHESIZED = 'synthesized'
    SPEAKER_INFO_SYNTHESIZER_VOICE = 'synthesizer_voice'
    SPEAKER_INFO_SYNTHESIZER_EFFECTS = 'synthesizer_effects'
    SPEAKER_INFO_SYNTHESIZER_TOOL = 'synthesizer_tool'
    SPEAKER_INFO_PART_FROM = 'part_from_speaker'

    def __init__(self, idx, gender=None):
        self.idx = idx

        if gender == 'm':
            gender = Gender.MALE
        elif gender == 'f':
            gender = Gender.FEMALE

        self.gender = gender

        self.is_synthesized = False
        self.synthesis_voice = None
        self.synthesis_effects = None
        self.synthesis_tool = None
        self.part_from_speaker = None

    def load_speaker_info_from_dict(self, speaker_info):
        if Speaker.SPEAKER_INFO_GENDER in speaker_info.keys():
            gender = speaker_info[Speaker.SPEAKER_INFO_GENDER]

            if gender == 'm':
                self.gender = Gender.MALE
            elif gender == 'f':
                self.gender = Gender.FEMALE

        if Speaker.SPEAKER_INFO_SYNTHESIZED in speaker_info.keys():
            self.is_synthesized = speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZED]

        if Speaker.SPEAKER_INFO_SYNTHESIZER_VOICE in speaker_info.keys():
            self.synthesis_voice = speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_VOICE]

        if Speaker.SPEAKER_INFO_SYNTHESIZER_EFFECTS in speaker_info.keys():
            self.synthesis_effects = speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_EFFECTS]

        if Speaker.SPEAKER_INFO_SYNTHESIZER_TOOL in speaker_info.keys():
            self.synthesis_tool = speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_TOOL]

        if Speaker.SPEAKER_INFO_PART_FROM in speaker_info.keys():
            self.part_from_speaker = speaker_info[Speaker.SPEAKER_INFO_PART_FROM]

    def get_speaker_info_dict(self):
        speaker_info = {}

        if self.gender == Gender.MALE:
            speaker_info[Speaker.SPEAKER_INFO_GENDER] = 'm'
        elif self.gender == Gender.FEMALE:
            speaker_info[Speaker.SPEAKER_INFO_GENDER] = 'f'

        speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZED] = self.is_synthesized

        if self.synthesis_tool is not None:
            speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_TOOL] = self.synthesis_tool

        if self.synthesis_voice is not None:
            speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_VOICE] = self.synthesis_voice

        if self.synthesis_effects is not None:
            speaker_info[Speaker.SPEAKER_INFO_SYNTHESIZER_EFFECTS] = self.synthesis_effects

        if self.part_from_speaker is not None:
            speaker_info[Speaker.SPEAKER_INFO_PART_FROM] = self.part_from_speaker

        return speaker_info
