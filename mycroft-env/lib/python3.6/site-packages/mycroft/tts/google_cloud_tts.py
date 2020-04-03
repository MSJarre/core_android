# # Copyright 2017 Mycroft AI Inc.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #    http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# #
#
# from mycroft.tts import TTSValidator
# from mycroft.tts.remote_tts import RemoteTTS
# from mycroft.configuration import Configuration
# from requests.auth import HTTPBasicAuth
#
# from google.cloud import texttospeech
#
#
# from mycroft.util.log import LOG
#
#
# class GoogleCloudTTS(RemoteTTS):
#     PARAMS = {'accept': 'audio/wav'}
#
#     def __init__(self, lang, config,
#                  url="https://stream-fra.watsonplatform.net/text-to-speech/api"):
#         super(GoogleCloudTTS, self).__init__(lang, config, url, '/v1/synthesize',
#                                         GoogleCloudTTSValidator(self))
#         self.type = "wav"
#         conf = self.config.get("credential").get("json")
#         password = self.config.get("password")
#         apikey = self.config.get("apikey")
#         # self.auth = HTTPBasicAuth(user, password)
#         self.auth =
#
#     def build_request_params(self, sentence):
#         params = self.PARAMS.copy()
#         params['LOCALE'] = self.lang
#         params['voice'] = self.voice
#         params['text'] = sentence.encode('utf-8')
#         return params
#
#
# class GoogleCloudTTSValidator(TTSValidator):
#     def __init__(self, tts):
#         super(GoogleCloudTTSValidator, self).__init__(tts)
#
#     def validate_lang(self):
#         # TODO
#         pass
#
#     def validate_connection(self):
#         config = Configuration.get().get("tts", {}).get("watson", {})
#         apikey = config.get("apikey")
#         if apikey:
#             return
#         else:
#             raise ValueError('user and/or password for IBM tts is not defined')
#
#     def get_tts_class(self):
#         return GoogleCloudTTS
